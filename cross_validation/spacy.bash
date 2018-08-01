#!/usr/bin/env bash

python -m rasa_nlu.evaluate \
    --data ./dataset/dialogflow/weather/RASA_format_dataset/data.json \
    --config ./pipeline/spacy.yml \
    --mode crossvalidation