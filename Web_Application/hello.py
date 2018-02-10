from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap  import Bootstrap
from flask_moment import Moment
from datetime import datetime
moment = Moment(app)

bootstrap = Bootstrap(app)

manager = Manager(app)


app = Flask(__name__)

"""
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
"""


@app.route('/')
def index():
    return render_template('index.html')

# 加入一个datatime变量
@app.route('/')
def index():
    return render_template('index.html',current_time=datatime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



if __name__ == '__main__':
    manager.run()