# -*- coding: utf-8 -*-

"""
把 csv 转换为可以被 Dictionary Development Kit 处理的 xml 的脚本
"""

import csv

FILENAME = 'football_terms_dic.csv'


def load_dataset(filename):
    with open(filename) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            print(row)


if __name__ == '__main__':
    load_dataset(FILENAME)
