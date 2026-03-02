from flask import Flask, send_file, send_from_directory
import webbrowser
import threading
import time
import os

app = Flask(__name__)

# 主页：返回 index.html
@app.route('/')
def index():
    return send_file('index.html')

# 静态资源：处理 css、js、img 文件夹的请求
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

# 启动本地服务器
def run_server():
    app.run(host='127.0.0.1', port=8080, debug=False)

# 自动打开浏览器
def open_browser():
    time.sleep(1.5)  # 给服务器多一点启动时间
    webbrowser.open('http://127.0.0.1:8080')

if __name__ == '__main__':
    threading.Thread(target=run_server).start()
    threading.Thread(target=open_browser).start()