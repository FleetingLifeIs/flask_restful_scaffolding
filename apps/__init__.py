from flask import Flask, Blueprint
from flask_restplus import Api

import yaml
import os

blueprint = Blueprint("open_api", __name__, url_prefix="/open_api")
api = Api(blueprint)


def register_api():
    from apps.users.views import DemoView, Servers, Server, UserListApi
    from apps.users import user_api
    api.add_resource(DemoView, "/home")
    user_api.add_resource(Servers, "/servers")
    user_api.add_resource(Server, "/servers/<_id>")
    user_api.add_resource(UserListApi, "/user/<_id>")


def read_yaml(config_name, config_path):
    """
    config_name:需要读取的配置内容
    config_path:配置文件路径
    """
    if config_name and config_path:
        with open(config_path, 'r', encoding='utf-8') as f:
            conf = yaml.safe_load(f.read())
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            raise KeyError('未找到对应的配置信息')
    else:
        raise ValueError('请输入正确的配置名称或配置文件路径')


def create_app(config_name=None, config_path=None):
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.register_blueprint(blueprint)
    register_api()
    # # 读取配置文件
    if not config_path:
        pwd = os.getcwd()
        config_path = os.path.join(pwd, 'config/config.yaml')
    if not config_name:
        config_name = 'PRODUCTION'

    # 读取配置文件
    conf = read_yaml(config_name, config_path)
    app.config.update(conf)

    return app
