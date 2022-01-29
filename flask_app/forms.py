from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, EqualTo, Length


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
