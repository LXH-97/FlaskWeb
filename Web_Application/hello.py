from flask import Flask,render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap  import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
moment = Moment(app)

bootstrap = Bootstrap(app)

manager = Manager(app)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

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

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm
    if form.validate_on_submit():
        old_name = session.get('name')          # flash消息
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data        # 重定向和用户对话
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))



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

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')



if __name__ == '__main__':
    manager.run()