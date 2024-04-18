import sqlalchemy
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import orm


class Configuration(SqlAlchemyBase):
    __tablename__ = 'configurations'


    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    #Кулер
    cooler = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    cooler_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cooler_price = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    #Корпус
    frame = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    frame_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    frame_price = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    #SSD
    ssd = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ssd_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ssd_price = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    #Процессор
    cpu = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    cpu_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cpu_price = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    #Блок питания
    power = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    power_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    power_price = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    #Материнская плата
    motherboard = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    motherboard_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    motherboard_price = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    #Видео карта
    gpu = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    gpu_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    gpu_price = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    #Оперативная памаять
    ram = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ram_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ram_price = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    #Коментарий к сборке
    comment = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    
    total_price = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    user = orm.relationship('User')
    
    def all(self):
        return {
                'name': self.name, 
                'about': self.about, 
                'cooler': self.cooler, 
                'cooler_link': self.cooler_link,
                'cooler_price': self.cooler_price, 
                'frame': self.frame, 
                'frame_link': self.frame_link,
                'frame_price': self.frame_price,
                'ssd': self.ssd, 
                'ssd_link': self.ssd_link, 
                'ssd_price': self.ssd_price, 
                'cpu': self.cpu, 
                'cpu_link': self.cpu_link, 
                'cpu_price': self.cpu_price, 
                'power': self.power, 
                'power_link': self.power_link,
                'power_price': self.power_price,
                'motherboard': self.motherboard, 
                'motherboard_link': self.motherboard_link, 
                'motherboard_price': self.motherboard_price,
                'gpu': self.gpu, 
                'gpu_link': self.gpu_link, 
                'gpu_price': self.gpu_price,
                'ram': self.ram, 
                'ram_link': self.ram_link, 
                'ram_price': self.ram_price,
                'comment': self.comment, 
                'user_id': self.user_id
                }