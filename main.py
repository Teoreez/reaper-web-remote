#init
from bottle import route, run, post, get, static_file, request
from pywinauto.application import Application
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import json

#init controll
app = Application().connect(path='C:\Program Files\REAPER (x64)\\reaper.exe')
app_dialog = app.top_window()
app_dialog.maximize()
app_dialog.set_focus()

#static servers and routes
@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='./www/')

@route('/css/<filename>')
def servecss(filename):
    return static_file(filename, root='./www/css/')

@route('/js/<filename>')
def servejs(filename):
    return static_file(filename, root='./www/js/')

@get('/')
def index():
    return server_static('index.html')

#Post API things
@post('/')
def index():
    #postdata = request.body.read()    
    value = request.forms.get("command")    
    if value == 'r':
        send_keys('^r')
    if value == 'e':
        send_keys('{END}')
    if value == 'm':
        #sendkey("m") - foobar
        send_keys("{m down}"
                "{m up}")
    return server_static('index.html')

#Edit server ip, etc
run(host='192.168.1.32', port=3000, debug=False)