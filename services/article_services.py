from sqlalchemy import Select, Update, func, and_, Delete
from models.article_models import Article

from route import db


class ArticleServers:

    def get_article(self, article_id):
        return db.session.get(Article, article_id)

    def get_articles(self):
        query = Select(Article)
        return db.session.scalars(query)

    def create_article(self, article: Article):
        query = Article.query.where(Article.title == article.title)
        assert not db.session.scalar(query), '该文章标题已经存在'

        db.session.add(article)
        return db.session.commit()

    def edit_article(self, article_id, form):
        exist_article = Article.query.get(article_id)
        assert exist_article, '该文章不存在，修改失败'

        query = Select(Article).where(and_(Article.id != article_id, Article.title == form.title.data))
        assert not db.session.scalars(query).all(), '该文章标题已存在，不允许标题重复'

        exist_article.title = form.title.data
        exist_article.content = form.content.data
        exist_article.update_time = func.now()

        db.session.commit()
        return exist_article

    def delete_article(self, article_id):
        article = db.session.get(Article, article_id)

        if article:
            db.session.delete(article)
            db.session.commit()
            return 'success', '删除成功'
        else:
            return 'danger', '错误，找不到需要删除的文章'