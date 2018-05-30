#!/usr/bin/env bash

python -m rasa_nlu.evaluate \
    --data ./dataset/dialogflow/weather/RASA_format_dataset/data.json \
    --config ./pipeline/MITIE+jieba.yml \
    --mode crossvalidation