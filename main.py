import ctypes
import pickle
import socket
import sys

from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtWidgets import QApplication

from constant import _HOST, _ICON_MAIN, _PORT
from module import function_config_normal

from module.function_config_get import GetSetting
from ui.SimpleComicViewer import SimpleComicViewer


def load_app(arg):
    app = QApplication()
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    app.setPalette(palette)

    program_ui = SimpleComicViewer(arg)
    app_width, app_height = GetSetting.app_size()
    program_ui.resize(app_width, app_height)
    program_ui.setWindowIcon(QIcon(_ICON_MAIN))
    program_ui.show()

    app.exec()


def check_software_is_running():
    """使用互斥体检查是否已经打开了一个实例"""
    mutex_name = 'SimpleComicViewer'
    mutex = ctypes.windll.kernel32.CreateMutexW(None, False, mutex_name)
    if ctypes.windll.kernel32.GetLastError() == 183:  # ERROR_ALREADY_EXISTS
        ctypes.windll.kernel32.CloseHandle(mutex)
        return True
    return False


def send_data_to_host(data):
    """向指定本地端口发送数据"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (_HOST, _PORT)
    sock.connect(server_address)

    try:
        # 发送数据
        serialized_data = pickle.dumps(data)
        sock.sendall(serialized_data)
    finally:
        # 关闭连接
        sock.close()


if __name__ == "__main__":
    try:
        args = sys.argv[1:]
    except IndexError:
        args = []

    if check_software_is_running():
        send_data_to_host(args)
        sys.exit(1)
    else:
        function_config_normal.create_default_config()
        load_app(args)
