from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


# 加载用户的回调函数
@login_manager.user_loder
def load_user(user_id):
    return User.query.get(int(user_id))


# 修改User模型， 支持用户登陆
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Interger, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Interger, db.ForeignKey('role.id'))


    """
    # ..
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    """
