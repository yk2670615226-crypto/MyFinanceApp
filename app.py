"""开发模式下的 Web 入口。"""

from webapp import create_app, socketio

app = create_app()


if __name__ == "__main__":
    """直接运行时，使用本地回环地址启动调试服务器。"""
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
