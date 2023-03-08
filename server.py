""""

    Author       : Ahmet Aktas
    Project name : Embedded HTTP Server
    Date         : 08.03.2023
    Versioh      : 1.0.0

Comment:
    This project created for demonstraions the http server on embedded systems(like a stm32, esp32 etc).
    However, This project didn't test the by a microcontroller. 
    At least, Now you can use the your computer with the local host. 

"""

from crypt import methods
from flask import Flask, render_template, jsonify, request, redirect
import ssl

app = Flask(__name__)

#context = ssl.SSLContext()
#context.load_cert_chain('/home/ahmet/Desktop/python_projects/rootCACert.pem', '/home/ahmet/Desktop/python_projects/rootCAKey.pem')

valid_name = "ahmet"
valid_pwd = "1234"

access_flag = False

@app.route("/", methods = ['GET', 'POST'])
def login_page():
    if request.method == "POST":
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        print(name, pwd)
        if (valid_name == name) & (valid_pwd == pwd):
            access_flag = True
            print(access_flag)
            print("hello world")
            return redirect('/home_page')
        #access_flag = False
        return "Invalid User Name and Password"
    return render_template('login.html')

@app.route("/home_page", methods = ['GET', 'POST'])
def home_page():
    if access_flag == True:
        return render_template('home_page.html')
    return "Permission denied"
    


@app.route("/io", methods = ['GET'])
def io_page():
    if access_flag ==True:
        return render_template('io.html')
    return "Permission denied"


@app.route("/log", methods = ['GET'])
def log_page():
    if access_flag ==True:
        return render_template('log.html')
    return "Permission denied"
    



if __name__ == '__main__':
    app.run(debug= TRUE, host='192.168.1.115', port = 8000)
    #app.run(debug= TRUE, host='192.168.10.150', port = 8000, ssl_context = context)