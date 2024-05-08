# 发送自动播放信号的子线程
import time

from PySide6.QtCore import QThread, Signal

from module import function_normal
from module.function_config_get import GetSetting


class ThreadAutoPlay(QThread):
    """发送自动播放信号的子线程"""
    signal_next = Signal(float)
    signal_stop = Signal()
    signal_speed_info = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._PREVIEW_TYPE = None  # 预览类型
        self._is_stop = False  # 是否停止
        self._active_interval = None  # 当前的刷新间隔时间类型
        self._INTERVAL_SCROLL = None  # 滚动视图的刷新间隔时间（秒）
        self._INTERVAL_SINGLE_PAGE = None  # 单页视图的刷新间隔时间（秒）
        self._INTERVAL_DOUBLE_PAGE = None  # 双页视图的刷新间隔时间（秒）
        self._INTERVAL_SCROLL_MIN = None  # 滚动视图的最小刷新间隔时间（秒）
        self._INTERVAL_SINGLE_PAGE_MIN = None  # 单页视图的最小刷新间隔时间（秒）
        self._INTERVAL_DOUBLE_PAGE_MIN = None  # 双页视图的最小刷新间隔时间（秒）
        self._SPEED_RATE_SCROLL = None  # 修改播放速度（滚动）
        self._SPEED_RATE_SINGLE_PAGE = None  # 修改播放速度（单页）
        self._SPEED_RATE_DOUBLE_PAGE = None  # 修改播放速度（双页）

        self._load_setting()

    def _load_setting(self):
        """加载设置"""
        self._INTERVAL_SCROLL = GetSetting.auto_play_interval_scroll()
        self._INTERVAL_SINGLE_PAGE = GetSetting.auto_play_interval_single_page()
        self._INTERVAL_DOUBLE_PAGE = GetSetting.auto_play_interval_double_page()
        self._INTERVAL_SCROLL_MIN = GetSetting.auto_play_interval_scroll_min()
        self._INTERVAL_SINGLE_PAGE_MIN = GetSetting.auto_play_interval_single_page_min()
        self._INTERVAL_DOUBLE_PAGE_MIN = GetSetting.auto_play_interval_double_page_min()
        self._SPEED_RATE_SCROLL = GetSetting.auto_play_speed_rate_scroll()
        self._SPEED_RATE_SINGLE_PAGE = GetSetting.auto_play_speed_rate_single_page()
        self._SPEED_RATE_DOUBLE_PAGE = GetSetting.auto_play_speed_rate_double_page()

    def run(self):
        self._is_stop = False
        while True:
            time.sleep(self._active_interval)
            if self._is_stop:
                self.signal_stop.emit()
                break
            else:
                self.signal_next.emit(self._active_interval)

    def reset_setting(self):
        """初始化设置项"""
        function_normal.print_function_info()
        self._PREVIEW_TYPE = GetSetting.current_view_mode_eng()
        self._load_setting()  # 重置速度变量
        if self._PREVIEW_TYPE == 'mode_1':
            self._active_interval = self._INTERVAL_SINGLE_PAGE
        elif self._PREVIEW_TYPE == 'mode_2':
            self._active_interval = self._INTERVAL_DOUBLE_PAGE
        else:
            self._active_interval = self._INTERVAL_SCROLL

    def _update_active_interval(self):
        """更新启用的刷新时间"""
        function_normal.print_function_info()
        if self._PREVIEW_TYPE == 'mode_1':
            self._active_interval = self._INTERVAL_SINGLE_PAGE
        elif self._PREVIEW_TYPE == 'mode_2':
            self._active_interval = self._INTERVAL_DOUBLE_PAGE
        else:
            self._active_interval = self._INTERVAL_SCROLL

        self._active_interval = round(self._active_interval, 2)  # 统一小数位，加减速后可能会出现尾数
        self._emit_speed_info()

    def speed_up(self):
        """加速"""
        function_normal.print_function_info()
        self._INTERVAL_SCROLL -= self._SPEED_RATE_SCROLL
        if self._INTERVAL_SCROLL < self._INTERVAL_SCROLL_MIN:
            self._INTERVAL_SCROLL = self._INTERVAL_SCROLL_MIN

        self._INTERVAL_SINGLE_PAGE -= self._SPEED_RATE_SINGLE_PAGE
        if self._INTERVAL_SINGLE_PAGE < self._INTERVAL_DOUBLE_PAGE_MIN:
            self._INTERVAL_SINGLE_PAGE = self._INTERVAL_DOUBLE_PAGE_MIN

        self._INTERVAL_DOUBLE_PAGE -= self._SPEED_RATE_DOUBLE_PAGE
        if self._INTERVAL_DOUBLE_PAGE < self._INTERVAL_DOUBLE_PAGE_MIN:
            self._INTERVAL_DOUBLE_PAGE = self._INTERVAL_DOUBLE_PAGE_MIN
        self._update_active_interval()

    def speed_down(self):
        """减速"""
        function_normal.print_function_info()
        self._INTERVAL_SCROLL += self._SPEED_RATE_SCROLL
        self._INTERVAL_SINGLE_PAGE += self._SPEED_RATE_SINGLE_PAGE
        self._INTERVAL_DOUBLE_PAGE += self._SPEED_RATE_DOUBLE_PAGE
        self._update_active_interval()

    def reset_speed(self):
        """重置速度"""
        function_normal.print_function_info()
        self._load_setting()
        self._update_active_interval()

    def stop_play(self):
        self._is_stop = True

    def _emit_speed_info(self):
        """发送速度信息"""
        text = f'当前滚动速度:{round(self._active_interval, 2)}秒'
        self.signal_speed_info.emit(text)
