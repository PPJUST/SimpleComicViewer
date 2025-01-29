from PySide6.QtWidgets import QMainWindow, QApplication

from common.comic_info import ComicInfo
from common.image_info import ImageInfo
from common.mode_viewer import ModeViewer
from components.hover_image_info import HoverImageInfo
from components.mainWindow.ui_mainWindow import Ui_MainWindow
from components.menubar import Menubar
from components.page_size import PageSize
from components.turn_page import TurnPageLeft, TurnPageRight
from components.viewer_double_page import ViewerDoublePage
from components.viewer_horizontal_scroll import ViewerHorizontalScroll
from components.viewer_mode import ViewerMode
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
        self.widget_change_mode = ViewerMode(self)
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
        # 悬浮的漫画和图片信息
        self.hover_image_info = HoverImageInfo(self)
        self.hover_image_info.show()
        """添加预览控件"""
        # 预览控件-单页
        self.viewer_single_page = ViewerSinglePage(self)
        self.ui.page_single.layout().addWidget(self.viewer_single_page)
        self.viewer_single_page.imageInfoShowed.connect(self._show_image_info)
        # 预览控件-双页
        self.viewer_double_page = ViewerDoublePage(self)
        self.ui.page_double_left.layout().addWidget(self.viewer_double_page)
        self.viewer_double_page.imageInfoShowed.connect(self._show_image_info)
        # 预览控件-横向卷轴
        self.viewer_horizontal_scroll = ViewerHorizontalScroll(self)
        self.ui.page_horizontal_scroll_left.layout().addWidget(self.viewer_horizontal_scroll)
        # 预览控件-纵向卷轴
        self.viewer_vertical_scroll = ViewerVerticalScroll(self)
        self.ui.page_vertical_scroll.layout().addWidget(self.viewer_vertical_scroll)
        self.viewer_vertical_scroll.imageInfoShowed.connect(self._show_image_info)
        # 绑定信号
        self.bind_signal()

        # 设置参数
        self.comics = []  # 漫画列表
        self.comic_showed: ComicInfo = None  # 当前显示的漫画的漫画信息类

    def drop_paths(self, paths: list):
        """拖入文件"""
        # 备忘录 先检查路径中的符合条件的漫画文件
        comics = paths
        self.comics = comics
        # 提取漫画信息类
        self.comic_showed = ComicInfo(paths[0])
        # 显示
        self.show_comic(self.comic_showed)

    def show_comic(self, comic_info: ComicInfo):
        self.hover_image_info.set_comic(comic_info)
        self._get_current_viewer().set_comic(comic_info)

    def bind_signal(self):
        """绑定信号"""
        # 切换模式控件
        self.widget_change_mode.SinglePage.connect(self._change_viewer)
        self.widget_change_mode.DoublePage.connect(self._change_viewer)
        self.widget_change_mode.VerticalScroll.connect(self._change_viewer)
        self.widget_change_mode.HorizontalScroll.connect(self._change_viewer)
        # 页面大小控件
        self.widget_page_size.FitHeight.connect(self._viewer_fit_height)
        self.widget_page_size.FitWidth.connect(self._viewer_fit_width)
        self.widget_page_size.FitWidget.connect(self._viewer_fit_widget)
        self.widget_page_size.FullSize.connect(self._viewer_full_size)
        self.widget_page_size.RotateLeft.connect(self._viewer_rotate_left)
        self.widget_page_size.RotateRight.connect(self._viewer_rotate_right)
        self.widget_page_size.ZoomIn.connect(self._viewer_zoom_in)
        self.widget_page_size.ZoomOut.connect(self._viewer_zoom_out)
        # 左翻页控件
        self.widget_turn_page_left.TurnPage.connect(self._viewer_previous_page)
        # self.widget_turn_page_left.TurnPageRC.connect()
        # 右翻页控件
        self.widget_turn_page_right.TurnPage.connect(self._viewer_next_page)
        # self.widget_turn_page_right.TurnPageRC.connect()
        # 选项栏
        # self.widget_menubar.Option.connect()
        self.widget_menubar.PreviousPage.connect(self._viewer_previous_page)
        # self.widget_menubar.PreviousRC.connect()
        self.widget_menubar.AutoPlayStart.connect(self._viewer_start_autoplay)
        self.widget_menubar.AutoPlayStop.connect(self._viewer_stop_autoplay)
        self.widget_menubar.NextPage.connect(self._viewer_next_page)
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
        # 悬浮的漫画和图片信息
        new_x = 0
        new_y = self.widget_change_mode.height()
        self.hover_image_info.move(new_x, new_y)

    def _get_current_viewer(self):
        """获取当前视图模式对应的控件"""
        tab = self.ui.stackedWidget.currentWidget()
        if tab:
            layout = tab.layout()
            viewer: ViewerSinglePage = layout.itemAt(0).widget()
            return viewer

    def _change_viewer(self, viewer_mode: ModeViewer):
        """修改显示模式"""
        # 设置页面尺寸选项
        self.widget_page_size.set_button_mode(viewer_mode)
        # 清除旧的预览控件显示的图像
        self._get_current_viewer().clear()
        # 将当前显示的漫画集成至新的预览控件中
        if self.comic_showed:
            self.show_comic(self.comic_showed)
        # 切换到对应页
        if viewer_mode is ModeViewer.SinglePage:
            self.ui.stackedWidget.setCurrentIndex(0)
        elif viewer_mode is ModeViewer.DoublePage.Left:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif viewer_mode is ModeViewer.DoublePage.Right:
            self.ui.stackedWidget.setCurrentIndex(2)
        elif viewer_mode is ModeViewer.Scroll.Vertical:
            self.ui.stackedWidget.setCurrentIndex(3)
        elif viewer_mode is ModeViewer.Scroll.Horizontal.Left:
            self.ui.stackedWidget.setCurrentIndex(4)
        elif viewer_mode is ModeViewer.Scroll.Horizontal.Right:
            self.ui.stackedWidget.setCurrentIndex(5)

    def _viewer_fit_height(self):
        """设置预览控件-图片尺寸，适合高度"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.fit_height()

    def _viewer_fit_width(self):
        """设置预览控件-图片尺寸，适合宽度"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.fit_width()

    def _viewer_fit_widget(self):
        """设置预览控件-图片尺寸，适合页面"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.fit_widget()

    def _viewer_full_size(self):
        """设置预览控件-图片尺寸，实际大小"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.full_size()

    def _viewer_rotate_left(self):
        """设置预览控件-向左旋转图片"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.rotate_left()

    def _viewer_rotate_right(self):
        """设置预览控件-向右旋转图片"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.rotate_right()

    def _viewer_zoom_in(self):
        """设置预览控件-放大图片"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.zoom_in()

    def _viewer_zoom_out(self):
        """设置预览控件-缩小图片"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.zoom_out()

    def _viewer_previous_page(self):
        """设置预览控件-上一页"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.previous_page()

    def _viewer_next_page(self):
        """设置预览控件-下一页"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.next_page()

    def _viewer_start_autoplay(self):
        """设置预览控件-开始自动播放"""
        viewer = self._get_current_viewer()
        viewer.autoplay_start()

    def change_autoplay_state(self):
        """修改自动播放状态，（开启时关闭，关闭时开启）"""
        viewer = self._get_current_viewer()
        is_running = viewer.is_autoplay_running()
        if is_running:
            self._viewer_stop_autoplay()
        else:
            self._viewer_start_autoplay()

    def _viewer_set_autoplay_speed(self, add_speed: float):
        """设置预览控件-设置自动播放的速度
        :param add_speed: 两位小数，变动的自动播放速度"""
        viewer = self._get_current_viewer()
        viewer.set_autoplay_speed(add_speed)

    def _viewer_reset_autoplay_speed(self):
        """设置预览控件-重置自动播放的速度"""
        viewer = self._get_current_viewer()
        viewer.reset_autoplay_speed()

    def _viewer_stop_autoplay(self):
        """设置预览控件-停止自动播放"""
        viewer = self._get_current_viewer()
        viewer.autoplay_stop()

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
    ui = MainWindow()
    ui.show()
    app.exec()
