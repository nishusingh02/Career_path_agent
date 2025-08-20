from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    role = db.Column(db.String(100))
    department = db.Column(db.String(100))
    experience = db.Column(db.Integer)
    career_goal = db.Column(db.String(200))
    performance_rating = db.Column(db.Float)
    feedback = db.Column(db.String(500))