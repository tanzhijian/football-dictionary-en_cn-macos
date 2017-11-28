# -*- coding: utf-8 -*-

"""
把 csv 转换为可以被 Dictionary Development Kit 处理的 xml 的脚本
"""

import csv

from jinja2 import Environment, FileSystemLoader

FILENAME = 'football_terms_dic.csv'
INPUT_FILENAME = 'template.xml'
OUTPUT_FILENAME = 'football_terms_dic.xml'


def load_dataset(filename):
    with open(filename) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            print(row)


def render_template(input_filename, output_filename):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template(input_filename).render()
    with open(output_filename, 'wt') as f:
        f.write(template)


if __name__ == '__main__':
    load_dataset(FILENAME)
    render_template(INPUT_FILENAME, OUTPUT_FILENAME)
