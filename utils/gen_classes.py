from xml.etree.ElementTree import parse
import os
import xml.etree.ElementTree as ET

xml_dir = '../data/voc2007/train/Annotations'
saved_classes_file = '../data/voc2007/train/classes.names'
classes = set()
for file in os.listdir(xml_dir):
    file_path = os.path.join(xml_dir, file)
    tree = ET.parse(file_path)
    root = tree.getroot()
    for obj in root.iter('object'):
        cls = obj.find('name').text
        classes.add(cls)

with open(saved_classes_file, 'w') as f:
    for cla in classes:
        f.write(cla + '\n')
print('num classes:', len(classes))
print('classes:', classes)


