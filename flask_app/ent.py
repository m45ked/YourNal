from flask_app import db


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


class SessionBO(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    campaign = db.relationship('CampaignBO', back_populates='sessions')
