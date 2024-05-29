#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/29  15:12
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
from PySide6.QtWidgets import QTableWidgetItem

from utility.SQLite_Tool import *

def refresh_table(window):
    sql = SQL()
    sql.select_grade()
    results = sql.results

    # 填写信息
    # 获取窗口中的表格组件
    table_widget = window.table_widget
    # 清除表格中的现有数据
    table_widget.clearContents()
    table_widget.setRowCount(len(results))  # 设置行数
    # 假设查询结果是一个元组列表，每个元组代表一行数据
    for row_index, row_data in enumerate(results):
        # 设置每行的单元格数据
        for column_index, data in enumerate(row_data):
            # 创建一个表格项并设置数据
            item = QTableWidgetItem(str(data))
            # 将表格项添加到表格的相应位置
            table_widget.setItem(row_index, column_index, item)

