import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MovingWidget(QWidget):
    def __init__(self, parent=None):
        super(MovingWidget, self).__init__(parent)
        self.resize(100, 100)
        
        self.color = Qt.green if isinstance(self, GreenSquare) else Qt.blue
        


class GreenSquare(MovingWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.green)

    def animate(self):
        self.animation = QPropertyAnimation(self, b"pos", self)
        self.animation.setDuration(5000)
        self.animation.setStartValue(QPoint(0, 0))
        self.animation.setKeyValues([(0.25, QPoint(10, 50)), (0.5, QPoint(50, 10)), (0.75, QPoint(150, 100)) ])
        self.animation.setEndValue(QPoint(200, 250))
        # self.animation.setPath(path)
        self.animation.setLoopCount(-1)  # -1 для бесконечного повторения анимации
        self.animation.start()

class BlueCircle(MovingWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.blue))
        painter.drawEllipse(self.rect())

    def animate(self):
        self.animation = QPropertyAnimation(self, b"pos", self)
        self.animation.setDuration(2500)
        self.animation.setStartValue(QPoint(0, 0))
        self.animation.setEndValue(QPoint(300, 50))
        # self.animation.setPath(path)
        self.animation.setLoopCount(-1)  # -1 для бесконечного повторения анимации
        self.animation.start()

def main():
    app = QApplication(sys.argv)
    
    window = QWidget()
    layout = QVBoxLayout()
    
    green_square = GreenSquare(window)
    green_square.setFixedSize(50, 50)
    blue_circle = BlueCircle(window)
    blue_circle.setFixedSize(50, 50)
    
    green_path = QPainterPath()
    green_path.moveTo(10, 10)
    green_path.lineTo(200, 200)
    
    blue_path = QPainterPath()
    blue_path.moveTo(10, 10)
    blue_path.lineTo(200, 10)
    
    green_square.animate()
    blue_circle.animate()
    
    layout.addWidget(green_square)
    layout.addWidget(blue_circle)
    
    window.setLayout(layout)
    
    window.setWindowTitle("Animated Widgets")
    window.setGeometry(100, 100, 300, 300)
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
