import uuid
from . import user_api
from flask_restplus import fields

user_model = user_api.model(
    'UserModel', {
        'user_id': fields.String(readOnly=True, description='The user unique identifier'),
        'username': fields.String(required=True, description='The user nickname'),
    })
user_list_model = user_api.model('UserListModel', {
    'users': fields.List(fields.Nested(user_model)),
    'total': fields.Integer,
})


class User(object):
    user_id = None
    username = None

    def __init__(self, username: str):
        self.user_id = str(uuid.uuid4())
        self.username = username
