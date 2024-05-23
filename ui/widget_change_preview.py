# 主界面左上方的切换预览视图类型的组件

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout

from constant import (_ICON_DOUBLE_PAGE, _ICON_DOUBLE_PAGE_RED,
                      _ICON_SCROLL_HORIZONTAL, _ICON_SCROLL_HORIZONTAL_RED,
                      _ICON_SCROLL_VERTICAL, _ICON_SCROLL_VERTICAL_RED,
                      _ICON_SINGLE_PAGE, _ICON_SINGLE_PAGE_RED)
from module import function_normal
from module.function_config_get import GetSetting
from module.function_config_reset import ResetSetting
from thread.thread_wait_time import ThreadWaitTime
from ui.ui_src.ui_widget_top_control_child import Ui_Form


class WidgetChangePreview(QWidget):
    """主界面左上方的切换预览视图类型的组件（主程序使用的控件，用于中转子控件的信号和继承隐藏事件）"""
    signal_preview_mode_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # ui设置
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.widget = WidgetChangePreviewChild()
        self.layout.addWidget(self.widget)
        self.installEventFilter(self.widget)
        self.widget.raise_()  # 使该label显示在widget之上

        # 固定size大小，用于setGeometry方法设置相对位置
        self._size = self.sizeHint()

        # 中转子控件信号
        self.widget.signal_preview_mode_changed.connect(
            self.signal_preview_mode_changed.emit)

    def set_active_icon(self, preview_mode):
        """手动设置预览模式"""
        self.widget.set_active_icon(preview_mode)

    def reset_xy(self, x: int, y: int):
        """重设坐标轴位置"""
        self.setGeometry(x, y, self._size.width(), self._size.height())


class WidgetChangePreviewChild(QWidget):
    """主界面左上方的切换预览视图类型的组件（作为子控件，用于编写隐藏事件）"""
    signal_preview_mode_changed = Signal()  # 改变预览模式

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # ui设置
        self.setMouseTracking(True)
        self._reset_icon_preview_button()
        self._load_button_size()

        # 初始化
        self._preview_mode = None  # 当前选择的预览模式（英文名mode_*
        self._load_setting()

        # 设置延迟子线程
        self.thread_wait = ThreadWaitTime()
        self.thread_wait.signal_start.connect(self.show)
        self.thread_wait.signal_end.connect(self.hide)

        # 连接信号
        self.ui.toolButton_preview_single.clicked.connect(
            lambda: self._click_preview_button('mode_1'))
        self.ui.toolButton_preview_double.clicked.connect(
            lambda: self._click_preview_button('mode_2'))
        self.ui.toolButton_preview_v.clicked.connect(
            lambda: self._click_preview_button('mode_3'))
        self.ui.toolButton_preview_h.clicked.connect(
            lambda: self._click_preview_button('mode_4'))

    def set_active_icon(self, preview_mode):
        """手动设置预览模式"""
        self._preview_mode = preview_mode
        self._change_preview_mode()

    def _load_setting(self):
        """加载设置"""
        self._preview_mode = GetSetting.current_view_mode_eng()
        self._change_preview_mode()

    def _click_preview_button(self, mode: str):
        """点击预览视图按钮"""
        function_normal.print_function_info()
        if self._preview_mode != mode:
            self._preview_mode = mode
            self._change_preview_mode()

    def _change_preview_mode(self):
        """改变预览模式"""
        function_normal.print_function_info()
        # 修改图标
        self._update_icon()
        # 修改设置文件
        ResetSetting.current_view_mode(self._preview_mode)
        # 发送信号
        self.signal_preview_mode_changed.emit()

    def _update_icon(self):
        """根据当前视图选项更新图标"""
        # 先重置
        self._reset_icon_preview_button()
        # 再更新
        if self._preview_mode == 'mode_1':
            self.ui.toolButton_preview_single.setIcon(QIcon(_ICON_SINGLE_PAGE_RED))
        elif self._preview_mode == 'mode_2':
            self.ui.toolButton_preview_double.setIcon(QIcon(_ICON_DOUBLE_PAGE_RED))
        elif self._preview_mode == 'mode_3':
            self.ui.toolButton_preview_v.setIcon(QIcon(_ICON_SCROLL_VERTICAL_RED))
        elif self._preview_mode == 'mode_4':
            self.ui.toolButton_preview_h.setIcon(QIcon(_ICON_SCROLL_HORIZONTAL_RED))

    def _reset_icon_preview_button(self):
        """重置按钮图标"""
        self.ui.toolButton_preview_single.setIcon(QIcon(_ICON_SINGLE_PAGE))
        self.ui.toolButton_preview_double.setIcon(QIcon(_ICON_DOUBLE_PAGE))
        self.ui.toolButton_preview_v.setIcon(QIcon(_ICON_SCROLL_VERTICAL))
        self.ui.toolButton_preview_h.setIcon(QIcon(_ICON_SCROLL_HORIZONTAL))

    def _load_button_size(self):
        """设置按钮的大小"""
        button_size = 30
        self.ui.toolButton_preview_single.setMinimumSize(button_size, button_size)
        self.ui.toolButton_preview_double.setMinimumSize(button_size, button_size)
        self.ui.toolButton_preview_v.setMinimumSize(button_size, button_size)
        self.ui.toolButton_preview_h.setMinimumSize(button_size, button_size)

    def eventFilter(self, obj, event):
        """隐藏事件"""
        if event.type() == event.Enter:
            if not self.thread_wait.isRunning():
                self.thread_wait.start()
            self.thread_wait.enable_loop()
        elif event.type() == event.Leave:
            self.thread_wait.reset_end_time()
            self.thread_wait.disable_loop()
            if not self.thread_wait.isRunning():
                self.thread_wait.start()
        return super().eventFilter(obj, event)
