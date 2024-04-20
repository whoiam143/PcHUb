from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField, URLField, IntegerField
from wtforms.validators import DataRequired


class AddConfigurationForm(FlaskForm):
    name = StringField("Название сборки", validators=[DataRequired()], render_kw={"placeholder": 'Имя сборки'})
    
    about = TextAreaField('Описание', render_kw={'style': 'min-height: 150px',
                                                              "placeholder": 'Здесь вы можете описать вашу сборку, для каких целей она и сколько FPS в играх'})
    
    cpu = StringField('Процессор', validators=[DataRequired()], render_kw={"placeholder": 'Название процессора'})
    cpu_link = URLField('', render_kw={"placeholder": 'Ссылка на процессор'})
    cpu_price = IntegerField('Цена', validators=[DataRequired()], render_kw={"placeholder": 'Цена', 'type': 'number'})

    gpu = StringField('Видеокарта', validators=[DataRequired()], render_kw={"placeholder": 'Название видео карты'})
    gpu_link = URLField('', render_kw={"placeholder": 'Ссылка на видео карту'})
    gpu_price = IntegerField('Цена', validators=[DataRequired()], render_kw={"placeholder": 'Цена', 'type': 'number'})

    ram = StringField('Оперативная память', validators=[DataRequired()], render_kw={"placeholder": 'Название опративной памяти'})
    ram_link = URLField('', render_kw={"placeholder": 'Ссылка на опертивную память'})
    ram_price = IntegerField('Цена', validators=[DataRequired()], render_kw={"placeholder": 'Цена', 'type': 'number'})
     
    motherboard = StringField('Материнская плата', validators=[DataRequired()], render_kw={"placeholder": 'Название материнской платы'})
    motherboard_link = URLField('', render_kw={"placeholder": 'Ссылка на материнскую плату'})
    motherboard_price = IntegerField('Цена', validators=[DataRequired()], render_kw={"placeholder": 'Цена', 'type': 'number'})

    ssd = StringField('Накопитель', validators=[DataRequired()], render_kw={"placeholder": 'Название накопителя'})
    ssd_link = URLField('', render_kw={"placeholder": 'Ссылка на накопитель'})
    ssd_price = IntegerField('Цена', validators=[DataRequired()], render_kw={"placeholder": 'Цена', 'type': 'number'})

    frame = StringField('Корпус', validators=[DataRequired()], render_kw={"placeholder": 'Название корпуса'})
    frame_link = URLField('', render_kw={"placeholder": 'Ссылка на корпус'})
    frame_price = IntegerField('Цена', validators=[DataRequired()], render_kw={"placeholder": 'Цена', 'type': 'number'})

    cooler = StringField('Кулер', validators=[DataRequired()], render_kw={"placeholder": 'Название кулера'})
    cooler_link = URLField('', render_kw={"placeholder": 'Ссылка на кулеры'})
    cooler_price = IntegerField('Цена', validators=[DataRequired()], render_kw={"placeholder": 'Цена', 'type': 'number'})

    power = StringField('Блок питания', validators=[DataRequired()], render_kw={"placeholder": 'Название блока питания'})
    power_link = URLField('', render_kw={"placeholder": 'Ссылка на блок питания'})
    power_price = IntegerField('Цена', validators=[DataRequired()], render_kw={"placeholder": 'Цена', 'type': 'number'})

    comment = TextAreaField('Коментарий', render_kw={'style': 'min-height: 150px',
                                                              "placeholder": 'Напишите коментарий к сборке пк'})

    submit = SubmitField('Отправить')
