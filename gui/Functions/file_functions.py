#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/29  12:59
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
import os

from PySide6.QtWidgets import QFileDialog, QMessageBox

from utility.SQLite_Tool import SQL


# 选择Excel文件
def select_file(window, *args, **kwargs):
    caption = args[0]
    directory = args[1]
    file_filter = args[2]
    initial_filter = args[3]
    file = QFileDialog.getOpenFileName(window, caption, directory, file_filter, initial_filter)
    window.file_path_line.setText(file[0])


# 保存Excel文件
def save_file(window, *args, **kwargs):
    caption = args[0]
    directory = args[1]
    file_filter = args[2]
    initial_filter = args[3]
    file = QFileDialog.getSaveFileName(window, caption, directory, file_filter, initial_filter)


    # ini写入file【0】 暂不实现，价值不大
    save_path = file[0]
    if save_path:
        # 获取目录路径
        directory_path = os.path.dirname(save_path)

        # 检查目录是否存在，如果不存在则创建
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # 在目标路径创建文件
        with open(save_path, 'w'):
            pass  # 在此处添加文件的具体内容
            sql = SQL()
            sql.writeExcel(save_path)
            suc_msg = QMessageBox(QMessageBox.Information, '提示', '保存成功！')
            suc_msg.exec_()
