# 图片相关方法
from PIL import Image


def get_image_size(image_path):
    """获取图片的宽高"""
    image = Image.open(image_path)
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
