# 图片相关方法
from io import BytesIO

from PIL import Image

from module import function_comic


def get_image_size(image_path):
    """获取图片的宽高"""
    image = Image.open(image_path)
    size = image.size
    return size


def get_image_size_from_archive(archive, image_path):
    """从压缩包中读取图片的宽高"""
    img_bytes = function_comic.read_image_in_archive(archive, image_path)
    img_stream = BytesIO(img_bytes)
    image = Image.open(img_stream)
    size = image.size
    return size


def is_horizontal_image(image_path):
    """判断图片是否为横向图像（纵横比超过1.4）
    一般漫画纸比例为0.7"""
    width, height = get_image_size(image_path)
    if width / height > 1.4:
        return True
    else:
        return False
