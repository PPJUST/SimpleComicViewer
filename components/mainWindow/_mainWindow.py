import lzytools._qt_pyside6
from PySide6.QtWidgets import QMainWindow, QApplication

from common import common_comic
from common.comic_info import ComicInfo
from common.image_info import ImageInfo
from components.hover_image_info import HoverImageInfo
from components.hover_tips.hover_tips import HoverTips
from components.mainWindow.icon_base64 import _APP
from components.mainWindow.ui_mainWindow import Ui_MainWindow
from components.menubar import Menubar
from components.page_size import PageSize
from components.turn_page import TurnPageLeft, TurnPageRight
from components.viewer_double_page import ViewerDoublePage
from components.viewer_mode import ViewerMode
from components.viewer_scroll_horizontal import ViewerScrollHorizontal
from components.viewer_scroll_vertical import ViewerScrollVertical
from components.viewer_single_page import ViewerSinglePage


class _MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.setMinimumSize(300, 400)
        self.setWindowIcon(lzytools._qt_pyside6.base64_to_pixmap(_APP))

        # 设置参数
        self.comics = []  # 漫画列表
        self.comic_showed: ComicInfo = None  # 当前显示的漫画的漫画信息类

        """添加悬浮控件"""
        # 切换模式控件
        self.widget_change_mode = ViewerMode(self)
        self.widget_change_mode.show()
        # 页面尺寸控件
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
        # 悬浮的漫画和图片信息
        self.hover_image_info = HoverImageInfo(self)
        self.hover_image_info.show()
        # 悬浮的操作信息提示
        self.hover_tips = HoverTips(self)
        self.hover_image_info.show()

        """添加预览控件"""
        # 预览控件-单页
        self.viewer_single_page = ViewerSinglePage(self)
        self.ui.page_single.layout().addWidget(self.viewer_single_page)
        # 预览控件-双页
        self.viewer_double_page = ViewerDoublePage(self)
        self.ui.page_double_left.layout().addWidget(self.viewer_double_page)
        # 预览控件-横向卷轴
        self.viewer_horizontal_scroll = ViewerScrollHorizontal(self)
        self.ui.page_horizontal_scroll_left.layout().addWidget(self.viewer_horizontal_scroll)
        # 预览控件-纵向卷轴
        self.viewer_vertical_scroll = ViewerScrollVertical(self)
        self.ui.page_vertical_scroll.layout().addWidget(self.viewer_vertical_scroll)

    def drop_paths(self, paths: list):
        """拖入文件"""
        # 检查路径中的符合条件的漫画文件
        self.comics = [i for i in paths if common_comic.is_comic(i)]
        if self.comics:
            # 如果正在执行自动播放，则终止
            self._viewer_stop_autoplay()
            # 提取漫画信息类
            self.comic_showed = ComicInfo(paths[0])
            # 显示
            self.show_comic(self.comic_showed)
            HoverTips().show_tips('更新显示的漫画')
        else:
            HoverTips().show_tips('未识别到漫画')

    def show_comic(self, comic_info: ComicInfo):
        self.hover_image_info.set_comic(comic_info)
        self._get_current_viewer().set_comic(comic_info)

    def _update_hover_position(self):
        """修改尺寸后，更新悬浮控件的位置"""
        p_rect = self.geometry()  # 框架
        # 切换模式控件
        new_x = 0
        new_y = 0
        self.widget_change_mode.move(new_x, new_y)
        # 页面尺寸控件
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
        # 悬浮的漫画和图片信息
        new_x = 0
        new_y = self.widget_change_mode.height()
        self.hover_image_info.move(new_x, new_y)
        # 悬浮的操作信息提示
        new_x = 0
        new_y = p_rect.height() - self.hover_tips.height()
        self.hover_tips.move(new_x, new_y)

    def _get_current_viewer(self):
        """获取当前视图模式对应的控件"""
        tab = self.ui.stackedWidget.currentWidget()
        if tab:
            layout = tab.layout()
            viewer: ViewerSinglePage = layout.itemAt(0).widget()
            return viewer

    def _viewer_stop_autoplay(self):
        """设置预览控件-停止自动播放"""
        viewer = self._get_current_viewer()
        is_autoplay = viewer.is_autoplay_running()
        if is_autoplay:
            viewer.stop_autoplay()
            self._set_menubar_stop_autoplay()
            HoverTips().show_tips('停止自动播放')

    def _set_menubar_start_autoplay(self):
        """设置控制栏的自动播放开始状态"""
        self.widget_menubar.set_autoplay_state_start()

    def _set_menubar_stop_autoplay(self):
        """设置控制栏的自动播放停止状态"""
        self.widget_menubar.set_autoplay_state_stop()

    def _show_image_info(self, image_info: ImageInfo):
        """更新漫画和图片信息"""
        self.hover_image_info.set_image(image_info)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_hover_position()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        self._get_current_viewer()
        urls = event.mimeData().urls()
        if urls:
            paths = []
            for index in range(len(urls)):
                path = urls[index].toLocalFile()
                paths.append(path)
            self.drop_paths(paths)


if __name__ == '__main__':
    app = QApplication()
    ui = _MainWindow()
    ui.show()
    app.exec()
