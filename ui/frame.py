import sys
import PyQt5
import PyQt5.QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

class CalendarDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('对话框')
        self.setGeometry(100, 100, 200, 100)

        layout = QHBoxLayout()
        button = QPushButton('点击我', self)
        layout.addWidget(button)
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 960, 720)
        self.setWindowTitle('AI Calendar')  

        font = PyQt5.QtGui.QFont()
        font.setFamily('幼圆')
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        self.calendar_button = QPushButton('日历', self)
        self.dialog_button = QPushButton('对话', self)
        self.calendar_button.setFont(font)
        self.dialog_button.setFont(font)
        self.calendar_button.setFlat(True)
        self.dialog_button.setFlat(True)
        #self.calendar_button.setStyleSheet("background-color: #008CBA; color: black; border-radius: 1px;")
        #self.dialog_button.setStyleSheet("background-color: #008CBA; color: black; border-radius: 1px;")
        self.calendar_button.clicked.connect(self.show_calendar)
        self.dialog_button.clicked.connect(self.show_dialog)
        left_layout.addWidget(self.calendar_button)
        left_layout.addWidget(self.dialog_button)

        self.calendar = QCalendarWidget(self)

        self.right_layout = QHBoxLayout()
        self.right_layout.addWidget(self.calendar)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(self.right_layout)

        self.setLayout(main_layout)

    def show_calendar(self):
        for i in reversed(range(self.right_layout.count())): 
            self.right_layout.itemAt(i).layout().setParent(None)

        self.calendar = QCalendarWidget(self)
        self.right_layout.addWidget(self.calendar)

    def show_dialog(self):
        for i in reversed(range(self.right_layout.count())): 
            self.right_layout.itemAt(i).widget().setParent(None)

        inner_layout = QVBoxLayout()
        self.right_layout.addLayout(inner_layout)

        title_font = PyQt5.QtGui.QFont()
        title_font.setFamily('幼圆')
        title_font.setPointSize(25)
        title_font.setBold(True)
        title_font.setWeight(70)

        title_label = QLabel(self)
        title_label.setText('向日历说话吧')
        title_label.setFont(title_font)
        
        bt_font = PyQt5.QtGui.QFont()
        bt_font.setFamily('微软雅黑')
        bt_font.setPointSize(12)
        bt_font.setBold(True)
        bt_font.setWeight(15)

        image_button = QPushButton(self)
        image_button.setText('选取日程图片')
        image_button.setFont(bt_font)
        image_button.clicked.connect(self.get_image)

        self.lineedit = QLineEdit()
        self.lineedit.setFixedHeight(80)
        self.lineedit.setFixedWidth(800)
        l_font = PyQt5.QtGui.QFont()
        l_font.setFamily('微软雅黑')
        l_font.setPointSize(13)
        self.lineedit.setFont(l_font)
        self.lineedit.setStyleSheet("background:transparent; border-width: 0;")
        self.lineedit.returnPressed.connect(self.send_text)

        inner_layout.addStretch(1)
        inner_layout.addWidget(title_label)
        inner_layout.addStretch(2)
        inner_layout.addWidget(image_button)
        inner_layout.addStretch(3)
        inner_layout.addWidget(self.lineedit)
        self.right_layout.addLayout(inner_layout)

    def get_image(self):
        image_file = QFileDialog.getOpenFileName(self, 'Open file', 'C:/', 'Image files (*.jpg *.png *.jpeg)')

    def send_text(self):
        print(self.lineedit.text())
        self.lineedit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
