## full pipeline registry should look like below:
# pipeline_registry = [
#     {
#         'name': '',
#         'configure_description': {
#             'zh': '',
#             'en': '',
#         },
#         'settings': {
#             'data_path': '',
#             'config_path': '',
#         }
#     }
# ]
import os

pipeline_registry = [
    {
        'name': 'MITIE+jieba',
        'configure_description': {
            'zh': '使用 `MITIE_Chinese_Wikipedia_corpus` 项目提供的 `total_word_feature_extractor.dat`',
            'en': '`total_word_feature_extractor.dat` provided by the `MITIE_Chinese_Wikipedia_corpus` project',
        }
    },
    {
        'name': 'spacy',
        'configure_description': {
            'zh': '使用 `Chinese_models_for_SpaCy` 项目提供的中文 SpaCy 模型',
            'en': 'Chinese SpaCy model provided by the `Chinese_models_for_SpaCy` project',
        }
    },
    {
        'name': 'spacy',
        'configure_description': {
            'zh': '使用 `Chinese_models_for_SpaCy` 项目提供的中文 SpaCy 模型',
            'en': 'Chinese SpaCy model provided by the `Chinese_models_for_SpaCy` project',
        }
    },
]

for pipeline in pipeline_registry:
    default_pipeline_data_path = './dataset/dialogflow/weather/RASA_format_dataset/data.json'

    default_config_path = os.path.join(
        './pipeline',
        pipeline['name'] + '.yml'
    )

    if 'settings' not in pipeline:  # auto generate pipeline settings
        pipeline['settings'] = {}

    settings = pipeline['settings']

    if 'data_path' not in settings:
        settings['data_path'] = default_pipeline_data_path

    if 'config_path' not in settings:
        settings['config_path'] = default_config_path

