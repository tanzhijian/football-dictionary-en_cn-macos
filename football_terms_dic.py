# -*- coding: utf-8 -*-

"""
把 csv 转换为可以被 Dictionary Development Kit 处理的 xml 的脚本
"""

import csv

from jinja2 import Environment, FileSystemLoader

DATASET = 'football_terms_dic.csv'
INPUT_FILENAME = 'template.xml'
OUTPUT_FILENAME = 'football_terms_dic.xml'


def load_dataset(dataset):
    entry_list = []
    with open(dataset) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            entry_list.append(row)
    return entry_list


def render_template(dataset, input_filename, output_filename):
    entry_list = load_dataset(dataset)
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template(input_filename).render(entry_list=entry_list)
    with open(output_filename, 'wt') as f:
        f.write(template)


if __name__ == '__main__':
    render_template(DATASET, INPUT_FILENAME, OUTPUT_FILENAME)
