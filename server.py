""""

    Author       : Ahmet Aktas
    Project name : Embedded HTTP Server
    Date         : 08.08.2023
    Versioh      : 1.0.0

Comment:
    This project created for demonstraions the http server on embedded systems(like a stm32, esp32 etc).
    However, This project didn't test the by a microcontroller. 
    At least, Now you can use the your computer with the local host. 

"""

from crypt import methods
from flask import Flask, render_template, jsonify, request, redirect
import ssl
import datetime
from ring_buffer import RingBuffer
#import RPi.GPIO as GPIO

buttons = ['IO1', 'IO2', 'IO3']
pins = [23, 24, 25]

valid_name = "ahmet"
valid_pwd = "1234" 

buff_len = 10
msg_button = RingBuffer(buff_len)
msg_time = RingBuffer(buff_len)
#context = ssl.SSLContext()
#context.load_cert_chain('/home/ahmet/Desktop/python_projects/rootCACert.pem', '/home/ahmet/Desktop/python_projects/rootCAKey.pem')

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def login_page():
    if request.method == "POST":
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        print(name, pwd)
        if (valid_name == name) & (valid_pwd == pwd):
            access_flag = True
            print("access flag is = ", access_flag)
            print("Pasword is correct")
            return redirect('/home_page')

        return "Invalid User Name and User Password"
    return render_template('login.html')

@app.route("/home_page", methods = ['GET', 'POST'])
def home_page():
    return render_template('home_page.html')
    

@app.route("/io", methods = ['GET', 'POST'])
def io_page():
    checked = []
    for i in range(len(buttons)):
        if request.method == 'POST':
            control = request.form.get(buttons[i])
            checked.append(' ')
            current_time = datetime.datetime.now()
            msg_time.add(current_time)
            if str(control) == 'on':
                checked[i] = 'checked'
                msg_button.add(str(buttons[i] + " on"))
                print("gpio output is high")
            else:
                msg_button.add(str(buttons[i] + " off"))
                print("gpio output is low")
            

        template = render_template('io.html', len = len(buttons), button = buttons, checked = checked)

    return template


@app.route("/log", methods = ['GET'])
def log_page():
    return render_template('log.html', len = buff_len, time = msg_time.getAll(), 
                           message = msg_button.getAll())

if __name__ == '__main__':
    app.run(debug= True, host='192.168.1.168', port = 8000)
    #app.run(debug= TRUE, host='192.168.10.150', port = 8000, ssl_context = context)