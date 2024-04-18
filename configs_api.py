import flask
from flask import jsonify

import data.db_session 
from data.configurations import Configuration

blueprint = flask.Blueprint(
    'configs_api',
    __name__,
    template_folder='templates'
)

@blueprint.route('/api')
def get_configs():
    db_sess = data.db_session.create_session()
    configs = db_sess.query(Configuration).all()
    return jsonify(
        {
            'configs': [item.all() for item in configs]
        }
    )
    