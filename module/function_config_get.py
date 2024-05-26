# 配置文件相关方法-获取设置项的方法
import configparser

from module.function_config_normal import _CONFIG_FILE


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
    def random_play():
        """获取随机播放选项"""
        value = _get_setting_normal('option', 'random_play')
        return value

    @staticmethod
    def hide_wait_time_small():
        """获取隐藏控件延迟时间选项"""
        value = _get_setting_normal('constant', 'hide_wait_time_small')
        return value

    @staticmethod
    def hide_wait_time_medium():
        """获取隐藏控件延迟时间选项"""
        value = _get_setting_normal('constant', 'hide_wait_time_medium')
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
        width = _get_setting_normal('size', 'app_width')
        height = _get_setting_normal('size', 'app_height')

        return width, height

    @staticmethod
    def playlist_width():
        """获取播放列表大小选项"""
        value = _get_setting_normal('size', 'playlist_width')
        return value

    @staticmethod
    def playlist_height():
        """获取播放列表大小选项"""
        value = _get_setting_normal('size', 'playlist_height')
        return value

    @staticmethod
    def playlist_column_max_height():
        """获取播放列表宽度选项"""
        value = _get_setting_normal('size', 'playlist_column_max_height')
        return value

    @staticmethod
    def button_small():
        """获取按钮大小选项"""
        value = _get_setting_normal('size', 'button_small')
        return value

    @staticmethod
    def button_medium():
        """获取按钮大小选项"""
        value = _get_setting_normal('size', 'button_medium')
        return value

    @staticmethod
    def button_large():
        """获取按钮大小选项"""
        value = _get_setting_normal('size', 'button_large')
        return value

    @staticmethod
    def comic_info_width():
        """获取漫画信息控件大小选项"""
        value = _get_setting_normal('size', 'comic_info_width')
        return value

    @staticmethod
    def comic_info_height():
        """获取漫画信息控件大小选项"""
        value = _get_setting_normal('size', 'comic_info_height')
        return value

    @staticmethod
    def margin_small():
        """获取左上角控件的边距选项"""
        value = _get_setting_normal('size', 'margin_small')
        return value

    @staticmethod
    def margin_medium():
        """获取左下角控件的边距选项"""
        value = _get_setting_normal('size', 'margin_medium')
        return value

    @staticmethod
    def margin_large():
        """获取右上角控件的边距选项"""
        value = _get_setting_normal('size', 'margin_large')
        return value

    @staticmethod
    def margin_preview():
        """获取预览控件边距选项"""
        value = _get_setting_normal('size', 'margin_preview')
        return value

    @staticmethod
    def host():
        """获取主机号选项"""
        value = _get_setting_str('constant', 'host')
        return value

    @staticmethod
    def port():
        """获取端口号选项"""
        value = _get_setting_normal('constant', 'port')
        return value

    @staticmethod
    def image_suffix():
        """获取支持的图片后缀选项"""
        value = _get_setting_str('constant', 'image_suffix')
        return value

    @staticmethod
    def archive_suffix():
        """获取支持的压缩包后缀选项"""
        value = _get_setting_str('constant', 'archive_suffix')
        return value

    @staticmethod
    def comic_min_page_count():
        """获取识别漫画最小图片数选项"""
        value = _get_setting_normal('constant', 'comic_min_page_count')
        return value

    @staticmethod
    def resize_image_hash():
        """获取计算图片hash时的缩放大小选项"""
        value = _get_setting_normal('constant', 'resize_image_hash')
        return value

    @staticmethod
    def horizontal_image_aspect_ratio():
        """获取横向图像纵横比选项"""
        value = _get_setting_normal('constant', 'horizontal_image_aspect_ratio')
        return value


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
