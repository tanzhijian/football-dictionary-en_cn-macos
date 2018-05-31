# -*- coding: utf-8 -*-

"""
测试转换函数
"""

import unittest

from converter.convert import (
    read_data, render_template, data, template)


class ConvertTestCase(unittest.TestCase):

    def setUp(self):
        self.entry_list = []

    def test_read_data(self):
        self.assertFalse(self.entry_list)
        self.entry_list.extend(read_data(data))
        self.assertTrue(self.entry_list)

    def test_render_template(self):
        xml = render_template(self.entry_list, template)
        self.assertTrue(xml)
