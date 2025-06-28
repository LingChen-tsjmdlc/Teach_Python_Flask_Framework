# 一，填空题
# 在Flask中，获取POST请求的JSON数据使用的方法是 _______.get_json()。
# 在上课时候的示例代码中，GET 请求返回数据时使用的 Flask 函数是 _______。
# 在上课时候的示例代码中，更新图书信息时使用的 HTTP 方法是 _______。
# 当找不到要删除的资源时，通常返回的状态码是 _______。


# 二，实践题：用户收藏API
# 创建一个用户收藏文章的API，包含以下功能：
#
# GET /favorites - 获取所有收藏
# POST /favorites - 添加新收藏
# DELETE /favorites/<int:fav_id> - 删除收藏
# PUT /favorites/<int:fav_id> - 更新收藏信息
# 备注：收藏数据的字段如下: {"id": 唯一 ID 号, "user_id": 用户 ID 号, "article_id": 作者 ID 号, "note": "收藏内容"}
