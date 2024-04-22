from wtforms import SubmitField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class DeleteArticle(FlaskForm):
    article_id = HiddenField(validators=[DataRequired()])
    submit = SubmitField(label='删除')