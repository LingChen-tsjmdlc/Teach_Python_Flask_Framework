# 导入 flask 包
from flask import Flask, jsonify, request

# 创建 flask 程序
app = Flask(__name__)

books = [
    {"id": 1, "title": "书名1", "author": "张三"},
    {"id": 2, "title": "书名2", "author": "李四"},
]


# 创建路由
@app.route('/')
def home():
    return "<h1>Hello Word!</h1>"


# get 请求实例
@app.route('/book', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    books = [
        {"id": 1, "title": "书名1", "author": "张三"},
        {"id": 2, "title": "书名2", "author": "李四"},
    ]
    for b in books:
        if b["id"] == book_id:
            book_find = b
            break
    else:
        book_find = None
    return jsonify(book_find)


# post 增加书的请求
@app.route('/book', methods=['POST'])
def creat_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data['title'],
        "author": data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 200


# PUT 修改书籍信息
@app.route('/book/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    found_book = None
    for book in books:
        if book["id"] == book_id:
            found_book = book
            break
    if not found_book:
        return 'Not Found', 404

    found_book['title'] = data['title']
    found_book['author'] = data['author']

    return jsonify(found_book)

@app.route('/book/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    # 使用全局的 books 变量
    global books

    found = False

    for book in books:
        if book["id"] == book_id:
            found = True
            break
    if found:
        new_books = []
        for book in books:
            if book['id'] != book_id:
                new_books.append(book)
        books = new_books
        return "成功",200
    else:
        return 'Not Found', 404

if __name__ == "__main__":
    app.run(debug=True)
