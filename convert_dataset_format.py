import os

from rasa_nlu.convert import convert_training_data

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(CURRENT_DIR, "dataset/dialogflow/weather/Weather")
output_path = os.path.join(CURRENT_DIR, "dataset/dialogflow/weather/RASA_format_dataset/data.json")


def convert_alien_format_dataset(input_path, output_path):
    convert_training_data(
        data_file=input_path,
        out_file=output_path,
        output_format="json",
        language="zh-cn"
    )


convert_alien_format_dataset(input_path, output_path)
