"""桌面壳入口，用 pywebview 启动本地记账应用。"""

import socket
import sys
import threading
import time
import urllib.request
from typing import Optional

import webview

from app import app, socketio

HOST = "127.0.0.1"
WINDOW_TITLE = "个人记账系统 Pro"


def get_free_port() -> int:
    """获取本机可用端口，供内嵌 Web 服务使用。"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, 0))
        return s.getsockname()[1]


def wait_for_server(port: int, timeout: float = 8.0) -> bool:
    """轮询检查后端服务是否已经可访问。"""
    url = f"http://{HOST}:{port}/"
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            with urllib.request.urlopen(url) as response:
                if response.getcode() == 200:
                    return True
        except Exception:
            time.sleep(0.1)
    return False


def start_server(port: int):
    """在后台线程中启动 Flask-SocketIO 服务。"""
    socketio.run(
        app,
        host=HOST,
        port=port,
        debug=False,
        use_reloader=False,
        allow_unsafe_werkzeug=True,
    )


def main() -> Optional[int]:
    """启动本地服务并创建桌面窗口。"""
    port = get_free_port()
    url = f"http://{HOST}:{port}/"
    print(f"系统启动中... {url}")

    t = threading.Thread(target=start_server, args=(port,), daemon=True)
    t.start()

    if not wait_for_server(port):
        print("错误：后端服务器启动超时。")
        return 1

    webview.create_window(
        title=WINDOW_TITLE,
        url=url,
        width=1600,
        height=900,
        min_size=(1024, 768),
        resizable=True,
        confirm_close=True,
        text_select=False,
    )

    webview.start(private_mode=False, storage_path=None)
    return None


if __name__ == "__main__":
    sys.exit(main())
