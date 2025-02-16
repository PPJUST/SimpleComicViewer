from PySide6.QtWidgets import QFileDialog


def select_folder():
    """选择单个文件夹"""
    dirpath = QFileDialog.getExistingDirectory(
        None,  # 父窗口
        "选择文件夹类漫画",  # 弹窗标题
        '',  # 默认打开的路径（空字符串表示当前目录）
        QFileDialog.Option.ShowDirsOnly  # 只显示文件夹
    )

    return dirpath


def select_archive():
    """选择单个压缩文件"""
    archive_filter = '*.zip *.rar'
    filepath, _ = QFileDialog.getOpenFileName(
        None,  # 父窗口
        "选择压缩文件类漫画",  # 弹窗标题
        '',  # 默认打开的路径（空字符串表示当前目录）,
        filter=archive_filter
    )

    return filepath


def select_pdf():
    """选择单个PDF"""
    archive_filter = '*pdf'
    filepath, _ = QFileDialog.getOpenFileName(
        None,  # 父窗口
        "选择PDF类漫画",  # 弹窗标题
        '',  # 默认打开的路径（空字符串表示当前目录）,
        filter=archive_filter
    )

    return filepath
