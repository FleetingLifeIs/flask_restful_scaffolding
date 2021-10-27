from flask import request
from flask_restplus import Resource
from . import user_api
from .models import user_model, user_list_model


class Servers(Resource):

    def get(self):
        # 返回所有数据
        return "this is data list"

    def post(self):
        # 新增数据
        data = request.get_json()
        return "add new data: %s" % data


class Server(Resource):

    def get(self, _id):
        # 返回单条数据
        return "this data is %s" % _id

    def delete(self, _id):
        # 删除单条数据
        return "delete data: %s" % _id

    def put(self, _id):
        # 修改单条数据
        data = request.get_json()
        return "put data %s: %s" % (_id, data)


class DemoView(Resource):

    def get(self):
        return {"message": "get"}

    def post(self):
        return {"message": "post"}


class UserListApi(Resource):
    # 初始化数据
    users = [""]

    @user_api.doc('get_user_list')
    @user_api.marshal_with(user_list_model)
    def get(self):
        return {
            "users": self.users,
            "total": len(self.users),
        }

    @user_api.doc('create_user')
    @user_api.expect(user_model)
    @user_api.marshal_with(user_model, code=201)
    def post(self):
        user = "insert a user"
        return user
