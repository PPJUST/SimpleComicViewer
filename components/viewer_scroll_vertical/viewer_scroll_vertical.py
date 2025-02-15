from PySide6.QtWidgets import QApplication

from components.viewer_scroll_frame import ViewerScrollFrame


class ViewerScrollVertical(ViewerScrollFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent, layout='vertical')


if __name__ == '__main__':
    app = QApplication()
    ui = ViewerScrollVertical()
    ui.show()
    app.exec()
