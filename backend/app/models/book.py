from datetime import datetime
from app.database import db


class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    title = db.Column("title", db.String)
    author = db.Column("author", db.String)
    read = db.Column("read", db.Boolean)
    created_at = db.Column("created_at", db.DateTime)
    
    def __init__(self, title, author, read=False):
        self.title = title
        self.author = author
        self.read = read
        self.created_at = datetime.now()
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "read": self.read,
            "created_at": self.created_at.strftime('%d/%m/%Y %H:%M:%S') if self.created_at else None
        }
        