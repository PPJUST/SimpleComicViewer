# 图片相关方法
from io import BytesIO

import imagehash
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


def is_pure_color(image_path):
    """是否为纯色图片"""
    # 考虑到软件大小，使用计算图片hash的方法来判断纯色图片，opencv库太大了
    try:
        image_pil = Image.open(image_path)
        image_pil = image_pil.convert('L')  # 转灰度图
    # 如果图片损坏，会抛出异常OSError: image file is truncated (4 bytes not processed)
    except OSError:
        return False

    image_pil = image_pil.resize(size=(10, 10))
    ahash = imagehash.average_hash(image_pil, hash_size=10)
    hash_str = _hash_numpy2str(ahash)

    if hash_str.count('0') == len(hash_str):
        return True
    else:
        return False


def _hash_numpy2str(hash_numpy):
    """将哈希值的numpy数组(imagehash.hash)转换为二进制字符串"""
    if not hash_numpy:
        return None

    if type(hash_numpy) is imagehash.ImageHash:
        hash_numpy = hash_numpy.hash

    hash_str = ''
    for row in hash_numpy:
        for col in row:
            if col:
                hash_str += '1'
            else:
                hash_str += '0'

    return hash_str
