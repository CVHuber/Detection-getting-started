# Detection-getting-started

基于PyTorch的YOLOv3项目实现，支持训练自定义数据集，前向推理，模型测试与评估！

## 安装运行环境

将github代码克隆到本地

```shell
$ git clone https://github.com/CVHuber/Detection-getting-started.git
```

进入项目文件夹并安装运行环境

```shell
$ cd Detection-getting-started/
$ pip install -r requirements.txt
```

## 模型测试

模型权重文件下载

```shell
$ cd weights/
$ bash download_weights.sh
```

模型测试

```shell
$ python test.py --weights_path weights/yolov3.weights
```

## 训练Pascal Voc2007数据集

[参考]: https://mp.weixin.qq.com/s/QgYeZnGWYysEAdI94lar_A

训练命令

```shell
$ train.py [-h] [--epochs EPOCHS] [--batch_size BATCH_SIZE]
                [--gradient_accumulations GRADIENT_ACCUMULATIONS]
                [--model_def MODEL_DEF] [--data_config DATA_CONFIG]
                [--pretrained_weights PRETRAINED_WEIGHTS] [--n_cpu N_CPU]
                [--img_size IMG_SIZE]
                [--checkpoint_interval CHECKPOINT_INTERVAL]
                [--evaluation_interval EVALUATION_INTERVAL]
                [--compute_map COMPUTE_MAP]
                [--multiscale_training MULTISCALE_TRAINING]
                [--device_id GPU_ID]
```

训练日志

```
---- [Epoch 7/100, Batch 7300/14658] ----
+------------+--------------+--------------+--------------+
| Metrics    | YOLO Layer 0 | YOLO Layer 1 | YOLO Layer 2 |
+------------+--------------+--------------+--------------+
| grid_size  | 16           | 32           | 64           |
| loss       | 1.554926     | 1.446884     | 1.427585     |
| x          | 0.028157     | 0.044483     | 0.051159     |
| y          | 0.040524     | 0.035687     | 0.046307     |
| w          | 0.078980     | 0.066310     | 0.027984     |
| h          | 0.133414     | 0.094540     | 0.037121     |
| conf       | 1.234448     | 1.165665     | 1.223495     |
| cls        | 0.039402     | 0.040198     | 0.041520     |
| cls_acc    | 44.44%       | 43.59%       | 32.50%       |
| recall50   | 0.361111     | 0.384615     | 0.300000     |
| recall75   | 0.222222     | 0.282051     | 0.300000     |
| precision  | 0.520000     | 0.300000     | 0.070175     |
| conf_obj   | 0.599058     | 0.622685     | 0.651472     |
| conf_noobj | 0.003778     | 0.004039     | 0.004044     |
+------------+--------------+--------------+--------------+
Total Loss 4.429395
---- ETA 0:35:48.821929
```

参考：https://github.com/eriklindernoren/PyTorch-YOLOv3