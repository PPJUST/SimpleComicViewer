# 图片相关方法
from io import BytesIO

import imagehash
from PIL import Image

from constant import _RESIZE_IMAGE_HASH, _HORIZONTAL_IMAGE_ASPECT_RATIO
from module import function_comic



def is_horizontal_image(image_path):
    """判断图片是否为横向图像（纵横比超过指定值）
    一般漫画纸比例为0.7"""
    width, height = get_image_size(image_path)
    if width / height > _HORIZONTAL_IMAGE_ASPECT_RATIO:
        return True
    else:
        return False




