from PySide6.QtWidgets import QMainWindow, QApplication

from components.change_mode import ChangeMode
from components.mainWindow.ui_mainWindow import Ui_MainWindow
from components.menubar import Menubar
from components.page_size import PageSize
from components.turn_page import TurnPageLeft, TurnPageRight


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.setMinimumSize(300,400)

        """添加悬浮控件"""
        # 切换模式控件
        self.widget_change_mode = ChangeMode(self)
        self.widget_change_mode.show()
        # 页面大小控件
        self.widget_page_size = PageSize(self)
        self.widget_page_size.show()
        # 左翻页控件
        self.widget_turn_page_left = TurnPageLeft(self)
        self.widget_turn_page_left.show()
        # 右翻页控件
        self.widget_turn_page_right = TurnPageRight(self)
        self.widget_turn_page_right.show()
        # 选项栏
        self.widget_menubar = Menubar(self)
        self.widget_menubar.show()

    def bind_signal(self):
        """绑定信号"""
        # 切换模式控件
        self.widget_change_mode.SinglePage.connect()
        self.widget_change_mode.DoublePage.connect()
        self.widget_change_mode.VerticalScroll.connect()
        self.widget_change_mode.HorizontalScroll.connect()
        # 页面大小控件
        self.widget_page_size.FitHeight.connect()
        self.widget_page_size.FitWidth.connect()
        self.widget_page_size.FitWidget.connect()
        self.widget_page_size.FullSize.connect()
        self.widget_page_size.RotateLeft.connect()
        self.widget_page_size.RotateRight.connect()
        self.widget_page_size.ZoomIn.connect()
        self.widget_page_size.ZoomOut.connect()
        self.widget_page_size.FitHeight.connect()
        self.widget_page_size.FitHeight.connect()
        # 左翻页控件
        self.widget_turn_page_left.TurnPage.connect()
        self.widget_turn_page_left.TurnPageRC.connect()
        # 右翻页控件
        self.widget_turn_page_right.TurnPage.connect()
        self.widget_turn_page_right.TurnPageRC.connect()
        # 选项栏
        self.widget_menubar.Option.connect()
        self.widget_menubar.PreviousPage.connect()
        self.widget_menubar.PreviousRC.connect()
        self.widget_menubar.AutoPlay.connect()
        self.widget_menubar.NextPage.connect()
        self.widget_menubar.NextRC.connect()
        self.widget_menubar.Playlist.connect()
    def _update_hover_position(self):
        """修改大小后，更新悬浮控件的位置"""
        p_rect = self.geometry()  # 框架
        # 切换模式控件
        new_x = 0
        new_y = 0
        self.widget_change_mode.move(new_x, new_y)
        # 页面大小控件
        new_x = p_rect.width() - self.widget_page_size.width()
        new_y = 0
        self.widget_page_size.move(new_x, new_y)
        # 左翻页控件
        new_x = 0
        new_y = (p_rect.height() - self.widget_turn_page_left.height()) // 2
        self.widget_turn_page_left.move(new_x, new_y)
        # 右翻页控件
        new_x = p_rect.width() - self.widget_turn_page_right.width()
        new_y = (p_rect.height() - self.widget_turn_page_right.height()) // 2
        self.widget_turn_page_right.move(new_x, new_y)
        # 选项栏
        new_x = (p_rect.width() - self.widget_menubar.width()) // 2
        new_y = p_rect.height() - self.widget_menubar.height()
        self.widget_menubar.move(new_x, new_y)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_hover_position()


if __name__ == '__main__':
    app = QApplication()
    ui = MainWindow()
    ui.show()
    app.exec()
