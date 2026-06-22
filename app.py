from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import pandas as pd
import resend
import os
from dotenv import load_dotenv
import requests


def send_email(username, user_email, api_key):
    email_content = f"Здраввствуйте, {username}, вы получили предложение от нашего магазина"
    email_from = "mager.alexey@gmail.com"

    try:
        response = requests.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "from": email_from,
                "to": user_email,
                "subject": "Предложение от магазина",
                "text": email_content
            }
        )

        if response.status_code == 200:
            print(f"✅ Email успешно отправлен через Resend!")
            print(f"📧 Ответ: {response.json()}")
            return True
        else:
            print(f"❌ Ошибка отправки: {response.status_code}")
            print(f"📝 Детали: {response.text}")
            return False
        
    except Exception as e:
        print(f"❌ Исключение при отправке: {e}")
        return False


def get_user(username, usernumber, api_key):
    email_content = f"Здраввствуйте! Новый пользователь {username}, {usernumber}"
    email_from = "mager.alexey@gmail.com"

    try:
        response = requests.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "from": email_from,
                "to": email_from,
                "subject": "Новый пользователь",
                "text": email_content
            }
        )

        if response.status_code == 200:
            print(f"✅ Email успешно отправлен через Resend!")
            print(f"📧 Ответ: {response.json()}")
            return True
        else:
            print(f"❌ Ошибка отправки: {response.status_code}")
            print(f"📝 Детали: {response.text}")
            return False
        
    except Exception as e:
        print(f"❌ Исключение при отправке: {e}")
        return False   


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def site():


#---------Отправка на почту----------------------------


    if request.method == 'POST':
        api_key = "re_FXJTH6y1_BqQ16dWDhodoz6dBkAtXnK6f"
        form_type = request.form.get("form_type")

        if form_type == "form1_submit":
            print(api_key)
            username = request.form.get('user_name')
            user_email = request.form.get('user_email')
            send_email(username, user_email, api_key)



        elif form_type == "form2_submit":

            username = request.form.get('user_name')
            usernumber = request.form.get('user_number')

            get_user(username, usernumber, api_key)



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



#------------------Люди--------------------------------------


    database = pd.read_excel('База Данных инста.xlsx')
        
    insta_imgs = []

    for index, row in database.iterrows():
        insta_imgs.append(row['Путь до картинки'])


    return render_template('index.html', sneakers=sneakers, teams=teams, insta_imgs=insta_imgs)



if __name__ == '__main__':
    app.run(debug=True)
