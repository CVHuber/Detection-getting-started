import os
from datetime import datetime
from shutil import copy
import xml.etree.ElementTree as ET
from absl import app, logging


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def main(argv):
    images = '../data/voc2007/train/JPEGImages'
    images = os.path.abspath(images)
    annotation = '../data/voc2007/train/Annotations'
    annotation = os.path.abspath(annotation)
    classes_names = '../data/voc2007/train/classes.names'
    classes_names = os.path.abspath(classes_names)
    new_dir = '../data/custom'
    rebuild = True
    VOCtoYOLO = True

    # create two new folders
    os.makedirs(new_dir)

    classes = []
    if classes_names is not None:
        # copy the classes file it self to the new directory
        copy(classes_names,
             new_dir)
        # create the classes list
        with open(classes_names) as f:
            classes = [my_class.strip() for my_class in f]

    if rebuild:

        new_dir_images = new_dir + '/images'
        new_dir_annotation = new_dir + '/annotation'
        yolo_dir = new_dir + '/labels'

        # create two folders in the new images: images and annotation
        os.makedirs(new_dir_images)
        os.makedirs(new_dir_annotation)
        new_dir_images = os.path.abspath(new_dir_images)
        new_dir_annotation = os.path.abspath(new_dir_annotation)
        if VOCtoYOLO:
            os.makedirs(yolo_dir)

        counter = 0
        if os.path.exists(annotation):

            # count the number of annotation files
            annotation_count = len([file for file in os.listdir(annotation)])
            train_count = annotation_count - (annotation_count // 3)

            # create train and validation files
            train = open(os.path.join(new_dir, 'train.txt'), 'w')
            validation = open(os.path.join(new_dir, 'valid.txt'), 'w')


            for annotation_file_name in os.listdir(annotation):
                annotation_file = os.path.splitext(annotation_file_name)[0]
                image_file_name = annotation_file + '.jpg'


                # if image exists move both annotation and images to new directory
                if os.path.exists(os.path.join(images, image_file_name)):
                    # copy annotation
                    copy(os.path.join(annotation, annotation_file_name),
                         os.path.join(new_dir_annotation, annotation_file_name))
                    copy(os.path.join(images, image_file_name),
                         os.path.join(new_dir_images, image_file_name))

                    # print('copying ' + annotation_file_name + ' & ' + image_file_name + ' >>> ' + new_dir)
                    counter += 1
                    if counter < train_count:
                        train.write(os.path.join(new_dir_images, image_file_name) + '\n')
                    else:
                        validation.write(os.path.join(new_dir_images, image_file_name) + '\n')

                    # if convert VOC to YOLO
                    if VOCtoYOLO and classes:
                        # create the new Yolo file
                        yolo_file = open(os.path.join(yolo_dir, annotation_file) + '.txt', 'w')
                        tree = ET.parse(os.path.join(annotation, annotation_file_name))
                        root = tree.getroot()
                        size = root.find('size')
                        w = int(size.find('width').text)
                        h = int(size.find('height').text)
                        for obj in root.iter('object'):
                            cls = obj.find('name').text
                            cls_id = classes.index(cls)
                            xmlbox = obj.find('bndbox')
                            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                                 float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                            bb = convert((w, h), b)

                            yolo_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

        logging.info('Copied ' + str(counter) + ' Images and Annotation')


if __name__ == '__main__':
    app.run(main)