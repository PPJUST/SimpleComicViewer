# 漫画相关方法
import os
import zipfile

import natsort
import rarfile

from module import function_normal


def read_image_in_archive(archive, image_path):
    """读取压缩包中的图片对象"""
    function_normal.print_function_info()
    try:
        archive_file = zipfile.ZipFile(archive)
    except zipfile.BadZipFile:
        try:
            archive_file = rarfile.RarFile(archive)
        except rarfile.NotRarFile:
            return False

    img_bytes = archive_file.read(image_path)
    archive_file.close()

    return img_bytes


def extract_archive_images(archive: str) -> list:
    """提取压缩包内图片路径"""
    function_normal.print_function_info()
    try:
        archive_file = zipfile.ZipFile(archive)
    except zipfile.BadZipFile:
        try:
            archive_file = rarfile.RarFile(archive)
        except rarfile.NotRarFile:
            return []

    files = archive_file.namelist()  # 中文会变为乱码，可以考虑转utf-8编码
    images = []
    for file in files:
        if _is_image_suffix(file):
            images.append(file)
    images = natsort.natsorted(images)
    return images


def extract_folder_images(folder) -> list:
    """提取文件夹内图片路径"""
    function_normal.print_function_info()
    images = []
    for i in os.listdir(folder):
        filepath = os.path.normpath(os.path.join(folder, i))
        if _is_image_suffix(filepath):
            images.append(filepath)
    images = natsort.natsorted(images)
    return images


def _is_image_suffix(file: str):
    """判断一个文件后缀是否是图片类型"""
    # 为了速度，直接使用后缀名判断
    image_suffix = ['.jpg', '.png', '.webp', '.jpeg']

    file_suffix = os.path.splitext(file)[1].lower()
    if file_suffix in image_suffix:
        return True
    else:
        return False
