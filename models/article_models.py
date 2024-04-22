from datetime import datetime

from route import db
from sqlalchemy import Integer, String, TIMESTAMP, BLOB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class Article(db.Model):
    __tablename__ = 'article'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    # title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    __content: Mapped[bytes] = mapped_column(BLOB, nullable=False, name='content')
    update_time: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)

    @property
    def content(self):
        return self.__content.decode('utf-8')

    @content.setter
    def content(self, value: str):
        self.__content = value.encode()

    @property
    def short_content(self):
        short_article = self.__content.decode('utf-8')
        if len(short_article) > 150:
            return short_article[:150] + '……'
        else:
            return self.__content.decode('utf-8')
