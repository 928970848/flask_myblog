from flask_login import logout_user, current_user
import bcrypt
from route import app
from flask import render_template, url_for, abort, flash, redirect
from services.article_services import ArticleServers
from forms.user_forms import LoginForm
from forms.delete_article_form import DeleteArticle
from services.user_services import UserServers


@app.route('/', methods=['POST', 'GET'])
@app.route('/index.html', methods=['POST', 'GET'])
def home_page():
    articles = ArticleServers().get_articles()

    if current_user.is_authenticated:
        delete_article_form = DeleteArticle()
        if delete_article_form.validate_on_submit():
            article_id = delete_article_form.article_id.data
            status, message = ArticleServers().delete_article(int(article_id))
            flash(message=message, category=status)
            return redirect(url_for('home_page'))
        else:
            return render_template('index.html', articles=articles, delete_article_form=delete_article_form)

    return render_template('index.html', articles=articles)


@app.route('/about.html')
def about_page():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # form
    if form.validate_on_submit():
        if UserServers().do_login(username=form.username.data, password=form.password.data):
            flash(f'欢迎登录{form.username.data}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash(f'账号或密码错误,请重试', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route("/article/<article_id>", methods=['GET', 'POST'])
def article_page(article_id):
    article = ArticleServers().get_article(article_id)
    if article:
        return render_template('article.html', article=article)
    abort(404)
