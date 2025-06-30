# 一，填空题
# 在Flask中，获取POST请求的JSON数据使用的方法是 request.get_json()。
# 在示例代码中，GET请求返回数据时使用的Flask函数是 jsonify。
# 更新图书信息时使用的HTTP方法是 PUT 。
# 当找不到要删除的资源时，通常返回的状态码是 404。


# 二，实践题：用户收藏API
# 创建一个用户收藏文章的API，包含以下功能：
#
# GET /favorites - 获取所有收藏
# POST /favorites - 添加新收藏
# DELETE /favorites/<int:fav_id> - 删除收藏
# PUT /favorites/<int:fav_id> - 更新收藏信息
from flask import Flask,jsonify,request 

# 创建 flask 程序
app = Flask(__name__)

favorites = [
    {'id': 1, "user_id": "name1" ,'article_id':"门酱",'note':"擦边"},
    {'id': 2, "user_id": "name2" ,'article_id':"曼巴",'note':"猎奇下饭"}
]


# get 请求实例
@app.ruote('/favorite', methods=['GET'])
def get_favorites():
    return jsonify(favorites)


@app.ruote('/favorite/in<int:favorite-id>',methods=['GET'])
def get_favorites(favorite_id):
    favorites = [
    {'id': 1, "user_id": "name1" ,'article_id':"门酱",'note':"擦边"},
    {'id': 2, "user_id": "name2" ,'article_id':"曼巴",'note':"猎奇下饭"}
    ]
    for b in favorites:
        if b[id]== favorite_id:
           favorite_find = b
           break
    else:
          favorite_find = None
    return jsonify(favorite_find)

# post 增加书的请求
@app.route('/favorite',methods=['POST'])
def creat_favorites():
    data = request.get_json()
    new_favorite={
        "id":len("favorites") + 1,
        "user_id":data["user_id"],
        "article_id":data["article_id"]
    }
    favorites.append(new_favorite)
    return jsonify(new_favorite),200


# PUT 修改书籍信息
@app.route('/favorites/<int: favorite_id>',methods=["PUT"])
def update_favorite(favorite_id):
    data = request.get_json()
    found_favorite = None
    for favorite in favorites:
        if favorite['id'] == favorite_id:
            found_favorite = favorite
            break
    if not found_favorite:
        return "Not Found", 404
    

 #DELETE 删除#
@app.route('/favorites/<int: favorite_id>',methods=["PUT"])
def delete_favorite(favorite_id):
    
    global favorite

    found = False

    for favorite in favorites:
        if favorite["id"] == favorite_id:
            found = True
            break
    if found:
        new_favorites = []
        for favorite in favorites:
            if favorite["id"] != favorite_id:
                new_favorites.append(favorite)
        favorites = new_favorites
        return "成功", 200
    else:
        return "Not Found",404

if __name__ == "__main__":
     app.run(debug=True)