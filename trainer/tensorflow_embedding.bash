#!/usr/bin/env bash

python -m rasa_nlu.train \
   -o ./projects \
   -d ./dataset/dialogflow/weather/RASA_format_dataset/data.json \
   -c ./pipeline/tensorflow_embedding.yml