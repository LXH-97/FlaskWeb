
# 关注关联表的模型实现
class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Ingeter, db.ForeignKey('users.id'),
                            primary_key=True)
    followed_id = db.Column(db.Ingeter, db.ForeignKey('users.id'),
                            primary_key=True)

    timestamp = db.Column(db.Datetime, default=datetime.utcnow)

    comments = db.relationship('Comment', backref='author', lazy='dynamic')


# 使用两个一对多关系实现的多对多关系
class User(UserMixin, db.Model):
    followed = db.relationship('Follow',
                               foreign_keys=[Follow.follower_id],
                               backref=db.backref('follower', lazy='joined'),
                               lazy='dynamic',
                               cascade='all, delete-orphan')
    followers = db.relationship('Follow',
                                foreign_keys=[Follow.follower_id],
                                backref=db.backref('follower', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')


# users和posts表与comments表之间的一对多的关系
class User(db.Model):
    # ...
    comments = db.relationship('Comment', backref='authors', lazy='dynamic')

class Post(db.Model):
    # ...
    comments = db.relationship('Comment', backref='post', lazy='dynamic')


