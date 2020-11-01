import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from random import randint


def Gym_Bot():
    weight_level = 62
    Name = ""
    Weight = int()
    Email_address = ""
    Email_password = ""
    answer = input('Requires your permission for email address and password will you like to do it: ')
    if answer.upper() == 'YES':
        print('(0-|-|-|-|-|-|-|-|-|-0)')
        print("permission granted...")
        Name = input('Enter your name: ')
        input('Enter your Height(feet): ')
        Weight = int(input('Enter your Weight(kilograms): '))
        input('Enter your  Blood_type: ')
        Email_address = input('Enter your  Email_address: ')
        Email_password = input("Enter your Email_password:  ")
    else:
        return "okay"
    if Weight <= weight_level:
        print(f'{Name} you are in good shape')
    else:
        result1 = f"Please {Name} listen to the instructions"
        message = MIMEMultipart()
        message["from"] = "GYM_BOT.235"
        message["to"] = Email_address
        message["subject"] = "Exercise"
        message.attach(MIMEText(result1 + ","))
        message.attach(MIMEText(result2 + ","))
        message.attach(MIMEText(result3 + ","))
        message.attach(MIMEText(result4 + ","))
        message.attach(MIMEText(result5 + ","))
        message.attach(MIMEText(result6 + ","))
        message.attach(MIMEText(result7 + ","))
        message.attach(MIMEText(result8 + "."))
        message.attach(MIMEImage(Path("gym pic.jpg").read_bytes()))
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(Email_address, Email_password)
            smtp.send_message(message)
            print(f"Message sent to {Email_address}...")


result2 = f'Ride your bicycle {randint(0, 30)} minutes everyday'
result3 = f'Jug {randint(0, 30)} minutes everyday'
result4 = f'Do seat ups {randint(0, 30)} times'
result5 = 'Eat vegetables everyday'
result6 = f'Do recreational activities at list {randint(0, 30)} minutes every weekend'
result7 = f'Go and meet your doctor after {randint(0, 30)} days'
result8 = f'In {randint(0, 30)} days you will be fit'

Gym_Bot()
