# 常量
import os
import sys

# 程序所在路径
_PROGRAM_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/'  # 源码运行使用
# _PROGRAM_FOLDER = os.path.dirname(sys.executable) + '/'  # 打包运行使用

# 文件路径
_CONFIG_FILE = _PROGRAM_FOLDER + 'config.ini'

# 图标
_ICON_MAIN = _PROGRAM_FOLDER + 'icon/main.ico'
_ICON_SINGLE_PAGE = _PROGRAM_FOLDER + 'icon/single_page.png'
_ICON_SINGLE_PAGE_RED = _PROGRAM_FOLDER + 'icon/single_page_red.png'
_ICON_DOUBLE_PAGE = _PROGRAM_FOLDER + 'icon/double_page.png'
_ICON_DOUBLE_PAGE_RED = _PROGRAM_FOLDER + 'icon/double_page_red.png'
_ICON_SCROLL_HORIZONTAL = _PROGRAM_FOLDER + 'icon/scroll_horizontal.png'
_ICON_SCROLL_HORIZONTAL_RED = _PROGRAM_FOLDER + 'icon/scroll_horizontal_red.png'
_ICON_SCROLL_VERTICAL = _PROGRAM_FOLDER + 'icon/scroll_vertical.png'
_ICON_SCROLL_VERTICAL_RED = _PROGRAM_FOLDER + 'icon/scroll_vertical_red.png'
_ICON_FIT_HEIGHT = _PROGRAM_FOLDER + 'icon/fit_height.png'
_ICON_FIT_HEIGHT_RED = _PROGRAM_FOLDER + 'icon/fit_height_red.png'
_ICON_FIT_WIDTH = _PROGRAM_FOLDER + 'icon/fit_width.png'
_ICON_FIT_WIDTH_RED = _PROGRAM_FOLDER + 'icon/fit_width_red.png'
_ICON_ZOOM_OUT = _PROGRAM_FOLDER + 'icon/zoom_out.png'
_ICON_ARROW_LEFT = _PROGRAM_FOLDER + 'icon/arrow_left.png'
_ICON_ARROW_RIGHT = _PROGRAM_FOLDER + 'icon/arrow_right.png'
_ICON_LIST = _PROGRAM_FOLDER + 'icon/list.png'
_ICON_OPTION = _PROGRAM_FOLDER + 'icon/option.png'
_ICON_PLAY = _PROGRAM_FOLDER + 'icon/play.png'
_ICON_STOP = _PROGRAM_FOLDER + 'icon/stop.png'
_ICON_ZOOM_IN = _PROGRAM_FOLDER + 'icon/zoom_in.png'

# 其他常量
_MARGIN = 16  # 与边框的边距，用于预留滚动条的距离

# 本地监听端口
_HOST = '127.0.0.1'
_PORT = 9527
