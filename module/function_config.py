# 配置文件相关方法
import configparser
import os

from constant import _CONFIG_FILE


def create_default_config():
    """创建初始配置文件"""
    if not os.path.exists(_CONFIG_FILE):
        with open(_CONFIG_FILE, 'w', encoding='utf-8') as cw:
            config = configparser.ConfigParser()
            config.read(_CONFIG_FILE, encoding='utf-8')
            # 视图选项
            config.add_section('view_mode')
            config.set('view_mode', 'mode_1', '普通视图')
            config.set('view_mode', 'mode_2', '双页视图')
            config.set('view_mode', 'mode_3', '纵向滚动视图')
            config.set('view_mode', 'mode_4', '横向滚动视图')
            # 切页选项
            config.add_section('switch_page_mode')
            config.set('switch_page_mode', 'mode_1', '循环浏览')
            config.set('switch_page_mode', 'mode_2', '切换到上/下一本漫画')
            # 大小适应选项
            config.add_section('fit_mode')
            config.set('fit_mode', 'mode_1', '适应宽度')
            config.set('fit_mode', 'mode_2', '适应高度')
            config.set('fit_mode', 'mode_3', '其他')
            # 自动播放选项
            config.add_section('auto_play')
            config.set('auto_play', 'interval_scroll', '0.2')
            config.set('auto_play', 'interval_single_page', '1')
            config.set('auto_play', 'interval_double_page', '2')
            config.set('auto_play', 'interval_scroll_min', '0.1')
            config.set('auto_play', 'interval_single_page_min', '0.5')
            config.set('auto_play', 'interval_double_page_min', '0.5')
            config.set('auto_play', 'speed_rate_scroll', '0.1')
            config.set('auto_play', 'speed_rate_single_page', '0.5')
            config.set('auto_play', 'speed_rate_double_page', '0.5')
            config.set('auto_play', 'scroll_distance', '100')
            # 设置项
            config.add_section('option')
            config.set('option', 'view_mode', 'mode_1')
            config.set('option', 'switch_page_mode', 'mode_1')
            config.set('option', 'fit_mode', 'mode_1')
            config.set('option', 'skip_solid_color_page', 'False')
            config.set('option', 'sharpen_image', 'False')
            config.set('option', 'preload_pages', '5')
            config.set('option', 'hide_wait_time', '1')

            config.write(open(_CONFIG_FILE, 'w', encoding='utf-8'))
            cw.close()


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
    def auto_play_interval_scroll():
        """获取自动播放选项"""
        value = _get_setting_normal('auto_play', 'interval_scroll')
        return value

    @staticmethod
    def auto_play_interval_scroll_min():
        """获取自动播放选项"""
        value = _get_setting_normal('auto_play', 'interval_scroll_min')
        return value

    @staticmethod
    def auto_play_interval_single_page():
        """获取自动播放选项"""
        value = _get_setting_normal('auto_play', 'interval_single_page')
        return value

    @staticmethod
    def auto_play_interval_single_page_min():
        """获取自动播放选项"""
        value = _get_setting_normal('auto_play', 'interval_single_page_min')
        return value

    @staticmethod
    def auto_play_interval_double_page():
        """获取自动播放选项"""
        value = _get_setting_normal('auto_play', 'interval_double_page')
        return value

    @staticmethod
    def auto_play_interval_double_page_min():
        """获取自动播放选项"""
        value = _get_setting_normal('auto_play', 'interval_double_page_min')
        return value

    @staticmethod
    def auto_play_speed_rate_scroll():
        """获取自动播放选项"""
        value = _get_setting_normal('auto_play', 'speed_rate_scroll')
        return value

    @staticmethod
    def auto_play_speed_rate_single_page():
        """获取自动播放选项"""
        value = _get_setting_normal('auto_play', 'speed_rate_single_page')
        return value

    @staticmethod
    def auto_play_speed_rate_double_page():
        """获取自动播放选项"""
        value = _get_setting_normal('auto_play', 'speed_rate_double_page')
        return value

    @staticmethod
    def auto_play_scroll_distance():
        """获取自动播放选项"""
        value = _get_setting_normal('auto_play', 'scroll_distance')
        return value


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
    def auto_play_interval_scroll(value):
        """修改自动播放选项"""
        _reset_setting('auto_play', 'interval_scroll', value)

    @staticmethod
    def auto_play_interval_single_page(value):
        """修改自动播放选项"""
        _reset_setting('auto_play', 'interval_single_page', value)

    @staticmethod
    def auto_play_interval_double_page(value):
        """修改自动播放选项"""
        _reset_setting('auto_play', 'interval_double_page', value)

    @staticmethod
    def auto_play_speed_rate_scroll(value):
        """修改自动播放选项"""
        _reset_setting('auto_play', 'speed_rate_scroll', value)

    @staticmethod
    def auto_play_speed_rate_single_page(value):
        """修改自动播放选项"""
        _reset_setting('auto_play', 'speed_rate_single_page', value)

    @staticmethod
    def auto_play_speed_rate_double_page(value):
        """修改自动播放选项"""
        _reset_setting('auto_play', 'speed_rate_double_page', value)

    @staticmethod
    def auto_play_scroll_distance(value):
        """修改自动播放选项"""
        _reset_setting('auto_play', 'scroll_distance', value)


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


def _reset_setting(section: str, option: str, value):
    """重设配置文件中的选项"""
    config = configparser.ConfigParser()
    config.read(_CONFIG_FILE, encoding='utf-8')
    config.set(section, option, str(value))
    config.write(open(_CONFIG_FILE, 'w', encoding='utf-8'))
