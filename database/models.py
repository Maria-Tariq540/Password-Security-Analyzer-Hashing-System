from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    reports = db.relationship(
        "AnalysisReport",
        backref="user",
        lazy=True
    )


class AnalysisReport(db.Model):
    __tablename__ = "analysis_reports"

    id = db.Column(db.Integer, primary_key=True)

    password_length = db.Column(db.Integer)

    strength_score = db.Column(db.Integer)

    risk_level = db.Column(db.String(50))

    hash_type = db.Column(db.String(50))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )