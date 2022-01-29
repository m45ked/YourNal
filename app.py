from flask_wtf import CSRFProtect
from configparser import ConfigParser
from flask import send_from_directory

from flask_app.routes.users import *
from flask_app.routes.campaigns import *


csrf = CSRFProtect()

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///e:/database.db3"
app.config['SECRET_KEY'] = 'very simple secret key'


@app.route('/')
@app.route('/index')
def index():
    db.create_all()
    return render_template('index.html')


@app.route('/sessions/<campaign_id>')
def show_sessions(campaign_id):
    sessions = CampaignBO.query.filter_by(id=campaign_id).all()
    return "sessions"


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

    app.run(debug=debug)
