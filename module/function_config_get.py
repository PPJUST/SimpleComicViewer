# 配置文件相关方法-获取设置项的方法
import configparser

from constant import _CONFIG_FILE


class GetSetting:
    """获取设置项的类"""

    @staticmethod
    def view_modes():
        """获取视图列表"""
        return _get_setting_list('view_mode')

    @staticmethod
    def switch_page_modes():
        """获取切页模式列表"""
        return _get_setting_list('switch_page_mode')

    @staticmethod
    def current_view_mode_chs():
        """获取当前视图选项"""
        mode_index = _get_setting_str('option', 'view_mode')
        value = _get_setting_str('view_mode', mode_index)
        return value

    @staticmethod
    def current_view_mode_eng():
        """获取当前视图选项的原始名称 mode_"""
        mode_index = _get_setting_str('option', 'view_mode')
        return mode_index

    @staticmethod
    def current_switch_page_mode():
        """获取当前切页模式选项"""
        mode_index = _get_setting_str('option', 'switch_page_mode')
        value = _get_setting_str('switch_page_mode', mode_index)
        return value

    @staticmethod
    def current_fit_mode():
        """获取当前大小适应模式选项"""
        mode_index = _get_setting_str('option', 'fit_mode')
        return mode_index

    @staticmethod
    def skip_solid_color_page():
        """获取是否跳过纯色页选项"""
        value = _get_setting_normal('option', 'skip_solid_color_page')
        return value

    @staticmethod
    def sharpen_image():
        """获取是否锐化图像选项"""
        value = _get_setting_normal('option', 'sharpen_image')
        return value

    @staticmethod
    def preload_pages():
        """获取预载图像页数选项"""
        value = _get_setting_normal('option', 'preload_pages')
        return value

    @staticmethod
    def hide_wait_time():
        """获取隐藏控件延迟时间选项"""
        value = _get_setting_normal('option', 'hide_wait_time')
        return value

    @staticmethod
    def autoplay_interval_scroll():
        """获取自动播放选项"""
        value = _get_setting_normal('autoplay', 'interval_scroll')
        return value

    @staticmethod
    def autoplay_interval_scroll_min():
        """获取自动播放选项"""
        value = _get_setting_normal('autoplay', 'interval_scroll_min')
        return value

    @staticmethod
    def autoplay_interval_single_page():
        """获取自动播放选项"""
        value = _get_setting_normal('autoplay', 'interval_single_page')
        return value

    @staticmethod
    def autoplay_interval_single_page_min():
        """获取自动播放选项"""
        value = _get_setting_normal('autoplay', 'interval_single_page_min')
        return value

    @staticmethod
    def autoplay_interval_double_page():
        """获取自动播放选项"""
        value = _get_setting_normal('autoplay', 'interval_double_page')
        return value

    @staticmethod
    def autoplay_interval_double_page_min():
        """获取自动播放选项"""
        value = _get_setting_normal('autoplay', 'interval_double_page_min')
        return value

    @staticmethod
    def autoplay_speed_rate_scroll():
        """获取自动播放选项"""
        value = _get_setting_normal('autoplay', 'speed_rate_scroll')
        return value

    @staticmethod
    def autoplay_speed_rate_single_page():
        """获取自动播放选项"""
        value = _get_setting_normal('autoplay', 'speed_rate_single_page')
        return value

    @staticmethod
    def autoplay_speed_rate_double_page():
        """获取自动播放选项"""
        value = _get_setting_normal('autoplay', 'speed_rate_double_page')
        return value

    @staticmethod
    def autoplay_scroll_distance():
        """获取自动播放选项"""
        value = _get_setting_normal('autoplay', 'scroll_distance')
        return value

    @staticmethod
    def app_size():
        """获取程序界面大小选项"""
        width = _get_setting_normal('other', 'app_width')
        height = _get_setting_normal('other', 'app_height')

        return width, height


def _get_setting_str(section: str, option: str):
    """获取配置文件中的文本项"""
    config = configparser.ConfigParser()
    config.read(_CONFIG_FILE, encoding='utf-8')
    value = config.get(section, option)
    return value


def _get_setting_normal(section: str, option: str):
    """获取配置文件中的非文本格式的项"""
    config = configparser.ConfigParser()
    config.read(_CONFIG_FILE, encoding='utf-8')
    value = config.get(section, option)
    return eval(value)


def _get_setting_list(section: str):
    """获取配置文件中的列表项"""
    config = configparser.ConfigParser()
    config.read(_CONFIG_FILE, encoding='utf-8')
    options = config.options(section)
    values = [config.get(section, i) for i in options]
    return values
