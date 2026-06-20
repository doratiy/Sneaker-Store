from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import pandas as pd


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'mager.alexey@gmail.com'
app.config['MAIL_PASSWORD'] = 'igtt qwek wxyq wjzd'
app.config['MAIL_DEFAULT_SENDER'] = 'mager.alexey@gmail.com' 
mail = Mail(app)
manager_email = "mager.alexey@gmail.com"


@app.route('/', methods=['GET', 'POST'])


def site():


#---------Отправка на почту----------------------------

    if request.method == 'POST':
        form_type = request.form.get("form_type")

        if form_type == "form1_submit":
            username = request.form.get('user_name')
            email = request.form.get('user_email')

            try:
                msg = Message(
                    subject="Предложение",
                    recipients=[email],
                    body=f"Привет, {username}! Вы получили предложение от магазина"
                )
                mail.send(msg)
                print(f"пользователь: {username}, Email: {email} получил предложение")
                    
            except Exception as e:
                print(f"Произошла ошибка: {e}") 

        elif form_type == "form2_submit":

            username = request.form.get('user_name')
            email = request.form.get('user_email')

            try:
                msg = Message(
                    subject="Новый пользователь",
                    recipients=[manager_email],
                    body=f"Новый пользователь {username} {email}"
                )
                mail.send(msg)
                print(f"Новый пользователь: {username}, Email: {email}")
                    
            except Exception as e:
                print(f"Произошла ошибка: {e}")  

#---------Отправка на почту----------------------------


#---------Каталог----------------------------

    database = pd.read_excel('База Данных кроссовки.xlsx')
        
    sneakers = []

    for index, row in database.iterrows():
        sneakers.append({
            'name': row['Название'],
            'cost': row['Стоимость'],
            'image_path': row['Путь до картинки']
        })

        print(row['Путь до картинки'])

#------------------Люди--------------------------------------


    database = pd.read_excel('База Данных люди.xlsx')
        
    teams = []

    for index, row in database.iterrows():
        teams.append({
            'name': row['Имя'],
            'post': row['Должность'],
            'image_path': row['Путь до картинки']
        })

        print(row['Путь до картинки'])

    return render_template('index.html', sneakers=sneakers, teams=teams)



if __name__ == '__main__':
    app.run(debug=True)