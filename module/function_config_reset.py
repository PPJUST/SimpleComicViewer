# 配置文件相关方法-修改设置项的方法
import configparser

from constant import _CONFIG_FILE
from module.function_config_get import _get_setting_list


class ResetSetting:
    """修改设置项的类"""

    @staticmethod
    def current_view_mode(value):
        """修改当前视图选项"""
        _reset_setting('option', 'view_mode', value)

    @staticmethod
    def current_switch_page_mode(value):
        """修改当前切页模式选项"""
        view_modes = _get_setting_list('switch_page_mode')
        current_index = view_modes.index(value)
        _reset_setting('option', 'switch_page_mode',
                       f'mode_{current_index + 1}')

    @staticmethod
    def current_fit_mode(value):
        """修改当前大小适应模式选项"""
        _reset_setting('option', 'fit_mode', value)

    @staticmethod
    def skip_solid_color_page(value):
        """修改是否跳过纯色页选项"""
        _reset_setting('option', 'skip_solid_color_page', value)

    @staticmethod
    def sharpen_image(value):
        """修改是否锐化图像选项"""
        _reset_setting('option', 'sharpen_image', value)

    @staticmethod
    def preload_pages(value):
        """修改预载图像页数选项"""
        _reset_setting('option', 'preload_pages', value)

    @staticmethod
    def autoplay_interval_scroll(value):
        """修改自动播放选项"""
        _reset_setting('autoplay', 'interval_scroll', value)

    @staticmethod
    def autoplay_interval_single_page(value):
        """修改自动播放选项"""
        _reset_setting('autoplay', 'interval_single_page', value)

    @staticmethod
    def autoplay_interval_double_page(value):
        """修改自动播放选项"""
        _reset_setting('autoplay', 'interval_double_page', value)

    @staticmethod
    def autoplay_speed_rate_scroll(value):
        """修改自动播放选项"""
        _reset_setting('autoplay', 'speed_rate_scroll', value)

    @staticmethod
    def autoplay_speed_rate_single_page(value):
        """修改自动播放选项"""
        _reset_setting('autoplay', 'speed_rate_single_page', value)

    @staticmethod
    def autoplay_speed_rate_double_page(value):
        """修改自动播放选项"""
        _reset_setting('autoplay', 'speed_rate_double_page', value)

    @staticmethod
    def autoplay_scroll_distance(value):
        """修改自动播放选项"""
        _reset_setting('autoplay', 'scroll_distance', value)

    @staticmethod
    def app_size(width, height):
        """修改程序界面大小选项"""
        _reset_setting('other', 'app_width', width)
        _reset_setting('other', 'app_height', height)


def _reset_setting(section: str, option: str, value):
    """重设配置文件中的选项"""
    config = configparser.ConfigParser()
    config.read(_CONFIG_FILE, encoding='utf-8')
    config.set(section, option, str(value))
    config.write(open(_CONFIG_FILE, 'w', encoding='utf-8'))
