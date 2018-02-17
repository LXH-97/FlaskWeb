from flask import Flask

# 创建蓝本
main = Blueprint('main', __name__)

from . import views, errors


# 把Permission类加入模板上下文
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)