from flask_wtf import CSRFProtect
from configparser import ConfigParser
from flask import send_from_directory, render_template

from flask_app import app
from flask_app.db import db
from flask_app.ent import CampaignBO
from flask_app.routes.users import show_users, create_user, update_user, update_user_action, delete_user
from flask_app.routes.campaigns import update_campaign, show_campaigns, update_campaign_action, create_campaign, \
    delete_campaign
from flask_app.routes.sessions import show_sessions, create_session


csrf = CSRFProtect()


@app.route('/')
@app.route('/index')
def index():
    db.create_all()
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    import os
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    config = ConfigParser()

    from os.path import exists
    if exists('config/yournal.properties'):
        config.read('./config/yournal.properties')

    debug = False
    if config.has_section('DEVELOPMENT'):
        dev_config = config['DEVELOPMENT']
        if dev_config.getboolean('debug'):
            debug = True
        if dev_config.getboolean('echo_sql'):
            app.config['SQLALCHEMY_ECHO'] = True
    if config.has_section('DATABASE'):
        db_path = config['DATABASE'].get('path')
        if db_path:
            app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

    db.init_app(app=app)
    app.run(debug=debug)
