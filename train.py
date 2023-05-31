#!/usr/bin/python3
from gpiozero import Motor
from bottle import route, run, static_file, request

motor = Motor (17, 18)

@route('/')
def server_home ():
    return static_file ('index.html', root="/opt/train/public/")
    
# public files
# *** WARNING ANYTHING STORED IN THE PUBLIC FOLDER WILL BE AVAILABLE TO DOWNLOAD
@route ('/public/<filename>')
def server_public (filename):
    return static_file (filename, root="/opt/train/public")

@route('/control')
def control_train ():
    #getvar_dict = request.query.decode()
    # get speed & direction
    speed = int(request.query.speed)
    direction = int(request.query.direction or 1)
    # check speed is valid
    if (speed >= 0 and speed <= 10 and direction >= -1 and direction <= 1):
        command_speed = speed / 10
        train_set_speed (command_speed, direction)
        return "Speed is {} direction {}".format(speed, direction)
    else:
        return "Invalid command"
    
def train_set_speed(speed, direction):
    if direction == 0:
        motor.stop()
    elif direction == 1:
        motor.forward(speed)
    else:
        motor.backward(speed)

run (host='0.0.0.0', port=8080, debug=True)