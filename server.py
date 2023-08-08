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

buttons = ['IO1', 'IO2', 'IO3']


app = Flask(__name__)

#context = ssl.SSLContext()
#context.load_cert_chain('/home/ahmet/Desktop/python_projects/rootCACert.pem', '/home/ahmet/Desktop/python_projects/rootCAKey.pem')

valid_name = "ahmet"
valid_pwd = "1234"

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
            if str(control) == 'on':
                checked[i] = 'checked'
        
        template = render_template('io.html', len = len(buttons), button = buttons, checked = checked)

        print("template", template)
    return template


@app.route("/log", methods = ['GET'])
def log_page():
    return render_template('log.html')

if __name__ == '__main__':
    app.run(debug= True, host='192.168.1.168', port = 8000)
    #app.run(debug= TRUE, host='192.168.10.150', port = 8000, ssl_context = context)