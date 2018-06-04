[中文版本的 README](README.md)
------------------------------

# Use RASA NLU to build a Chinese Natural Language Understanding System (NLU)

This repository provides cutting-edge, detailed and complete guidance for the construction of a Chinese natural language understanding system.

## Online Demo

TODO

## Features
- Provide Chinese Corpus
- Provide corpus conversion tool to help users transfer corpus data
- Provide multiple Chinese language processing workflow based on RASA NLU
- Provide model performance evaluation tools to help automatically select and optimize models

## System Requirements

Python 3 (perhaps supporting python2 but not tested well)

## Process Flow

For more information, visit [workflow.md](workflow.md)

## available pipeline list
### MITIE+jieba
#### Install Dependent Packages
```bash
Pip install git+https://github.com/mit-nlp/MITIE.git
Pip install jieba
```
#### Download the required model data
MITIE needs a model file, in my another project: [MITIE_Chinese_Wikipedia_corpus] (https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus) [release] (https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/ Releases) Download `total_word_feature_extractor.dat.tar.gz`. Extract `total_word_feature_extractor.dat` to `data`
#### pipeline
```yaml
Language: "zh"

Pipeline:
- name: "nlp_mitie"
  Model: "data/total_word_feature_extractor.dat"
- name: "tokenizer_jieba"
- name: "ner_mitie"
- name: "ner_synonyms"
- name: "intent_featurizer_mitie"
- name: "intent_classifier_sklearn"
```

#### Training Script
```bash
Trainer/MITIE+jieba.bash
```

#### Evaluation Script
```bash
Cross_validation/MITIE+jieba.bash
```

### tensorflow_embedding

**TODO**: Wait [New feature: component 'count_vectors_featurizer' can use 'tokens' provide by tokenizers](https://github.com/RasaHQ/rasa_nlu/pull/1115) After finishing, you can use Chinese.

### spacy

**TODO**: After waiting for [Models for SpaCy that support Chinese](https://github.com/howl-anderson/Chinese_models_for_SpaCy) to finish, you can use Chinese.


## Performance Testing
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
    <tr>
        <td>1</td>
        <td>0.986</td>
        <td>0.986</td>
        <td>0.986</td>
        <td>0.665</td>
        <td>0.631</td>
        <td>0.648</td>
        <td>0.987</td>
        <td>0.987</td>
        <td>0.988</td>
        <td>0.967</td>
        <td>0.968</td>
        <td>0.973</td>
    </tr>
    </tbody>
    <tfoot>
        <tr>
            <td colspan="13">
                ACC: Accuracy; F1: F1-score; PRC: Precision;
            </td>
        </tr>
    </tfoot>
</table>

**Model List**

| No | Pipeline | Configure |
|-----|-------------|----------------------------- -------------------------------------------------|
| 1 | MITIE+jieba | `total_word_feature_extractor.dat` provided by the `MITIE_Chinese_Wikipedia_corpus` project |

## How to contribute

Please read [CONTRIBUTING.md] (https://gist.github.com/PurpleBooth/b24679402957c63ec426) and submit pull requests to us.

## Version Control

We use [SemVer] (http://semver.org/) as a versioned standard. See `tags` for all versions.

## Authors

* **Xiaoquan Kong** - *Initial work* - [howl-anderson](https://github.com/howl-anderson)

For more contributor information, please refer to `contributors`.

## Copyright

MIT License - See [LICENSE.md](LICENSE.md) for details

## Acknowledges

* TODO