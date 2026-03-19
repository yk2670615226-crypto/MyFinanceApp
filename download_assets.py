import os
import urllib.request

FILES = {
    "static/css/bootstrap.min.css": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
    "static/css/bootstrap-icons.min.css": "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
    "static/css/aos.css": "https://unpkg.com/aos@2.3.1/dist/aos.css",
    "static/css/fonts/bootstrap-icons.woff2": "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/fonts/bootstrap-icons.woff2",
    "static/css/fonts/bootstrap-icons.woff": "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/fonts/bootstrap-icons.woff",
    "static/js/bootstrap.bundle.min.js": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
    "static/js/aos.js": "https://unpkg.com/aos@2.3.1/dist/aos.js",
    "static/js/socket.io.min.js": "https://cdn.socket.io/4.7.4/socket.io.min.js",
    "static/js/echarts.min.js": "https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"
}

print("====== 开始构建纯本地化静态资源库 ======")
for local_path, url in FILES.items():
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    print(f"正在下载: {local_path}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
    except Exception as e:
        print(f"  [X] 下载失败: {e}")
print("====== 资源拉取完成！请检查根目录的 static 文件夹 ======")