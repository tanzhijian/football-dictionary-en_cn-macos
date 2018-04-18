# -*- coding: utf-8 -*-

"""
测试转换函数
"""

import unittest

from converter.convert import (
    load_dataset, render_template, dataset, template_file)


class ConvertTestCase(unittest.TestCase):

    def test_load_dataset(self):
        data = load_dataset(dataset)
        self.assertTrue(data)

    def test_render_template(self):
        template = render_template(dataset, template_file)
        self.assertTrue(template)
