#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/22  19:50
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-

import time

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QDialog, QPushButton, QLabel, QProgressBar


class ProcessDialog(QDialog):
    def __init__(self, web_scraper, total_num):
        super().__init__()
        self.finish_label = None
        self.finish_button = None
        self.setWindowTitle('爬虫进度')
        self.resize(500, 200)
        self.widget_list()
        self.total_num = total_num  # 总数目
        self.finish_num = 0  # 已完成数目
        self.web_scraper = web_scraper

    def widget_list(self):
        self.add_widget_process()
        self.add_widget_finish()

    def add_widget_finish(self):
        self.finish_button = QPushButton(self)
        self.finish_button.move(200, 120)
        self.finish_button.resize(80, 40)
        self.finish_button.setText('完成')
        self.finish_button.clicked.connect(self.close)
        self.finish_button.setVisible(False)

        self.finish_label = QLabel(self)
        self.finish_label.move(100, 80)
        self.finish_label.setText('数据爬取结束，点击‘完成’按钮返回！')
        self.finish_label.setVisible(False)

    def add_widget_process(self):
        pb = QProgressBar(self)
        pb.resize(400, 30)
        pb.move(50, 20)
        pb.setRange(0, 100)  # 设置值范围
        pb.setValue(0)  # 设置当前值

        pass  # 重置当前值
        # pb.reset()

        pass  # 展示文本格式设置
        pb.setFormat('当前进度：%p%')

        pass  # 展示字符对齐方式
        pb.setAlignment(Qt.AlignHCenter)

        pass  # 可用信号
        timer = QTimer(pb)

        def change_progress():
            if pb.value() >= pb.maximum():
                self.finish_button.setVisible(True)
                self.finish_label.setVisible(True)
                timer.stop()
            self.finish_num = self.web_scraper.finish_num
            print('已完成数目：' + str(self.finish_num) + ' 总数目：' + str(self.total_num))
            if self.finish_num == self.total_num:
                pb.setValue(pb.maximum())
            else:
                pb.setValue(int(self.finish_num / self.total_num * 100))

        timer.timeout.connect(change_progress)
        timer.start(1000)
