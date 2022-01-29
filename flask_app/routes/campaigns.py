from flask import render_template, request, redirect, url_for

from flask_app import app
from flask_app.db import db
from flask_app.ent import CampaignBO
from flask_app.forms import CampaignCreationForm, CampaignEditionForm


@app.route("/campaigns")
def show_campaigns():
    return render_template('campaigns/campaigns.html', campaigns=CampaignBO.query.all())


@app.route('/campaign/create', methods=['POST', 'GET'])
def create_campaign():
    form = CampaignCreationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            db.session.add(CampaignBO(name=form.name.data, desc=form.desc.data))
            db.session.commit()
        return redirect(url_for('show_campaigns'))
    else:
        return render_template('campaigns/create.html', form=form)


@app.route('/campaign/delete/<campaign_id>')
def delete_campaign(campaign_id):
    campaign = CampaignBO.query.filter_by(id=campaign_id).first()
    db.session.delete(campaign)
    db.session.commit()
    return redirect(url_for('show_campaigns'))


@app.route('/campaign/update/<campaign_id>')
def update_campaign(campaign_id):
    campaign = CampaignBO.query.filter_by(id=campaign_id).first()
    if campaign is None:
        return redirect(url_for('show_campaigns'))

    form = CampaignEditionForm()
    form.name.data = campaign.name
    form.desc.data = campaign.desc
    form.id.data = campaign_id
    return render_template('campaigns/update.html', form=form, campaign_id=campaign_id)


@app.route('/campaign/update/action/<campaign_id>', methods=['POST'])
def update_campaign_action(campaign_id):
    campaign = CampaignBO.query.filter_by(id=campaign_id).first()
    form = CampaignEditionForm()
    campaign.name = form.name.data
    campaign.desc = form.desc.data

    db.session.commit()

    return redirect(url_for('show_campaigns'))

