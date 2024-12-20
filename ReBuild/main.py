from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtWidgets import QApplication


from src.ui.mainWindow import MainWindow

def load_app():
    app = QApplication()
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    app.setPalette(palette)

    ui = MainWindow()
    ui.show()

    app.exec()



if __name__ == "__main__":
    load_app()
