from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Interval
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.sql.expression import bindparam
from sqlalchemy_serializer import SerializerMixin
from datetime import timedelta, datetime

def next_week():
    return datetime.utcnow() + timedelta(days=7)

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    number_of_pages = db.Column(db.Integer)

    # add relationship

    # add serialization rules

    def __repr__(self):
        return f'<Book {self.id} {self.title} {self.author} {self.number_or_pages}>'


class Member(db.Model, SerializerMixin):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    year_joined = db.Column(db.String)

    # add relationship
    
    # add serialization rules

    def __repr__(self):
        return f'<Member {self.id} {self.name} {self.year_joined}>'


class Loan(db.Model, SerializerMixin):
    __tablename__ = 'loans'

    id = db.Column(db.Integer, primary_key=True)
    check_out_date = db.Column(db.DateTime, server_default=db.func.now())
    due_date = db.Column(db.DateTime, default=next_week)

    # add relationship

    # add serialization rules

    def __repr__(self):
        return f'<Loan {self.id} {self.check_out_date} {self.due_date}>'