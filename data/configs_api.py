from flask_restful import reqparse, abort, Api, Resource
from . import db_session
from .users import User
from flask import jsonify
from.configurations import Configuration


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"User {user_id} not found")

        
parser = reqparse.RequestParser()
parser.add_argument('name', required=True, type=str)
parser.add_argument('about', required=True, type=str)
parser.add_argument('cooler', required=True, type=str)
parser.add_argument('cooler_link', required=False, type=str)
parser.add_argument('frame', required=True, type=str)
parser.add_argument('frame_link', required=False, type=str)
parser.add_argument('ssd', required=True, type=str)
parser.add_argument('ssd_link', required=False, type=str)
parser.add_argument('cpu', required=True, type=str)
parser.add_argument('cpu_link', required=False, type=str)
parser.add_argument('power', required=True, type=str)
parser.add_argument('power_link', required=False, type=str)
parser.add_argument('motherboard', required=True, type=str)
parser.add_argument('motherboard_link', required=False, type=str)
parser.add_argument('gpu', required=True, type=str)
parser.add_argument('gpu_link', required=False, type=str)
parser.add_argument('ram', required=True, type=str)
parser.add_argument('ram_link', required=False, type=str)
parser.add_argument('comment', required=False, type=str)



class ConfigurationList(Resource):
    def get(self):
        session = db_session.create_session()
        configs = session.query(Configuration).all()
        return jsonify(
            {
                'configs': [item.all() for item in configs]
            }
        )
    
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        
        