import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, QLinearGradient
from PySide6.QtCore import Qt, QPointF

class DrawingWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Эллипс
        pen_ellipse = QPen(QColor("black"))
        brush_ellipse = QBrush(QColor("lightblue"))
        painter.setPen(pen_ellipse)
        painter.setBrush(brush_ellipse)
        painter.drawEllipse(10, 120, 100, 50)
        
        # Квадрат
        pen_square = QPen(QColor("black"))
        brush_square = QBrush(QColor("lightgreen"))
        painter.setPen(pen_square)
        painter.setBrush(brush_square)
        painter.drawRect(135, 120, 80, 80)
        
        # Треугольник
        pen_triangle = QPen(QColor("black"))
        gr = QLinearGradient(100, 100, 200, 200)
        gr.setColorAt(0.0, QColor("cyan"))
        gr.setColorAt(1.0, QColor("magenta"))
        brush_gradient = QBrush(gr)
        painter.setPen(pen_triangle)
        painter.setBrush(brush_gradient)
        triangle = [QPointF(135, 100), QPointF(215, 100), QPointF(175, 30)]
        painter.drawPolygon(triangle)
     
        
def main():
    app = QApplication(sys.argv)
    
    window = QWidget()
    layout = QVBoxLayout()
    
    drawing_widget = DrawingWidget()
    
    layout.addWidget(drawing_widget)
    window.setLayout(layout)
    
    window.setWindowTitle("Shapes Drawing")
    window.setGeometry(100, 100, 300, 300)
    window.show()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()
