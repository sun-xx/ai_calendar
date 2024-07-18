# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys

class NewWindow(QWidget):
    def __init__(self,txt):
        super().__init__()
        self.setWindowTitle('新窗口')
        self.resize(280, 230)
        label = QLabel(newWin)
        print(txt.day())
        label.setText(str(txt.day()))
        newWin.show()
        self.show()

def draw_txt(txt):
    newWin = NewWindow(txt)
        
class Calendar(QCalendarWidget):
    def paintCell(self, painter, rect, date):
        super(Calendar, self).paintCell(painter, rect, date)
        if date == self.selectedDate():
            painter.save()
            font = QFont()
            font.setPixelSize(11)
            font.setBold(True)
            font.setItalic(True)
            painter.setFont(font)
            painter.drawText(
                rect.topLeft() + QPoint(10, 10),
                "{}".format(self.selectedDate().day()),
            )
            painter.restore()
    def mouseReleaseEvent(self, event):
        #newWin.clear()
        draw_txt(self.selectedDate())

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(100*2, 100*2, int(500*2.2), 400*2-15)
        self.UiComponents()
        self.collec_btn = QPushButton('打开新窗口', self)
        layout = QVBoxLayout()
        layout.addWidget(self.collec_btn)
        self.setLayout(layout)
        self.show()
    def UiComponents(self):
        self.calendar = Calendar(self)
        self.calendar.setCursor(Qt.PointingHandCursor)
        self.calendar.resize(350*3, 3*240)
        self.calendar.setFont(QFont('Times', 15))
        self.calendar.move(10, 10)
 
 
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    #window.collec_btn.clicked.connect(newWin.show)
    sys.exit(app.exec_())
