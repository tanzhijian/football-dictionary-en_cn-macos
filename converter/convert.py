# -*- coding: utf-8 -*-
"""
把 csv 转换为可供 Dictionary Development Kit 处理的 xml 的脚本
"""

import csv
from pathlib import Path

from jinja2 import Template

data = Path(Path.cwd(), 'data.csv')
template = Path(Path.cwd(), 'converter/template.xml')
output_file = Path(Path.cwd(), 'converter/data.xml')


def read_data(data):
    """读取词典 csv 数据集并转换为可供 jinja2 操作的列表数据结构
    Args: 
        data: 存储词典数据集的 data.csv，在根文件夹中
    Returns: 
        一个可供 jinja2 转换操作的双层嵌套列表，其中每个元素为 csv 数据集中的一行数据
    """
    with open(data) as f:
        entries = list(csv.reader(f))
    return entries


def render_template(entries, template):
    """用预先准备好的模板将读取的词典数据渲染为
        可供 Dictionary Development Kit 处理的数据格式
    Args: 
        entries: 已读取的可供 jinja2 转换操作的双层嵌套列表，
            其中每个元素为 csv 数据集中的一行数据
        template: 预先准备好可供渲染的 xml 模板文件，在当前文件夹中
    Returns: 
        一份渲染完毕的可供 Dictionary Development Kit 处理的文本字符串
    """
    with open(template) as f:
        xml = f.read()
    return Template(xml).render(entries=entries)


def main():
    """将转换好的文本字符串写入文件待使用"""
    with open(output_file, 'w') as f:
        f.write(render_template(read_data(data), template))


if __name__ == '__main__':
    main()
