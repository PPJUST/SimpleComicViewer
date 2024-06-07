# 配置文件相关方法
import configparser
import os

_CONFIG_FILE = None


def create_default_config(config_path):
    """创建初始配置文件"""
    global _CONFIG_FILE
    _CONFIG_FILE = config_path
    if not os.path.exists(config_path):
        with open(config_path, 'w', encoding='utf-8') as cw:
            config = configparser.ConfigParser()
            config.read(config_path, encoding='utf-8')

            # 主要设置项
            config.add_section('option')
            config.set('option', 'view_mode', 'mode_1')  # 视图模式
            config.set('option', 'switch_page_mode', 'mode_1')  # 切页模式
            config.set('option', 'skip_solid_color_page', 'False')  # 跳过空白页
            config.set('option', 'sharpen_image', 'False')  # 图像锐化
            config.set('option', 'preload_pages', '5')  # 预载图片数
            config.set('option', 'random_play', 'False')  # 随机播放

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

            # 尺寸设置
            config.add_section('size')
            config.set('size', 'app_width', '600')
            config.set('size', 'app_height', '600')
            config.set('size', 'playlist_width', '300')
            config.set('size', 'playlist_height', '300')
            config.set('size', 'playlist_column_max_height', '300')
            config.set('size', 'button_small', '16')
            config.set('size', 'button_medium', '32')
            config.set('size', 'button_large', '64')
            config.set('size', 'comic_info_width', '200')
            config.set('size', 'comic_info_height', '100')
            config.set('size', 'margin_small', '10')  # 边距（小）
            config.set('size', 'margin_medium', '20')  # 边距（中）
            config.set('size', 'margin_large', '30')  # 边距（大）
            config.set('size', 'margin_preview', '16')  # 预览控件与边框的边距，用于预留滚动条的距离

            # 常量-自动播放
            config.add_section('autoplay')
            config.set('autoplay', 'interval_scroll', '1')
            config.set('autoplay', 'interval_single_page', '1')
            config.set('autoplay', 'interval_double_page', '2')
            config.set('autoplay', 'interval_scroll_min', '0.05')
            config.set('autoplay', 'interval_single_page_min', '0.25')
            config.set('autoplay', 'interval_double_page_min', '0.25')
            config.set('autoplay', 'speed_rate_scroll', '0.05')
            config.set('autoplay', 'speed_rate_single_page', '0.25')
            config.set('autoplay', 'speed_rate_double_page', '0.5')
            config.set('autoplay', 'scroll_distance', '100')

            # 常量-其他
            config.add_section('constant')
            config.set('constant', 'hide_wait_time_small', '0.5')  # 延迟隐藏时间
            config.set('constant', 'hide_wait_time_medium', '1')  # 延迟隐藏时间
            config.set('constant', 'host', '127.0.0.1')
            config.set('constant', 'port', '9527')
            config.set('constant', 'image_suffix', '.jpg .png .webp .jpeg')
            config.set('constant', 'archive_suffix', '.zip .rar')
            config.set('constant', 'comic_min_page_count', '4')  # 识别漫画最小的图片数
            config.set('constant', 'resize_image_hash', '10')  # 计算图片hash时的缩放大小
            config.set('constant', 'horizontal_image_aspect_ratio', '1.4')  # 横向图像纵横比

            config.write(open(config_path, 'w', encoding='utf-8'))
            cw.close()
