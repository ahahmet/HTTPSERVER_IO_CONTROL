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
#from gpio import BoardGPIO

#IP
host = '192.168.1.168'

#button name for html
buttons = ['IO1', 'IO2', 'IO3']

# IO number and initialize
pins = [23, 24, 25]
""" gpio = BoardGPIO(len(pins))
gpio.gpio_init() """

# Ring Buffer
buff_len = 10
msg_button = RingBuffer(buff_len)
msg_time = RingBuffer(buff_len)

#If you want to use ssl on your server, please uncommand the line in below
#cert_dir = " "
#key_dir = " " 
#context = ssl.SSLContext()
#context.load_cert_chain( cert_dir, key_dir)

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
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
            #check the clicked button
            if str(control) == 'on':
                checked[i] = 'checked'
                msg_button.add(str(buttons[i] + " on"))
                #gpio.output_on(i)
                print("gpio output is high")
            else:
                msg_button.add(str(buttons[i] + " off"))
                #gpio.output_on(i)
                print("gpio output is low")         

        template = render_template('io.html', len = len(buttons), button = buttons, checked = checked)
    return template

@app.route("/log", methods = ['GET'])
def log_page():
    return render_template('log.html', len = buff_len, time = msg_time.getAll(), 
                           message = msg_button.getAll())

if __name__ == '__main__':
    app.run(debug= True, host= host, port = 8000)
    #app.run(debug= TRUE, host='192.168.10.150', port = 8000, ssl_context = context)