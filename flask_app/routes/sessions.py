from flask import render_template, request, redirect, url_for

from flask_app import app
from flask_app.db import db
from flask_app.ent import CampaignBO, UserBO, SessionBO
from flask_app.forms import SessionCreationForm


@app.route('/sessions/<campaign_id>')
def show_sessions(campaign_id):
    campaign = CampaignBO.query.filter_by(id=campaign_id).first()
    data = [{"session": session, "no": i+1} for i, session in enumerate(campaign.sessions)]
    return render_template('sessions/sessions.html', data=data, campaign=campaign)


@app.route('/sessions/create/<campaign_id>', methods=['POST', 'GET'])
def create_session(campaign_id):
    form = SessionCreationForm()
    form.gm.choices = [(i.id, i.name) for i in UserBO.query.all()]
    if request.method == 'POST':
        if form.validate_on_submit():
            session = SessionBO(campaign_id=campaign_id, gm_id=form.gm.data,
                                playing_date=form.playing_date.data)
            db.session.add(session)
            db.session.commit()

        return redirect(url_for('show_sessions', campaign_id=campaign_id))

    campaign = CampaignBO.query.filter_by(id=campaign_id).first()
    print(form.gm.choices)
    form.campaign_id = campaign_id
    return render_template('sessions/create.html', campaign=campaign, form=form)
