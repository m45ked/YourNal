from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, EqualTo, Length

from sqlalchemy import create_engine, select, insert
from flask import Flask, url_for, request, session, render_template, redirect, flash, send_from_directory

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///e:/database.db3"
app.config['SECRET_KEY'] = 'very simple secret key'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class UserCreationForm(FlaskForm):
    name = StringField(label='name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo(fieldname='confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm password')


class UserEditionForm(UserCreationForm):
    id = HiddenField(label='id')


class CampaignCreationForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(), Length(min=6, max=35)])
    desc = TextAreaField(label='Description', validators=[Length(max=150), DataRequired()])


class CampaignEditionForm(CampaignCreationForm):
    id = HiddenField(label='id')


class CampaignBO(db.Model):
    __tablename__ = 'campaigns'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    desc = db.Column(db.String)


class UserBO(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


@app.route('/')
@app.route('/index')
def index():
    db.create_all()
    return render_template('index.html')


@app.route("/users")
def show_users():
    users = UserBO.query.all()
    return render_template('users.html', users=users)


@app.route("/campaigns")
def show_campaigns():
    return render_template('campaigns.html', campaigns=CampaignBO.query.all())


@app.route('/create_user', methods=['POST', 'GET'])
def create_user():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            user = UserBO(name=form.name.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()

    return render_template('create_user.html', form=UserCreationForm())


@app.route('/create_campaign', methods=['POST', 'GET'])
def create_campaign():
    form = CampaignCreationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            db.session.add(CampaignBO(name=form.name.data, desc=form.desc.data))
            db.session.commit()
        return redirect(url_for('show_campaigns'))
    else:
        return render_template('create_campaign.html', form=form)


@app.route('/delete_campaign/<campaign_id>')
def delete_campaign(campaign_id):
    campaign = CampaignBO.query.filter_by(id=campaign_id).first()
    db.session.delete(campaign)
    db.session.commit()
    return redirect(url_for('show_campaigns'))


@app.route('/update_campaign/<campaign_id>')
def update_campaign(campaign_id):
    campaign = CampaignBO.query.filter_by(id=campaign_id).first()
    if campaign is None:
        return redirect(url_for('show_campaigns'))

    form = CampaignEditionForm()
    form.name.data = campaign.name
    form.desc.data = campaign.desc
    form.id.data = campaign_id
    return render_template('update_campaign.html', form=form, campaign_id=campaign_id)


@app.route('/update_campaign_action/<campaign_id>', methods=['POST'])
def update_campaign_action(campaign_id):
    campaign = CampaignBO.query.filter_by(id=campaign_id).first()
    form = CampaignEditionForm()
    campaign.name = form.name.data
    campaign.desc = form.desc.data

    db.session.commit()

    return redirect(url_for('show_campaigns'))


@app.route('/favicon.ico')
def favicon():
    import os
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=True)