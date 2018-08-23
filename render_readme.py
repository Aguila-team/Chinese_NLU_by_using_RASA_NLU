#!/usr/bin/env python
import json
import os

from jinja2 import Template

current_dir = os.path.dirname(os.path.abspath(__file__))


def get_file_content(relative_file_path):
    file_path = os.path.join(current_dir, relative_file_path)

    with open(file_path) as fd:
        return fd.read()


def render_file(input_bare_file, render_variable):
    input_file = os.path.join(current_dir, input_bare_file)

    # generate bare output file
    file_segment = input_bare_file.split(".")
    del file_segment[-2]
    bare_output_file = ".".join(file_segment)

    output_file = os.path.join(current_dir, bare_output_file)

    with open(input_file, encoding='utf_8') as input_fd, open(output_file, mode='w', encoding='utf_8') as output_fd:
        template = Template(input_fd.read())

        rendered_string = template.render(pipeline_list=render_variable)

        output_fd.write(rendered_string)


def main():
    with open('result.json') as fd:
        render_variable = json.load(fd)

    input_file_list = [
        'README.tpl.md',
        'README.en-US.tpl.md'
    ]

    for input_file in input_file_list:
        render_file(input_file, render_variable)
