# 一般方法
import inspect
import os
import time

import filetype

from constant import _IMAGE_SUFFIX, _ARCHIVE_SUFFIX


def print_function_info(mode: str = 'current'):
    """
    打印当前/上一个执行的函数信息
    :param mode: str类型，'current' 或 'last'
    """
    # pass

    if mode == 'current':
        print(time.strftime('%H:%M:%S ', time.localtime()),
              inspect.getframeinfo(inspect.currentframe().f_back).function)
    elif mode == 'last':
        print(time.strftime('%H:%M:%S ', time.localtime()),
              inspect.getframeinfo(inspect.currentframe().f_back.f_back).function)


def check_filetype(file: str):
    """获取一个文件的文件类型"""
    # 为了速度，直接使用后缀名判断
    suffix = os.path.splitext(file)[1].lower()
    if suffix in _IMAGE_SUFFIX:
        return 'image'
    elif suffix in _ARCHIVE_SUFFIX:
        return 'archive'


def is_archive(path):
    """文件是否为压缩包"""
    kind = filetype.guess(path)
    if kind is None:
        return False

    guess_type = kind.extension
    archive_suffix_remove_point = [i[1:] for i in _ARCHIVE_SUFFIX]
    if guess_type in archive_suffix_remove_point:
        return True
    else:
        return False


def get_folder_size(folder: str) -> int:
    """获取指定文件夹的总大小/byte
    :param folder: str类型，文件夹路径
    :return: int类型，总字节大小
    """
    folder_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for item in filenames:
            filepath = os.path.join(dirpath, item)
            folder_size += os.path.getsize(filepath)

    return folder_size
