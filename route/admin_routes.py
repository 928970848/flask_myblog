from route import app
from flask_login import login_required
from forms.article_forms import ArticleForm
from flask import render_template, flash, url_for, redirect, request
from models.article_models import Article
from services.article_services import ArticleServers


@app.route('/create_article', methods=['POST', 'GET'])
@login_required
def create_article():
    form = ArticleForm()
    if form.validate_on_submit():
        new_article = Article()
        new_article.title = form.title.data
        new_article.content = form.content.data
        try:
            ArticleServers().create_article(new_article)
            flash('添加文章成功,', category='success')
            return redirect('/index.html')
        except Exception as error:
            flash(f'添加文章失败,{error}', category='danger')

    return render_template('createarticle.html', form=form, is_edit=False)


@app.route('/edit_article/<article_id>', methods=['POST', 'GET'])
@login_required
def edit_article(article_id: str):
    form = ArticleForm()
    if request.method == 'GET':
        try:
            article = ArticleServers().get_article(int(article_id))
            if not article:
                flash('错误提示：要修改的文章不存在', category='danger')
                return redirect(url_for('home_page'))
            else:
                form.title.data = article.title
                form.content.data = article.content

        except Exception as e:
            flash('提取文章失败', category='danger')
            return redirect(url_for('home_page'))

    if form.validate_on_submit():
        try:
            article = ArticleServers().edit_article(int(article_id), form)
            flash('修改文章成功,', category='success')
            return redirect(f'/article/{article.id}')
        except Exception as error:
            flash(f'修改文章失败,{error}', category='danger')

    return render_template('createarticle.html', form=form, is_edit=True)