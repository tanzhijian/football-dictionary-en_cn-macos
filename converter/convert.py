# -*- coding: utf-8 -*-

"""
把 csv 转换为可以被 Dictionary Development Kit 处理的 xml 的脚本
"""

import csv
import os

from jinja2 import Environment, FileSystemLoader

dataset = os.getcwd() + '/data.csv'
template_file = 'converter/template.xml'
output_file = 'converter/data.xml'


def load_dataset(dataset):
    with open(dataset) as f:
        f_csv = csv.reader(f)
        __ = next(f_csv)
        entry_list = [row for row in f_csv]
    return entry_list


def render_template(dataset, template_file):
    entry_list = load_dataset(dataset)
    env = Environment(loader=FileSystemLoader('./'))
    return env.get_template(template_file).render(entry_list=entry_list)


def main():
    with open(output_file, 'w') as f:
        f.write(render_template(dataset, template_file))


if __name__ == '__main__':
    main()
