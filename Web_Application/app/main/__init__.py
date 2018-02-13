from flask import Flask

# 创建蓝本
main = Blueprint('main', __name__)

from . import views, errors