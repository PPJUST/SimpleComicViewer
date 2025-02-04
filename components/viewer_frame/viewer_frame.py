import lzytools._qt_pyside6
from PySide6.QtCore import QTimer, Signal
from PySide6.QtWidgets import QScrollArea, QWidget, QHBoxLayout, QVBoxLayout

from common.comic_info import ComicInfo
from common.mode_image_size import ModeImageSize

_MIN_SPEED = 0.1  # 限制的最慢自动播放速度
_MAX_SPEED = 5.0  # 限制的最快自动播放速度


class ViewerFrame(QScrollArea):
    """预览控件框架"""
    StopAutoPlay = Signal(name='在自动播放运行时，进行手动翻页则停止自动播放')
    StartAutoPlay = Signal(name='自动播放开始信号')

    def __init__(self, parent=None, layout='horizontal'):
        super().__init__(parent)
        self.setWidgetResizable(True)  # 使内容区域自适应尺寸
        # 设置外部框架控件
        self.content_widget = QWidget()
        if layout.lower() == 'horizontal':
            self.layout = QHBoxLayout()
        elif layout.lower() == 'vertical':
            self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.content_widget.setLayout(self.layout)
        self.setWidget(self.content_widget)
        # 设置透明背景
        lzytools._qt_pyside6.set_transparent_background(self)
        lzytools._qt_pyside6.set_transparent_background(self.content_widget)

        # 设置自动播放计时器
        self.timer_autoplay = QTimer()  # 自动播放的计时器
        self.speed_autoplay: float = 1.0  # 自动播放的速度 n秒/页
        self.timer_autoplay.timeout.connect(self._next_page_autoplay)
        self.timer_autoplay.setInterval(int(self.speed_autoplay * 1000))

        # 设置参数
        self.comic_info: ComicInfo = None  # 当前显示的漫画类
        self.page_index = 0  # 当前显示的页码（从1开始）
        self.page_size_mode = ModeImageSize.Fixed  # 当前的显示模式，默认为固定尺寸

    def set_comic(self, comic_info: ComicInfo):
        """设置漫画类
        :param comic_info: ComicInfo类"""
        # 备忘录 防止报错，先检查路径对应文件是否为漫画
        self.comic_info = comic_info
        self.page_index = 1

    def show_image(self):
        """显示图片"""

    def previous_page(self):
        """上一页"""

    def next_page(self):
        """下一页"""

    def zoom_in(self):
        """放大页面"""
        self.page_size_mode = ModeImageSize.Fixed

    def zoom_out(self):
        """缩小页面"""
        self.page_size_mode = ModeImageSize.Fixed

    def autoplay_start(self):
        """开始自动播放"""
        self.timer_autoplay.start()
        self.StartAutoPlay.emit()

    def is_autoplay_running(self) -> bool:
        """是否正在自动播放"""
        return self.timer_autoplay.isActive()

    def set_autoplay_speed(self, add_speed: float):
        """设置自动播放的速度
        :param add_speed: 1位小数，变动的自动播放速度"""
        self.speed_autoplay = round(self.speed_autoplay + add_speed, 1)
        # 处理超限
        if self.speed_autoplay < _MIN_SPEED:
            self.speed_autoplay = _MIN_SPEED
        if self.speed_autoplay > _MAX_SPEED:
            self.speed_autoplay = _MAX_SPEED

        self.timer_autoplay.setInterval(int(self.speed_autoplay * 1000))
        return self.speed_autoplay

    def reset_autoplay_speed(self):
        """重置自动播放的速度"""
        self.speed_autoplay = 1.0
        self.timer_autoplay.setInterval(int(self.speed_autoplay * 1000))
        return self.speed_autoplay

    def autoplay_stop(self):
        """停止自动播放"""
        self.timer_autoplay.stop()
        self.StopAutoPlay.emit()

    def _autoplay_end_when_bottom(self):
        """自动播放到尾页/底部时停止"""
        if self.page_index == self.comic_info.page_count:
            self.autoplay_stop()
            return False
        else:
            return True

    def keep_width(self):
        """以宽度为基准，固定尺寸显示图片"""
        if self.page_size_mode is not ModeImageSize.Fixed:
            self.page_size_mode = ModeImageSize.Fixed

    def fit_width(self):
        """以指定宽度为基准，显示图片"""
        if self.page_size_mode is not ModeImageSize.FitWidth:
            self.page_size_mode = ModeImageSize.FitWidth

    def fit_height(self):
        """以指定高度为基准，显示图片"""
        if self.page_size_mode is not ModeImageSize.FitHeight:
            self.page_size_mode = ModeImageSize.FitHeight

    def fit_widget(self):
        """以框架控件为基准，显示图片"""
        if self.page_size_mode is not ModeImageSize.FitPage:
            self.page_size_mode = ModeImageSize.FitPage

    def full_size(self):
        """页面实际尺寸"""
        if self.page_size_mode is not ModeImageSize.FullSize:
            self.page_size_mode = ModeImageSize.FullSize

    def rotate_left(self):
        """页面向左旋转"""

    def rotate_right(self):
        """页面向右旋转"""

    def clear(self):
        """清除显示"""

    def _next_page_autoplay(self):
        """自动播放专用的下一页操作"""
        if self._autoplay_end_when_bottom():
            self.next_page()

    def _update_image_size(self):
        """更新图像的显示尺寸"""
        if self.page_size_mode is ModeImageSize.Fixed:
            self.keep_width()
        elif self.page_size_mode is ModeImageSize.FitPage:
            self.fit_widget()
        elif self.page_size_mode is ModeImageSize.FitWidth:
            self.fit_width()
        elif self.page_size_mode is ModeImageSize.FitHeight:
            self.fit_height()
        elif self.page_size_mode is ModeImageSize.FullSize:
            self.full_size()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_image_size()
