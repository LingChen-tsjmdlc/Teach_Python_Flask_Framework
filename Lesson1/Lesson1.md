# 请求方式
> 常用的：get，post，put，delete

## 基础概念：
1. GET：获取资源
2. POST：创建资源
3. PUT：更新资源
4. DELETE：删除资源

## GET 请求
```python
from flask import Flask, jsonify
app = Flask(__name__)

books = [
    {"id": 1, "title": "书名1", "author": "张三"},
    {"id": 2, "title": "书名2", "author": "李四"},
]

@app.route('/book', methods=['GET'])
def get_books():
    return jsonify(books)
```

## POST 请求
```python
from flask import Flask, jsonify, request
app = Flask(__name__)

books = [
    {"id": 1, "title": "书名1", "author": "张三"},
    {"id": 2, "title": "书名2", "author": "李四"},
]

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
```


## PUT 请求
```python
from flask import Flask, jsonify, request
app = Flask(__name__)

books = [
    {"id": 1, "title": "书名1", "author": "张三"},
    {"id": 2, "title": "书名2", "author": "李四"},
]

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
```

## DELETE 请求
```python
from flask import Flask, jsonify, request
app = Flask(__name__)

books = [
    {"id": 1, "title": "书名1", "author": "张三"},
    {"id": 2, "title": "书名2", "author": "李四"},
]

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
```