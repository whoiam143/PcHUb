import sqlalchemy
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import orm


class Configuration(SqlAlchemyBase):
    __tablename__ = 'configurations'


    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    #Кулер
    cooler = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    cooler_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    #Корпус
    frame = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    frame_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    #SSD
    ssd = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ssd_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    #Процессор
    cpu = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    cpu_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    #Блок питания
    power = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    power_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    #Материнская плата
    motherboard = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    motherboard_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    #Видео карта
    gpu = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    gpu_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    #Оперативная памаять
    ram = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ram_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    #Коментарий к сборке
    comment = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))

    user = orm.relationship('User')