import configparser
import os

from common.config import CONFIG_PATH



def check_default():
    """检查初始配置文件"""
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'w', encoding='utf-8') as cw:
            config = configparser.ConfigParser()
            config.read(CONFIG_PATH, encoding='utf-8')

            # 浏览模式
            config.add_section('viewer_mode')
            config.set('viewer_mode', 'current', 'SinglePage')
            config.set('viewer_mode', 'info', 'SinglePage单页视图/DoublePage双页视图/VerticalScroll纵向卷轴/HorizontalScroll横向卷轴')

            # 切换页面到达首尾页时
            config.add_section('switch_page_mode')
            config.set('switch_page_mode', 'current', 'loop')
            config.set('switch_page_mode', 'info', 'notoperation无操作/loop循环浏览/jump切换漫画')

            # 程序尺寸
            config.add_section('app_size')
            config.set('app_size', 'width', '')
            config.set('app_size', 'height', '')

            # 自动播放设置
            config.add_section('autoplay')  # 备忘录
            config.set('autoplay', '', '')

            # socket设置
            config.add_section('socket')
            config.set('socket', 'host', '127.0.0.1')
            config.set('socket', 'port', '9527')

            # 其他设置
            # 跳过空白页
            # 图像锐化
            # 预载图片数量
            # 随机播放



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



            config.write(open(CONFIG_PATH, 'w', encoding='utf-8'))
            cw.close()
