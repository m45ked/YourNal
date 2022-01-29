from flask_app.db import db


class CampaignBO(db.Model):
    __tablename__ = 'campaigns'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    desc = db.Column(db.String)
    sessions = db.relationship('SessionBO', back_populates='campaign')


class UserBO(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    gm_sessions = db.relationship('SessionBO', back_populates='gm')


class SessionBO(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    playing_date = db.Column(db.Date, nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    campaign = db.relationship('CampaignBO', back_populates='sessions')
    gm_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    gm = db.relationship('UserBO', back_populates='gm_sessions')
