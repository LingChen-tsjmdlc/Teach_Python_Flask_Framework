# 导入 flask 包
from flask import Flask

# 创建 flask 程序
app = Flask(__name__)


# 创建路由
@app.route('/')
def home():
    return "<h1>Hello Word!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
