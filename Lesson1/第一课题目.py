# 一，填空题
# 在Flask中，获取POST请求的JSON数据使用的方法是 ___request____.get_json()。
# 在上课时候的示例代码中，GET 请求返回数据时使用的 Flask 函数是 ___jsonify()____。
# 在上课时候的示例代码中，更新图书信息时使用的 HTTP 方法是 ___PUT___。
# 当找不到要删除的资源时，通常返回的状态码是 ____404___。


# 二，实践题：用户收藏API
# 创建一个用户收藏文章的API，包含以下功能：
#
# GET /favorites - 获取所有收藏
# POST /favorites - 添加新收藏
# DELETE /favorites/<int:fav_id> - 删除收藏
# PUT /favorites/<int:fav_id> - 更新收藏信息
# 备注：收藏数据的字段如下: {"id": 唯一 ID 号, "user_id": 用户 ID 号, "article_id": 作者 ID 号, "note": "收藏内容"}

#导入Flask的包
from flask import Flask, jsonify, request

#创建Flask的程序
app = Flask(__name__)

#创建列表字典
favorites = [
    {'id':1,'user_id':11,'article_id':111,'note':'test1'},
    {'id':2,'user_id':22,'article_id':222,'note':'test2'},
]


#创建路由
@app.route('/')
def home():
    return "<h1>Hello,Word!!!<h1>"


#使用GET获取所有收藏
@app.route('/favorite',methods=['GET'])
def get_favorites():
    return jsonify(favorites)


#通过动态路由使用GET查找特定的收藏
@app.route('/favorite/<int:favorite_id>',methods=['GET'])
def get_favorite(favorite_id):
    global favorites
    for f in favorites:
        if f['id'] == favorite_id:
            favorite_find = f
            break
        else:
            favorite_find = None
    return jsonify(favorite_find)


#使用POST添加新的收藏
@app.route('/favorite',methods=['POST'])
def add_favorite():
    data = request.get_json()
    new_favorite = {
        "id":len(favorites) + 1,
        "user_id":data['user_id'],
        "article_id":data['article_id'],
        "note":data['note'],
    }
    favorites.append(new_favorite)
    return jsonify(new_favorite),200

#使用DELETE删除收藏
@app.route('/favorite/<int:favorite_id>',methods=['DELETE'])
def delete_favorite(favorite_id):
    global favorites
    found = False
    for f in favorites:
        if f['id'] == favorite_id:
            found = True
            break
    if found:
        new_favorites = []
        for f in favorites:
            if f['id'] != favorite_id:
                new_favorites.append(f)
        favorites = new_favorites
        return "删除成功",200
    else:
        return "Not Found",404


#使用PUT修改收藏信息
@app.route('/favorite/<int:favorite_id>',methods=['PUT'])
def update_favorite(favorite_id):
    data = request.get_json()
    found_favorite = None
    for f in favorites:
        if f['id'] == favorite_id:
            found_favorite = f
            break
    if not found_favorite:
        return "Not Found",404

    found_favorite['user_id'] = data['user_id']
    found_favorite['article_id'] = data['article_id']
    found_favorite['note'] = data['note']

    return jsonify(found_favorite)


if __name__ == "__main__":
    app.run(debug=True)





