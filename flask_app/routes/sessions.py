from flask import render_template, request, redirect, url_for

from flask_app import app
from flask_app.db import db
from flask_app.ent import CampaignBO, UserBO, SessionBO
from flask_app.forms import SessionCreationForm, SessionEditionForm


@app.route('/sessions/<campaign_id>')
def show_sessions(campaign_id):
    sessions = SessionBO.query.filter_by(campaign_id=campaign_id).order_by(SessionBO.playing_date).all()
    data = [{"session": session, "no": i+1} for i, session in enumerate(sessions)]
    return render_template('sessions/sessions.html', data=data,
                           campaign=CampaignBO.query.filter_by(id=campaign_id).first())


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
    form.campaign_id = campaign_id
    return render_template('sessions/create.html', campaign=campaign, form=form)


@app.route('/sessions/delete/<session_id>')
def delete_session(session_id):
    s = SessionBO.query.filter_by(id=session_id).first()
    campaign_id = s.campaign_id
    db.session.delete(s)
    db.session.commit()

    return redirect(url_for('show_sessions', campaign_id=campaign_id))


@app.route('/sessions/update/<session_id>')
def update_session(session_id):
    session = SessionBO.query.filter_by(id=session_id).first()
    if session is None:
        return redirect(url_for('show_campaigns'))

    form = SessionEditionForm()
    form.campaign_id.data = session.campaign_id
    form.gm.choices = [(i.id, i.name) for i in UserBO.query.all()]
    form.gm.data = session.gm_id
    form.id.data = session_id
    form.playing_date.data = session.playing_date

    return render_template('sessions/update.html', form=form)


@app.route('/sessions/update/action/<session_id>', methods=['POST'])
def update_session_action(session_id):
    session = SessionBO.query.filter_by(id=session_id).first()
    campaign_id = session.campaign_id
    form = SessionEditionForm()
    session.playing_date = form.playing_date.data
    session.gm_id = form.gm.data

    db.session.commit()

    return redirect(url_for('show_sessions', campaign_id=campaign_id))
