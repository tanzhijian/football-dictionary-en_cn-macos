# -*- coding: utf-8 -*-

"""
把 csv 转换为可以被 Dictionary Development Kit 处理的 xml 的脚本
"""

import csv
import os

from jinja2 import Environment, FileSystemLoader

data = os.getcwd() + '/data.csv'
template = 'converter/template.xml'
output = 'converter/data.xml'


def load_data(data):
    with open(data) as f:
        f_csv = csv.reader(f)
        __ = next(f_csv)
        entry_list = [row for row in f_csv]
    return entry_list


def render_template(entry_list, template):
    env = Environment(loader=FileSystemLoader('./'))
    return env.get_template(template).render(entry_list=entry_list)


def main():
    with open(output, 'w') as f:
        f.write(render_template(load_data(data), template))


if __name__ == '__main__':
    main()
