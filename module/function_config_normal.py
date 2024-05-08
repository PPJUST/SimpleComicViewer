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
            config.set('auto_play', 'interval_scroll', '1')
            config.set('auto_play', 'interval_single_page', '1')
            config.set('auto_play', 'interval_double_page', '2')
            config.set('auto_play', 'interval_scroll_min', '0.05')
            config.set('auto_play', 'interval_single_page_min', '0.25')
            config.set('auto_play', 'interval_double_page_min', '0.25')
            config.set('auto_play', 'speed_rate_scroll', '0.05')
            config.set('auto_play', 'speed_rate_single_page', '0.25')
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
            # 其他选项
            config.add_section('other')
            config.set('other', 'app_width', '600')
            config.set('other', 'app_height', '600')

            config.write(open(_CONFIG_FILE, 'w', encoding='utf-8'))
            cw.close()
