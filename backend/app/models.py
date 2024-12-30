from app import db

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_type = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
