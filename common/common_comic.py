import os

import lzytools.archive
import lzytools.file

_IMAGE_LIMIT = 4
_IMAGE_SUFFIX = ('.jpg', '.png', '.webp', '.jpeg', '.gif', '.bmp')
_ARCHIVE_SUFFIX = ('zip', 'rar')  # filetype库使用，返回的文件扩展名不带.


def is_comic(filepath: str):
    """路径对应文件/文件夹是否是漫画
    仅支持rar、zip和文件夹类漫画"""
    if os.path.isdir(filepath):
        return is_comic_folder(filepath)
    elif lzytools.file.guess_filetype(filepath) in _ARCHIVE_SUFFIX:
        return is_comic_archive(filepath)
    else:  # 备忘录 PDF之后在写
        return False


def is_comic_archive(archive_path):
    """是否为漫画压缩包（内部图片数>=指定值）"""
    files = lzytools.archive.get_infolist(archive_path)
    images = [i for i in files if i.lower().endswith(_IMAGE_SUFFIX)]
    if len(images) >= _IMAGE_LIMIT:
        return True
    else:
        return False


def is_comic_folder(dirpath):
    """是否为漫画压缩包（内部图片数>=指定值）"""
    files = lzytools.file.get_files_in_dir(dirpath)
    images = [i for i in files if i.lower().endswith(_IMAGE_SUFFIX)]
    if len(images) >= _IMAGE_LIMIT:
        return True
    else:
        return False
