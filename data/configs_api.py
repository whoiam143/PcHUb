from flask_restful import reqparse, abort, Api, Resource
from . import db_session
from .users import User
from flask import jsonify
from.configurations import Configuration


def abort_if_config_not_found(config_id):
    """
    Check if a configuration with the given ID exists. If not, abort with a 404 error.

    Args:
        config_id (int): The ID of the configuration to check.

    Returns:
        None

    Raises:
        HTTPError: If the configuration does not exist, abort with a 404 error.
    """
    session = db_session.create_session()
    config = session.query(Configuration).get(config_id)
    if not config:
        abort(404, message=f"Configuration {config_id} not found")
        
        
class ConfigurationList(Resource):
    def get(self):
        session = db_session.create_session()
        configs = session.query(Configuration).all()
        return jsonify(
            {
                'configs': [item.all() for item in configs]
            }
        )
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, type=str)
    parser.add_argument('about', required=True, type=str)
    parser.add_argument('cooler', required=True, type=str)
    parser.add_argument('cooler_link', required=False, type=str)
    parser.add_argument('cooler_price', required=True, type=str)
    parser.add_argument('frame', required=True, type=str)
    parser.add_argument('frame_link', required=False, type=str)
    parser.add_argument('frame_price', required=True, type=str)
    parser.add_argument('ssd', required=True, type=str)
    parser.add_argument('ssd_link', required=False, type=str)
    parser.add_argument('ssd_price', required=True, type=str)
    parser.add_argument('cpu', required=True, type=str)
    parser.add_argument('cpu_link', required=False, type=str)
    parser.add_argument('cpu_price', required=True, type=str)
    parser.add_argument('power', required=True, type=str)
    parser.add_argument('power_link', required=False, type=str)
    parser.add_argument('power_price', required=True, type=str)
    parser.add_argument('motherboard', required=True, type=str)
    parser.add_argument('motherboard_link', required=False, type=str)
    parser.add_argument('motherboard_price', required=True, type=str)
    parser.add_argument('gpu', required=True, type=str)
    parser.add_argument('gpu_link', required=False, type=str)
    parser.add_argument('gpu_price', required=True, type=str)
    parser.add_argument('ram', required=True, type=str)
    parser.add_argument('ram_link', required=False, type=str)
    parser.add_argument('ram_price', required=True, type=str)
    parser.add_argument('comment', required=False, type=str)


    def post(self):
        args = self.parser.parse_args()
        session = db_session.create_session()
        config = Configuration(
            name=args['name'],
            about=args['about'],
            cooler=args['cooler'],
            cooler_link=args['cooler_link'],
            cooler_price=args['cooler_price'],
            frame=args['frame'],
            frame_link=args['frame_link'],
            frame_price=args['frame_price'],
            ssd=args['ssd'],
            ssd_link=args['ssd_link'],
            ssd_price=args['ssd_price'],
            cpu=args['cpu'],
            cpu_link=args['cpu_link'],
            cpu_price=args['cpu_price'],
            power=args['power'],
            power_link=args['power_link'],
            power_price=args['power_price'],
            motherboard=args['motherboard'],
            motherboard_link=args['motherboard_link'],
            motherboard_price=args['motherboard_price'],
            gpu=args['gpu'],
            gpu_link=args['gpu_link'],
            gpu_price=args['gpu_price'],
            ram=args['ram'],
            ram_link=args['ram_link'],
            ram_price=args['ram_price'],
            comment=args['comment'],
        )
        session.add(config)
        session.commit()
        return 201
        
class ConfigurationResourse(Resource):
    def get(self, config_id):
        abort_if_config_not_found(config_id)
        session = db_session.create_session()
        config = session.query(Configuration).get(config_id)
        return jsonify(
            {
                'config': config.all()
            }
        )
    
    def delete(self, config_id):
        abort_if_config_not_found(config_id)
        session = db_session.create_session()
        config = session.query(Configuration).get(config_id)
        session.delete(config)
        session.commit()
        return 204