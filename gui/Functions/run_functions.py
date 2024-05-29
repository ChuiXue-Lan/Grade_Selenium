#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/29  14:14
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
import threading
import time

from WebScraper import WebScraper
from gui.uis.dialog.ProcessDialog import ProcessDialog
from utility import Config_Tool


def run(window):
    # 修改配置文件
    new_file_path = window.file_path_line.text()
    new_web_site = window.web_address_line.text()

    Config_Tool.modify_ini_file(new_file_path, new_web_site)

    # 运行爬虫
    web_scraper = WebScraper()

    # 处理数据
    # 获取数据总数
    web_scraper.sql.get_info_num()
    info_num = web_scraper.sql.info_num

    # 创建进度对话框
    my_process_dialog = ProcessDialog(web_scraper, info_num)

    # 创建线程：进度对话框，爬虫
    process_dialog_thread = threading.Thread(target=process_dialog, args=(my_process_dialog,))
    scraper_thread = threading.Thread(target=scraper, args=(web_scraper,))

    # 打开进度对话框
    my_process_dialog.show()

    # 运行线程
    process_dialog_thread.start()
    scraper_thread.start()

    # 关闭数据库
    web_scraper.sql.close_connection()

# 模拟爬虫
def deal(web_scraper):
    count = 0
    while count < 39:
        count += 1
        web_scraper.finish_num += 1
        time.sleep(1)
        print('爬取数据中...')

def process_dialog(my_process_dialog):
    my_process_dialog.exec_()

def scraper(web_scraper):
    deal(web_scraper)
    # web_scraper.deal_data()