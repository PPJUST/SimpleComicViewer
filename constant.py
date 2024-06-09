# 常量
import os
import sys

from module import function_config_normal

# 程序所在路径
_PROGRAM_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/'  # 源码运行使用
# _PROGRAM_FOLDER = os.path.dirname(sys.executable) + '/'  # 打包运行使用

# 配置文件路径
_CONFIG_FILE = _PROGRAM_FOLDER + 'config.ini'
function_config_normal.create_default_config(_CONFIG_FILE)

from module.function_config_get import GetSetting

# 图标
_ICON_MAIN = _PROGRAM_FOLDER + 'icon/main.ico'
_ICON_SINGLE_PAGE = _PROGRAM_FOLDER + 'icon/single_page.png'
_ICON_SINGLE_PAGE_RED = _PROGRAM_FOLDER + 'icon/single_page_red.png'
_ICON_DOUBLE_PAGE = _PROGRAM_FOLDER + 'icon/double_page.png'
_ICON_DOUBLE_PAGE_RED = _PROGRAM_FOLDER + 'icon/double_page_red.png'
_ICON_DOUBLE_PAGE_REVERSE = _PROGRAM_FOLDER + 'icon/double_page_reverse.png'
_ICON_DOUBLE_PAGE_REVERSE_RED = _PROGRAM_FOLDER + 'icon/double_page_reverse_red.png'
_ICON_SCROLL_HORIZONTAL = _PROGRAM_FOLDER + 'icon/scroll_horizontal.png'
_ICON_SCROLL_HORIZONTAL_RED = _PROGRAM_FOLDER + 'icon/scroll_horizontal_red.png'
_ICON_SCROLL_HORIZONTAL_REVERSE = _PROGRAM_FOLDER + 'icon/scroll_horizontal_reverse.png'
_ICON_SCROLL_HORIZONTAL_REVERSE_RED = _PROGRAM_FOLDER + 'icon/scroll_horizontal_reverse_red.png'
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
_ICON_ARCHIVE = _PROGRAM_FOLDER + 'icon/archive.png'
_ICON_FOLDER = _PROGRAM_FOLDER + 'icon/folder.png'
_ICON_CHECKED_GRAY = _PROGRAM_FOLDER + 'icon/checked_gray.png'
_ICON_CHECKED_GREEN = _PROGRAM_FOLDER + 'icon/checked_green.png'
_ICON_WARNING = _PROGRAM_FOLDER + 'icon/warning.png'
_ICON_NO_PIC = _PROGRAM_FOLDER + 'icon/no_pic.png'

# 其他常量
_IMAGE_SUFFIX = GetSetting.image_suffix().split(' ')
_ARCHIVE_SUFFIX = GetSetting.archive_suffix().split(' ')
_COMIC_MIN_PAGE_COUNT = GetSetting.comic_min_page_count()
_RESIZE_IMAGE_HASH = GetSetting.resize_image_hash()
_HORIZONTAL_IMAGE_ASPECT_RATIO = GetSetting.horizontal_image_aspect_ratio()
_PLAYLIST_WIDTH = GetSetting.playlist_width()
_PLAYLIST_HEIGHT = GetSetting.playlist_height()
_PLAYLIST_COLUMN_MAX_HEIGHT = GetSetting.playlist_column_max_height()
_BUTTON_SMALL = GetSetting.button_small()
_BUTTON_MEDIUM = GetSetting.button_medium()
_BUTTON_LARGE = GetSetting.button_large()
_COMIC_INFO_WIDTH = GetSetting.comic_info_width()
_COMIC_INFO_HEIGHT = GetSetting.comic_info_height()
_MARGIN_SMALL = GetSetting.margin_small()
_MARGIN_MEDIUM = GetSetting.margin_medium()
_MARGIN_LARGE = GetSetting.margin_large()
_MARGIN_PREVIEW = GetSetting.margin_preview()  # 与边框的边距，用于预留滚动条的距离

# 本地监听端口
_HOST = GetSetting.host()
_PORT = GetSetting.port()
