[README written in English](README.en-US.md)
------------------------------

# 使用 RASA NLU 来构建中文自然语言理解系统（NLU）

本仓库提供前沿、详细和完备的中文自然语言理解系统构建指南。

## 在线演示

TODO

## 特性
- 提供中文语料库
- 提供语料库转换工具，帮助用户转移语料数据
- 提供多种基于 RASA NLU 的中文语言处理流程
- 提供模型性能评测工具，帮助自动选择和优化模型

## 系统要求

Python 3 (也许支持 python2, 但未经过良好测试)

## 处理流程

详情请访问 [workflow.md](workflow.md)

## 可用 pipeline 列表
### MITIE+jieba
#### 描述
* jieba 提供中文分词功能
* MITIE 负责 `intent classification` 和 `slot filling`
#### 安装依赖的软件包
```bash
pip install git+https://github.com/mit-nlp/MITIE.git
pip install jieba
```
#### 下载所需的模型数据
MITIE 需要一个模型文件，在本人的另一个项目: [MITIE_Chinese_Wikipedia_corpus](https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus) 的 [release](https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/releases) 下载 `total_word_feature_extractor.dat.tar.gz`. 解压后将 `total_word_feature_extractor.dat` 放至 `data`
#### pipeline
```yaml
language: "zh"

pipeline:
- name: "nlp_mitie"
  model: "data/total_word_feature_extractor.dat"
- name: "tokenizer_jieba"
- name: "ner_mitie"
- name: "ner_synonyms"
- name: "intent_featurizer_mitie"
- name: "intent_classifier_sklearn"
```

#### 训练脚本
```bash
trainer/MITIE+jieba.bash
```

#### 评估脚本
```bash
cross_validation/MITIE+jieba.bash
```

### tensorflow_embedding

#### 描述
* jieba 提供中文分词功能
* tensorflow_embedding 负责 `intent classification`
* MITIE 负责 `slot filling`

#### 安装依赖的软件包
```bash
pip install git+https://github.com/mit-nlp/MITIE.git
pip install jieba
pip install tensorflow
```
#### 下载所需的模型数据
MITIE 需要一个模型文件，在本人的另一个项目: [MITIE_Chinese_Wikipedia_corpus](https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus) 的 [release](https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/releases) 下载 `total_word_feature_extractor.dat.tar.gz`. 解压后将 `total_word_feature_extractor.dat` 放至 `data`
#### pipeline
```yaml
language: "zh"

pipeline:
- name: "nlp_mitie"
  model: "data/total_word_feature_extractor.dat"
- name: "tokenizer_jieba"
- name: "intent_featurizer_count_vectors"
- name: "intent_classifier_tensorflow_embedding"
- name: "ner_mitie"
- name: "ner_synonyms"
```

#### 训练脚本
```bash
trainer/tensorflow_embedding.bash
```

#### 评估脚本
```bash
cross_validation/tensorflow_embedding.bash
```

### spacy
#### 描述
* [Chinese_models_for_SpaCy](https://github.com/howl-anderson/Chinese_models_for_SpaCy) 负责 `intent classification` and `slot filling`
#### 安装依赖的软件包
```bash
pip install https://github.com/howl-anderson/Chinese_models_for_SpaCy/releases/download/v2.0.3/zh_core_web_sm-2.0.3.tar.gz
./spacy_model_link.bash
```
#### pipeline
```yaml
language: "zh"

pipeline:
- name: "nlp_spacy"
  model: "zh"
- name: "tokenizer_spacy"
- name: "intent_entity_featurizer_regex"
- name: "intent_featurizer_spacy"
- name: "ner_crf"
- name: "ner_synonyms"
- name: "intent_classifier_sklearn"
```

#### 训练脚本
```bash
trainer/spacy.bash
```

#### 评估脚本
```bash
cross_validation/spacy.bash
```


## 性能测试
### DialogFlow > weather
<table>
    <thead>
    <tr>
        <th></th>
        <th colspan="6">Intent</th>
        <th colspan="6">Entity</th>
    </tr>
    <tr>
        <th></th>
        <th colspan="3">train</th>
        <th colspan="3">test</th>
        <th colspan="3">train</th>
        <th colspan="3">test</th>
    </tr>
    <tr>
        <th>No</th>
        <th>ACC</th>
        <th>F1</th>
        <th>PRC</th>
        <th>ACC</th>
        <th>F1</th>
        <th>PRC</th>
        <th>ACC</th>
        <th>F1</th>
        <th>PRC</th>
        <th>ACC</th>
        <th>F1</th>
        <th>PRC</th>
    </tr>
    </thead>
    <tbody>
    {% for pipeline in pipeline_list %}
    <tr>
        <td>{{ loop.index }}</td>
        <td>{{ pipeline.result.intent.train.ACC }}</td>
        <td>{{ pipeline.result.intent.train.F1 }}</td>
        <td>{{ pipeline.result.intent.train.PRC }}</td>
        <td>{{ pipeline.result.intent.test.ACC }}</td>
        <td>{{ pipeline.result.intent.test.F1 }}</td>
        <td>{{ pipeline.result.intent.test.PRC }}</td>
        <td>{{ pipeline.result.entity.train.ACC }}</td>
        <td>{{ pipeline.result.entity.train.F1 }}</td>
        <td>{{ pipeline.result.entity.train.PRC }}</td>
        <td>{{ pipeline.result.entity.test.ACC }}</td>
        <td>{{ pipeline.result.entity.test.F1 }}</td>
        <td>{{ pipeline.result.entity.test.PRC }}</td>
    </tr>
    {% endfor %}
    </tbody>
    <tfoot>
        <tr>
            <td colspan="13">
                ACC: Accuracy; F1: F1-score; PRC: Precision;
            </td>
        </tr>
    </tfoot>
</table>

### Model List

| No  | Pipeline             | Configure                                                                    |
|-----|----------------------|------------------------------------------------------------------------------|
{% for pipeline in pipeline_list %}
| {{ loop.index }} | {{ pipeline.name }} | {{ pipeline.configure_description.zh }} |
{% endfor %}

## 如何贡献

请阅读 [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) , 然后提交 pull requests 给我们.

## 版本化控制

我们使用 [SemVer](http://semver.org/) 做版本化的标准. 查看 `tags` 以了解所有的版本.

## 作者

* **Xiaoquan Kong** - *Initial work* - [howl-anderson](https://github.com/howl-anderson)

更多贡献者信息，请参考 `contributors`.

## 版权

MIT License - 详见 [LICENSE.md](LICENSE.md)

## 致谢

* TODO
