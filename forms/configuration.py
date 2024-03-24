from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField, URLField
from wtforms.validators import DataRequired


class AddConfigurationForm(FlaskForm):
    name = StringField("Название сборки", validators=[DataRequired()], render_kw={"placeholder": 'Имя сборки'})
    
    cpu = StringField('Процессор', validators=[DataRequired()], render_kw={"placeholder": 'Название процессора'})
    cpu_link = URLField('', render_kw={"placeholder": 'Ссылка на процессор'})

    gpu = StringField('Видеокарта', validators=[DataRequired()], render_kw={"placeholder": 'Название видео карты'})
    gpu_link = URLField('', render_kw={"placeholder": 'Ссылка на видео карту'})

    ram = StringField('Оперативная память', validators=[DataRequired()], render_kw={"placeholder": 'Название опративной памяти'})
    ram_link = URLField('', render_kw={"placeholder": 'Ссылка на опертивную память'})
     
    motherboard = StringField('Материнская плата', validators=[DataRequired()], render_kw={"placeholder": 'Название материнской платы'})
    motherboard_link = URLField('', render_kw={"placeholder": 'Ссылка на материнскую плату'})

    ssd = StringField('Накопитель', validators=[DataRequired()], render_kw={"placeholder": 'Название накопителя'})
    ssd_link = URLField('', render_kw={"placeholder": 'Ссылка на накопитель'})

    frame = StringField('Корпус', validators=[DataRequired()], render_kw={"placeholder": 'Название корпуса'})
    frame_link = URLField('', render_kw={"placeholder": 'Ссылка на корпус'})

    cooler = StringField('Кулер', validators=[DataRequired()], render_kw={"placeholder": 'Название куллера'})
    cooler_link = URLField('', render_kw={"placeholder": 'Ссылка на куллеры'})

    power = StringField('Блок питания', validators=[DataRequired()], render_kw={"placeholder": 'Название блока питания'})
    power_link = URLField('', render_kw={"placeholder": 'Ссылка на блок питания'})

    comment = TextAreaField('Коментарий', render_kw={'style': 'min-height: 150px',
                                                              "placeholder": 'Напишите коментарий к сборке пк'})

    submit = SubmitField('Отправить')
