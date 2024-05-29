# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////

# 槽函数
# ///////////////////////////////////////////////////////////////
from gui.Functions.file_functions import *
from gui.Functions.run_functions import *
from gui.Functions.table_functions import *


class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,  # 用于说明再菜单栏上部还是底部
            "is_active" : True
        },
        {
            "btn_icon": "icon_table.svg",
            "btn_id": "btn_page_2",
            "btn_text": "Open table",
            "btn_tooltip": "Open table",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_page_3",
            "btn_text": "Open help",
            "btn_tooltip": "Open help",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_day.svg",
            "btn_id": "btn_change_themes",
            "btn_text": "Change themes",
            "btn_tooltip": "Change themes",
            "show_top": False,
            "is_active": False
        }
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
            "is_active" : False
        }

    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        # self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # 加载页面、左列和右列的对象
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # 自定义组件
        # 文件路径
        # Label
        self.file_path_label = QLabel('文件路径：')

        # Edit
        self.file_path_line = PyLineEdit(
            text="",
            place_holder_text="请选择文件",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.file_path_line.setMinimumHeight(40)

        # 选择文件按钮
        self.select_file_btn = PyPushButton(
            text="浏览",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.select_file_btn.setMinimumWidth(120)
        self.select_file_btn.setMinimumHeight(40)

        # 查询网址
        # Label
        self.web_address_label = QLabel('网址：        ')

        # Edit
        self.web_address_line = PyLineEdit(
            text="",
            place_holder_text="请输入网址",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.web_address_line.setMinimumHeight(40)

        # 保存路径
        self.file_save_path_label = QLabel('保存路径：')
        self.file_save_path_line = PyLineEdit(
            text="",
            place_holder_text="请选择保存路径",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.file_save_path_line.setMinimumHeight(40)
        self.file_save_path_btn = PyPushButton(
            text="浏览",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.file_save_path_btn.setMinimumWidth(120)
        self.file_save_path_btn.setMinimumHeight(40)

        # 运行按钮
        self.run_btn = PyPushButton(
            text="运行",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.run_btn.setMinimumWidth(120)
        self.run_btn.setMinimumHeight(40)

        # 表格
        self.table_widget = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(23)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_0 = QTableWidgetItem()
        self.column_0.setTextAlignment(Qt.AlignCenter)
        self.column_0.setText("NAME")

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("NICK")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("PASS")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("PASS")

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText("PASS")

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText("PASS")

        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignCenter)
        self.column_6.setText("PASS")

        self.column_7 = QTableWidgetItem()
        self.column_7.setTextAlignment(Qt.AlignCenter)
        self.column_7.setText("PASS")

        self.column_8 = QTableWidgetItem()
        self.column_8.setTextAlignment(Qt.AlignCenter)
        self.column_8.setText("PASS")

        self.column_9 = QTableWidgetItem()
        self.column_9.setTextAlignment(Qt.AlignCenter)
        self.column_9.setText("PASS")

        self.column_10 = QTableWidgetItem()
        self.column_10.setTextAlignment(Qt.AlignCenter)
        self.column_10.setText("PASS")

        self.column_11 = QTableWidgetItem()
        self.column_11.setTextAlignment(Qt.AlignCenter)
        self.column_11.setText("PASS")

        self.column_12 = QTableWidgetItem()
        self.column_12.setTextAlignment(Qt.AlignCenter)
        self.column_12.setText("PASS")

        self.column_13 = QTableWidgetItem()
        self.column_13.setTextAlignment(Qt.AlignCenter)
        self.column_13.setText("PASS")

        self.column_14 = QTableWidgetItem()
        self.column_14.setTextAlignment(Qt.AlignCenter)
        self.column_14.setText("PASS")

        self.column_15 = QTableWidgetItem()
        self.column_15.setTextAlignment(Qt.AlignCenter)
        self.column_15.setText("PASS")

        self.column_16 = QTableWidgetItem()
        self.column_16.setTextAlignment(Qt.AlignCenter)
        self.column_16.setText("PASS")

        self.column_17 = QTableWidgetItem()
        self.column_17.setTextAlignment(Qt.AlignCenter)
        self.column_17.setText("PASS")

        self.column_18 = QTableWidgetItem()
        self.column_18.setTextAlignment(Qt.AlignCenter)
        self.column_18.setText("PASS")

        self.column_19 = QTableWidgetItem()
        self.column_19.setTextAlignment(Qt.AlignCenter)
        self.column_19.setText("PASS")

        self.column_20 = QTableWidgetItem()
        self.column_20.setTextAlignment(Qt.AlignCenter)
        self.column_20.setText("PASS")

        self.column_21 = QTableWidgetItem()
        self.column_21.setTextAlignment(Qt.AlignCenter)
        self.column_21.setText("PASS")

        self.column_22 = QTableWidgetItem()
        self.column_22.setTextAlignment(Qt.AlignCenter)
        self.column_22.setText("PASS")

        self.column_23 = QTableWidgetItem()
        self.column_23.setTextAlignment(Qt.AlignCenter)
        self.column_23.setText("PASS")

        # self.column_24 = QTableWidgetItem()
        # self.column_24.setTextAlignment(Qt.AlignCenter)
        # self.column_24.setText("PASS")
        #
        # self.column_25 = QTableWidgetItem()
        # self.column_25.setTextAlignment(Qt.AlignCenter)
        # self.column_25.setText("PASS")
        #
        # self.column_26 = QTableWidgetItem()
        # self.column_26.setTextAlignment(Qt.AlignCenter)
        # self.column_26.setText("PASS")

        # 设置列
        self.table_widget.setHorizontalHeaderItem(0, self.column_0)
        self.table_widget.setHorizontalHeaderItem(1, self.column_1)
        self.table_widget.setHorizontalHeaderItem(2, self.column_2)
        self.table_widget.setHorizontalHeaderItem(3, self.column_3)
        self.table_widget.setHorizontalHeaderItem(4, self.column_4)
        self.table_widget.setHorizontalHeaderItem(5, self.column_5)
        self.table_widget.setHorizontalHeaderItem(6, self.column_6)
        self.table_widget.setHorizontalHeaderItem(7, self.column_7)
        self.table_widget.setHorizontalHeaderItem(8, self.column_8)
        self.table_widget.setHorizontalHeaderItem(9, self.column_9)
        self.table_widget.setHorizontalHeaderItem(10, self.column_10)
        self.table_widget.setHorizontalHeaderItem(11, self.column_11)
        self.table_widget.setHorizontalHeaderItem(12, self.column_12)
        self.table_widget.setHorizontalHeaderItem(13, self.column_13)
        self.table_widget.setHorizontalHeaderItem(14, self.column_14)
        self.table_widget.setHorizontalHeaderItem(15, self.column_15)
        self.table_widget.setHorizontalHeaderItem(16, self.column_16)
        self.table_widget.setHorizontalHeaderItem(17, self.column_17)
        self.table_widget.setHorizontalHeaderItem(18, self.column_18)
        self.table_widget.setHorizontalHeaderItem(19, self.column_19)
        self.table_widget.setHorizontalHeaderItem(20, self.column_20)
        self.table_widget.setHorizontalHeaderItem(21, self.column_21)
        self.table_widget.setHorizontalHeaderItem(22, self.column_22)
        self.table_widget.setHorizontalHeaderItem(23, self.column_23)
        # self.table_widget.setHorizontalHeaderItem(24, self.column_24)
        # self.table_widget.setHorizontalHeaderItem(25, self.column_25)
        # self.table_widget.setHorizontalHeaderItem(26, self.column_26)

        # 刷新按钮
        self.refresh_btn = PyPushButton(
            text="刷新",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.refresh_btn.setMinimumWidth(120)
        self.refresh_btn.setMinimumHeight(40)

        # 导出按钮
        self.save_btn = PyPushButton(
            text="导出",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.save_btn.setMinimumWidth(120)
        self.save_btn.setMinimumHeight(40)

        # Label
        self.help_title_label = QLabel('使用手册')
        self.help_title_label.setStyleSheet(
            "font-size: 28pt"
        )
        self.help_text_label = QLabel(
            '''
① 在文件选择中选择要读取的学生信息Excel表格\n② 确认成绩查询网址是否正确\n③ 选择正确的文件保存路径\n④ 点击运行，当进度达到100%，将出现‘完成’按钮，点击回到开始界面\n⑤ 在右边菜单栏点击表格图标，将查看学生成绩信息\n⑦ 在表格界面点击导出，可以将信息以Excel文件形式导出到之前的保存路径！
            '''
        )
        self.help_text_label.setStyleSheet(
            "font-size: 16pt"
        )
        # 添加组件到布局
        self.ui.load_pages.row_1_layout.addWidget(self.file_path_label)
        self.ui.load_pages.row_1_layout.addWidget(self.file_path_line)
        self.ui.load_pages.row_1_layout.addWidget(self.select_file_btn)
        self.ui.load_pages.row_2_layout.addWidget(self.web_address_label)
        self.ui.load_pages.row_2_layout.addWidget(self.web_address_line)
        # self.ui.load_pages.row_3_layout.addWidget(self.file_save_path_label)
        # self.ui.load_pages.row_3_layout.addWidget(self.file_save_path_line)
        # self.ui.load_pages.row_3_layout.addWidget(self.file_save_path_btn)
        self.ui.load_pages.row_3_layout.addWidget(self.run_btn, alignment=Qt.AlignRight|Qt.AlignTop)
        self.ui.load_pages.table_layout.addWidget(self.table_widget)
        self.ui.load_pages.table_btn_layout.addWidget(self.refresh_btn, alignment=Qt.AlignRight|Qt.AlignTop)
        self.ui.load_pages.table_btn_layout.addWidget(self.save_btn, alignment=Qt.AlignRight|Qt.AlignTop)
        self.ui.load_pages.verticalLayout_2.addWidget(self.help_title_label, alignment=Qt.AlignCenter|Qt.AlignTop, stretch=0)
        self.ui.load_pages.verticalLayout_2.addWidget(self.help_text_label,  alignment=Qt.AlignCenter|Qt.AlignTop, stretch=1)

        # 槽函数所需参数
        caption = '请选择一个文件'
        directory = './'
        file_filter = 'Excel文件(*.xlsx *.xls);;所有文件(*.*)'
        initial_filter = 'Excel文件(*.xls *.xlsx)'

        # 设置槽函数
        self.select_file_btn.clicked.connect(lambda: select_file(self, caption, directory, file_filter, initial_filter))
        self.run_btn.clicked.connect(lambda: run(self))
        self.refresh_btn.clicked.connect(lambda: refresh_table(self))
        self.save_btn.clicked.connect(lambda: save_file(self, caption, directory, file_filter, initial_filter))

        # 测试使用
        # self.file_path_line.setText('D:/Pycharm/Grade_Selenium/gui/student1.xls')
        # self.web_address_line.setText('http://218.26.234.85/views/search.html')

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)