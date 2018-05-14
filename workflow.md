## 安装依赖

```console
$ pip install -r requirements.txt
```

## 准备数据
### 获取训练数据
 - 从 `dialogflow.com` 的 `Prebuilt Agent` 找到 `Weather` 并将其导入，在导入的新项目中，将项目导出
 - 数据文件位于：`dataset/dialogflow/weather/Weather`
### 获取 MITIE 模型数据
  - 从 [MITIE_Chinese_Wikipedia_corpus](https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/) 项目下载 [pre-trained model](https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/releases/download/0.1/total_word_feature_extractor.dat.tar.gz)
  - 解压缩后，将文件 `total_word_feature_extractor.dat` 移动至 `data/` 目录
### 转换格式
 - 使用脚本 `convert_dataset_format.py`
## 训练模型

使用脚本 `train.bash`



## 运行 HTTP 服务器

使用脚本 `http_server.bash`

## 交叉检验模型性能

使用脚本 `crossvalidation.bash`