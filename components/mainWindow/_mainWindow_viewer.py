# 分组添加控件
from PySide6.QtWidgets import QApplication

from common.mode_viewer import ModeViewer
from components.hover_tips.hover_tips import HoverTips
from components.mainWindow._mainWindow import _MainWindow


class _MainWindowViewer(_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 绑定信号
        self.bind_signal()

    def bind_signal(self):
        """绑定信号"""
        # 预览控件-单页
        self.viewer_single_page.imageInfoShowed.connect(self._show_image_info)
        self.viewer_single_page.StartAutoPlay.connect(self._set_menubar_start_autoplay)
        self.viewer_single_page.StopAutoPlay.connect(self._set_menubar_stop_autoplay)
        # 预览控件-双页
        self.viewer_double_page.imageInfoShowed.connect(self._show_image_info)
        self.viewer_double_page.StartAutoPlay.connect(self._set_menubar_start_autoplay)
        self.viewer_double_page.StopAutoPlay.connect(self._set_menubar_stop_autoplay)
        # 预览控件-横向卷轴
        self.viewer_horizontal_scroll.imageInfoShowed.connect(self._show_image_info)
        self.viewer_horizontal_scroll.StartAutoPlay.connect(self._set_menubar_start_autoplay)
        self.viewer_horizontal_scroll.StopAutoPlay.connect(self._set_menubar_stop_autoplay)
        # 预览控件-纵向卷轴
        self.viewer_vertical_scroll.imageInfoShowed.connect(self._show_image_info)
        self.viewer_vertical_scroll.StartAutoPlay.connect(self._set_menubar_start_autoplay)
        self.viewer_vertical_scroll.StopAutoPlay.connect(self._set_menubar_stop_autoplay)
        # 切换模式控件
        self.widget_change_mode.SinglePage.connect(self._change_viewer)
        self.widget_change_mode.DoublePage.connect(self._change_viewer)
        self.widget_change_mode.VerticalScroll.connect(self._change_viewer)
        self.widget_change_mode.HorizontalScroll.connect(self._change_viewer)
        # 页面尺寸控件
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
            HoverTips().show_tips('切换显示模式 - 单页模式')
        elif viewer_mode is ModeViewer.DoublePage.Left:
            self.ui.stackedWidget.setCurrentIndex(1)
            HoverTips().show_tips('切换显示模式 - 双页模式（左开本）')
        elif viewer_mode is ModeViewer.DoublePage.Right:
            self.ui.stackedWidget.setCurrentIndex(2)
            HoverTips().show_tips('切换显示模式 - 双页模式（右开本）')
        elif viewer_mode is ModeViewer.Scroll.Vertical:
            self.ui.stackedWidget.setCurrentIndex(3)
            HoverTips().show_tips('切换显示模式 -纵向卷轴模式')
        elif viewer_mode is ModeViewer.Scroll.Horizontal.Left:
            self.ui.stackedWidget.setCurrentIndex(4)
            HoverTips().show_tips('切换显示模式 -横向卷轴模式（左开本）')
        elif viewer_mode is ModeViewer.Scroll.Horizontal.Right:
            self.ui.stackedWidget.setCurrentIndex(5)
            HoverTips().show_tips('切换显示模式 -横向卷轴模式（右开本）')

    def _viewer_fit_height(self):
        """设置预览控件-图片尺寸，适合高度"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.update_size_fit_height()
        HoverTips().show_tips('设置图片模式 - 适合高度')

    def _viewer_fit_width(self):
        """设置预览控件-图片尺寸，适合宽度"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.update_size_fit_width()
        HoverTips().show_tips('设置图片模式 - 适合高度')

    def _viewer_fit_widget(self):
        """设置预览控件-图片尺寸，适合页面"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.update_size_fit_widget()
        HoverTips().show_tips('设置图片模式 - 适合页面')

    def _viewer_full_size(self):
        """设置预览控件-图片尺寸，实际尺寸"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.update_size_full_size()
        HoverTips().show_tips('设置图片模式 - 实际尺寸')

    def _viewer_rotate_left(self):
        """设置预览控件-向左旋转图片"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.rotate_left()
        HoverTips().show_tips('向左旋转当前图片')

    def _viewer_rotate_right(self):
        """设置预览控件-向右旋转图片"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.rotate_right()
        HoverTips().show_tips('向右旋转当前图片')

    def _viewer_zoom_in(self):
        """设置预览控件-放大图片"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.zoom_in()
        HoverTips().show_tips('放大图片')

    def _viewer_zoom_out(self):
        """设置预览控件-缩小图片"""
        self._viewer_stop_autoplay()
        viewer = self._get_current_viewer()
        viewer.zoom_out()
        HoverTips().show_tips('缩小图片')

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
        viewer.start_autoplay()
        HoverTips().show_tips('开始自动播放')

    def _viewer_change_autoplay_state(self):
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
        speed = viewer.set_autoplay_speed(add_speed)
        HoverTips().show_tips(f'设置自动播放速度 当前：{speed}')

    def _viewer_reset_autoplay_speed(self):
        """设置预览控件-重置自动播放的速度"""
        viewer = self._get_current_viewer()
        speed = viewer.reset_autoplay_speed()
        HoverTips().show_tips(f'设置自动播放速度 当前：{speed}')


if __name__ == '__main__':
    app = QApplication()
    ui = _MainWindowViewer()
    ui.show()
    app.exec()
