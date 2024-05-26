# 监听本地端口的子线程
import pickle
import socket

from PySide6.QtCore import QThread, Signal

from constant import _HOST, _PORT


class ThreadListenSocket(QThread):
    """监听本地端口的子线程"""
    signal_args = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((_HOST, _PORT))
        sock.listen(2)  # 最多允许2个客户端同时连接
        while True:
            connection, client_address = sock.accept()
            try:
                # 接收数据
                data = connection.recv(1024)
                if data:
                    args = pickle.loads(data)
                    # 打印接收到的参数
                    self.signal_args.emit(args)
            finally:
                # 关闭连接
                connection.close()
