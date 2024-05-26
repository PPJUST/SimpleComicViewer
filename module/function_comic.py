# 漫画相关方法
import os
import zipfile

import natsort
import rarfile

from constant import _IMAGE_SUFFIX, _COMIC_MIN_PAGE_COUNT
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
    file_suffix = os.path.splitext(file)[1].lower()
    if file_suffix in _IMAGE_SUFFIX:
        return True
    else:
        return False


def is_comic_archive(archive_path):
    """是否为漫画压缩包（内部图片数>=指定值）"""
    if function_normal.is_archive(archive_path) and len(extract_archive_images(archive_path)) >= _COMIC_MIN_PAGE_COUNT:
        return True
    else:
        return False


def filter_comic_folder_and_archive(check_dirpath):
    """从文件夹中筛选出符合要求的漫画文件夹和所有压缩包"""
    function_normal.print_function_info()
    folder_structure_dict = dict()  # 文件夹内部文件类型 {文件夹路径:{'dir':set(), 'image':set(), 'archive':set()}, ...}

    for dirpath, dirnames, filenames in os.walk(check_dirpath):
        # 提取所有文件夹，建立字典的key
        for dirname in dirnames:
            dirpath_join = os.path.normpath(os.path.join(dirpath, dirname))
            # 字典中添加当前文件夹key
            if dirpath_join not in folder_structure_dict:
                folder_structure_dict[dirpath_join] = {'dir': set(), 'image': set(), 'archive': set()}
            # 字典中添加父目录key，并添加value
            parent_dir = os.path.split(dirpath_join)[0]
            if parent_dir not in folder_structure_dict:
                folder_structure_dict[parent_dir] = {'dir': set(), 'image': set(), 'archive': set()}
            folder_structure_dict[parent_dir]['dir'].add(dirpath_join)

        # 提取所有文件，写入字典的value
        for filename in filenames:
            filepath_join = os.path.normpath(os.path.join(dirpath, filename))
            parent_dir = os.path.split(filepath_join)[0]
            if parent_dir not in folder_structure_dict:
                folder_structure_dict[parent_dir] = {'dir': set(), 'image': set(), 'archive': set()}
            # 根据文件类型写入不同的key
            filetype = function_normal.check_filetype(filepath_join)
            if filetype == 'image':
                folder_structure_dict[parent_dir]['image'].add(filepath_join)
            elif filetype == 'archive':
                folder_structure_dict[parent_dir]['archive'].add(filepath_join)

    # 检查字典，筛选出符合条件的漫画文件夹（内部图片文件数>=指定值且无压缩包和子文件夹）和压缩包
    comic_archives = set()  # 符合条件的漫画文件夹集合
    comic_folders = set()  # 符合条件的漫画文件夹集合
    for dirpath, inside_structure in folder_structure_dict.items():
        inside_dirs = inside_structure['dir']
        inside_images = inside_structure['image']
        inside_archives = inside_structure['archive']

        if inside_archives:
            # 检查压缩包内图片数量
            for path in inside_archives:
                if len(extract_archive_images(path)) >= _COMIC_MIN_PAGE_COUNT:
                    comic_archives.add(path)
        elif inside_dirs:
            continue
        elif len(inside_images) >= _COMIC_MIN_PAGE_COUNT:
            comic_folders.add(dirpath)

    return comic_folders, comic_archives


def extract_comic(paths: list) -> list:
    """从路径list中提取符合要求的漫画文件夹和漫画压缩包"""
    comic_folders = set()
    comic_archives = set()
    for path in paths:
        if os.path.isdir(path):
            folders, archives = filter_comic_folder_and_archive(path)
            comic_folders.update(folders)
            comic_archives.update(archives)
        elif os.path.isfile(path):
            if is_comic_archive(path):
                comic_archives.add(path)

    both = comic_folders.union(comic_archives)
    return list(both)
