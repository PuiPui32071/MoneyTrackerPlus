from typing import Type, Final

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QListWidget, QListWidgetItem, \
    QStackedWidget, QScrollArea, QWidget, QLabel, QDateEdit, QComboBox, QLineEdit, QPushButton \
    
from PyQt5.QtCore import QDate

from .chart_view import ChartView
from .money_tracker_widget import MoneyTrackerWidget
from .settings_view import SettingsView
from .transaction_edit_view import TransactionEditView
from .transaction_list_view import TransactionListView


class MoneyTrackerPlusView(QWidget):

    items: Final[list[Type[MoneyTrackerWidget]]] = [TransactionEditView, TransactionListView, ChartView, SettingsView]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("記帳+")
        self.setStyleSheet(self.get_stylesheet())

        # 创建分类列表
        self.category_list = QListWidget()
        self.category_list.setFixedWidth(200)  # 设置固定宽度
        for it in self.items:
            self.add_category_item(it.getName(), it.getIconPath())
        self.category_list.setCurrentRow(0)  # 默认选择第一个项
        self.category_list.currentRowChanged.connect(self.display_content)

        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.category_list)
        scroll_area.setFixedWidth(200)  # 确保滚动区域宽度一致

        # 创建右侧的内容区域
        self.content_stack = QStackedWidget()
        self.content_stack.addWidget(self.initAddData())
        self.content_stack.addWidget(self.initSearchData())
        self.content_stack.addWidget(self.initPlotAnalysis())
        self.content_stack.addWidget(self.initAccountBookSettings())
            

        # 设置主布局
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(scroll_area)  # 添加到布局中
        self.layout.addWidget(self.content_stack)
        

    @classmethod
    def get_stylesheet(cls):
        return """
        QDialog {
            background-color: white;
        }
        QDialog * {
            font-family: "Microsoft JhengHei";
            font-size: 12pt;
        }
        QListWidget {
            border: none;
            outline: 0;
            border: 1px solid #C9C9C9;
        }
        QScrollArea {
            border: none;
        }
        QListWidget::item {
            padding: 10px;
            border-radius: 10px;
        }
        QListWidget::item:hover {
            background-color: #f0f0f0;
        }
        QListWidget::item:selected {
            background-color: #E8F0FE;
            color: #2871D5;
        }
        QLineEdit[readOnly="true"], QLineEdit:disabled {
            border: 1px solid #dcdcdc;
            background-color: #f5f5f5;
        }
        QLineEdit, QTextEdit {
            border: 1px solid #6F747A;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton {
            border-radius: 5px;
            padding: 6px 12px;
        }
        QPushButton#applyButton {
            border: none;
            background-color: #4A90E2;
            color: white;
        }
        QPushButton#applyButton:hover {
            background-color: #1767C3;
        }
        QPushButton#cancelButton {
            border: none;
            background-color: #E0E0E0;
            color: #333333;
        }
        QPushButton#cancelButton:hover {
            background-color: #C9C9C9;
        }
        """

    def add_category_item(self, text, icon_path):
        """向分类列表中添加带有图标的项目"""
        item = QListWidgetItem(QIcon(icon_path), text)
        self.category_list.addItem(item)

    def display_content(self, index):
        self.content_stack.setCurrentIndex(index)
    
    def initAddData(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)

        # 1. 選擇日期
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("選擇日期："))
        date_layout.addStretch()  # 添加空間，將輸入框推到右側
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())  # 預設為當前日期
        date_layout.addWidget(self.date_edit)
        layout.addLayout(date_layout)

        # 2. 選擇收入或支出
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("選擇收入或支出："))
        type_layout.addStretch()
        self.type_combo = QComboBox()
        self.type_combo.addItems(["支出", "收入"])
        type_layout.addWidget(self.type_combo)
        layout.addLayout(type_layout)

        # 3. 輸入金額
        amount_layout = QHBoxLayout()
        amount_layout.addWidget(QLabel("輸入金額："))
        amount_layout.addStretch()
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("請輸入金額")  # 輸入提示
        amount_layout.addWidget(self.amount_input)
        layout.addLayout(amount_layout)

        # 4. 確定新增按鈕
        button_layout = QHBoxLayout()
        button_layout.addWidget(QLabel(""))
        button_layout.addStretch()
        self.submit_button = QPushButton("確定新增")
        self.submit_button.setObjectName("applyButton")
        button_layout.addWidget(self.submit_button)
        # self.submit_button.clicked.connect(self.submit_data)  # 綁定事件
        layout.addLayout(button_layout)
        
        return widget
    
    def initSearchData(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)

        # 1. 選擇日期
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("選擇日期："))
        date_layout.addStretch()  # 添加空間，將輸入框推到右側
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())  # 預設為當前日期
        date_layout.addWidget(self.date_edit)
        layout.addLayout(date_layout)

        # 4. 確定新增按鈕
        button_layout = QHBoxLayout()
        button_layout.addWidget(QLabel(""))
        button_layout.addStretch()
        self.submit_button = QPushButton("確定")
        self.submit_button.setObjectName("applyButton")
        button_layout.addWidget(self.submit_button)
        # self.submit_button.clicked.connect(self.submit_data)  # 綁定事件
        layout.addLayout(button_layout)
        
        return widget
    
    def initPlotAnalysis(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)

        # 1. 選擇起始日期
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("選擇起始日期："))
        date_layout.addStretch()  # 添加空間，將輸入框推到右側
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())  # 預設為當前日期
        date_layout.addWidget(self.date_edit)
        layout.addLayout(date_layout)

        # 2. 選擇結束日期
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("選擇結束日期："))
        date_layout.addStretch()  # 添加空間，將輸入框推到右側
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())  # 預設為當前日期
        date_layout.addWidget(self.date_edit)
        layout.addLayout(date_layout)

        # 4. 確定新增按鈕
        button_layout = QHBoxLayout()
        button_layout.addWidget(QLabel(""))
        button_layout.addStretch()
        self.submit_button = QPushButton("確定")
        self.submit_button.setObjectName("applyButton")
        button_layout.addWidget(self.submit_button)
        # self.submit_button.clicked.connect(self.submit_data)  # 綁定事件
        layout.addLayout(button_layout)
        
        return widget
    
    def initAccountBookSettings(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)

        # 2. 選擇當前帳本
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("選擇當前帳本："))
        type_layout.addStretch()
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Book1", "Book2", "Book3"])
        account_select_button = QPushButton("確定")
        account_select_button.setObjectName("applyButton")
        type_layout.addWidget(self.type_combo)
        type_layout.addWidget(account_select_button)
        layout.addLayout(type_layout)

        # 3. 新增帳本
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("新增帳本："))
        name_layout.addStretch()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("請輸入帳本名稱")  # 輸入提示
        account_add_button = QPushButton("確定")
        account_add_button.setObjectName("applyButton")
        name_layout.addWidget(self.name_input)
        name_layout.addWidget(account_add_button)
        layout.addLayout(name_layout)

        
        return widget
