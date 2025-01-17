from PySide6.QtWidgets import QMainWindow, QApplication

from components.change_mode import ChangeMode
from components.mainWindow.ui_mainWindow import Ui_MainWindow
from components.menubar import Menubar
from components.page_size import PageSize
from components.turn_page import TurnPageLeft, TurnPageRight
from components.viewer_double_page import ViewerDoublePage
from components.viewer_horizontal_scroll import ViewerHorizontalScroll
from components.viewer_single_page import ViewerSinglePage
from components.viewer_vertical_scroll import ViewerVerticalScroll


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.setMinimumSize(300, 400)

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
        """添加预览控件"""
        # 预览控件-单页
        self.viewer_single_page = ViewerSinglePage(self)
        self.viewer_single_page.set_comic('测试序号图')
        self.ui.page_single.layout().addWidget(self.viewer_single_page)
        # 预览控件-双页
        self.viewer_double_page = ViewerDoublePage(self)
        self.ui.page_double_left.layout().addWidget(self.viewer_double_page)
        # 预览控件-横向卷轴
        self.viewer_horizontal_scroll = ViewerHorizontalScroll(self)
        self.ui.page_horizontal_scroll_left.layout().addWidget(self.viewer_horizontal_scroll)
        # 预览控件-纵向卷轴
        self.viewer_vertical_scroll = ViewerVerticalScroll(self)
        self.ui.page_vertical_scroll.layout().addWidget(self.viewer_vertical_scroll)

        # 绑定信号
        self.bind_signal()

    def bind_signal(self):
        """绑定信号"""
        # 切换模式控件
        self.widget_change_mode.SinglePage.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.widget_change_mode.DoublePage.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.widget_change_mode.VerticalScroll.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.widget_change_mode.HorizontalScroll.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        # 页面大小控件
        self.widget_page_size.FitHeight.connect(self._get_current_viewer().fit_height)
        self.widget_page_size.FitWidth.connect(self._get_current_viewer().fit_width)
        self.widget_page_size.FitWidget.connect(self._get_current_viewer().fit_widget)
        self.widget_page_size.FullSize.connect(self._get_current_viewer().full_size)
        self.widget_page_size.RotateLeft.connect(self._get_current_viewer().rotate_left)
        self.widget_page_size.RotateRight.connect(self._get_current_viewer().rotate_right)
        self.widget_page_size.ZoomIn.connect(self._get_current_viewer().zoom_in)
        self.widget_page_size.ZoomOut.connect(self._get_current_viewer().zoom_out)
        # 左翻页控件
        self.widget_turn_page_left.TurnPage.connect(self._get_current_viewer().previous_page)
        # self.widget_turn_page_left.TurnPageRC.connect()
        # 右翻页控件
        self.widget_turn_page_right.TurnPage.connect(self._get_current_viewer().next_page)
        # self.widget_turn_page_right.TurnPageRC.connect()
        # 选项栏
        # self.widget_menubar.Option.connect()
        self.widget_menubar.PreviousPage.connect(self._get_current_viewer().previous_page)
        # self.widget_menubar.PreviousRC.connect()
        self.widget_menubar.AutoPlayStart.connect(self._get_current_viewer().autoplay_start)
        self.widget_menubar.AutoPlayStop.connect(self._get_current_viewer().autoplay_stop)
        self.widget_menubar.NextPage.connect(self._get_current_viewer().next_page)
        # self.widget_menubar.NextRC.connect()
        # self.widget_menubar.Playlist.connect()

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
        new_y = p_rect.height() - self.widget_menubar.height() - 50
        self.widget_menubar.move(new_x, new_y)

    def _get_current_viewer(self):
        tab = self.ui.stackedWidget.currentWidget()
        if tab:
            layout = tab.layout()
            viewer: ViewerSinglePage = layout.itemAt(0).widget()
            return viewer

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_hover_position()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            paths = []
            for index in range(len(urls)):
                path = urls[index].toLocalFile()
                paths.append(path)
            self._get_current_viewer().set_comic(paths[0])


if __name__ == '__main__':
    app = QApplication()
    ui = MainWindow()
    ui.show()
    app.exec()
