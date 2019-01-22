#!/usr/bin/python3
# -*- coding: utf-8 -*-

import bottle, os, time, subprocess
from bottle import route, template, post, request, error, run
from datetime import date

app = application = bottle.Bottle()

# 404 error message listing all available links
@app.error(404)
def error404(error):
    return template('404error')

# Redirecting to home page for now
@app.route('/boru')
def boru():
    # Redirect to home (for now)
    return template('boruRedirectToHome')

# Home Page
@app.route('/boru/home')
def home():
    return template('home')

# The main form
@app.get('/boru/form')
def form():
    #return 'form' template from views dir
    return template('form')

# Writing all information from the form to a file and redirecting to /readform
# When chanigin '/boru/form' remember to change the HTML
@app.post('/boru/form')
def do_post():
    # All the form fields from /form stored in variables below
    accountName = request.forms.get('field1')
    password = request.forms.get('field2')
    region = request.forms.get('field3')
    course = request.forms.get('field4')
    sensor = request.forms.get('field5')
    tag = request.forms.get('field6')
    ###beginDate = request.forms.get('field7')
    endDate = request.forms.get('field8')
    timezone = request.forms.get('field9')

    # Getting todays date
    currentDate = str(date.today())

    # Creating the labStart command
    labstartCommand = ('sudo -u aws /usr/local/bin/labStart -a ' + accountName + ' -p ' + password + ' -r ' + region + ' -c ' + course + ' -s ' + sensor + ' -t ' + tag + ' -b ' + 'now' + ' -e ' + endDate + ' -z ' + timezone + ' | tee -a /var/log/labs/labStart/' + currentDate + '-' + accountName + '-' + course + '-' + timezone + '-' + tag + '-labStart.log &')

    # Starting the Lab
    subprocess.call(labstartCommand, shell=True)

    # Path to log file
    pathToFile = currentDate + '-' + accountName + '-' + course + '-' + timezone + '-' + tag + '-labStart.log'

    # returns 'formPost' template from views dir
    return template('redirect', pathToFile=pathToFile)

# Read File
@app.route('/boru/logOutput/<fileName>')
def logOutput(fileName):
    pathToFile = '/var/log/labs/labStart/' + fileName
    # Passes the file path to readFile
    return template('readFile', pathToFile=pathToFile)
#---------------------------------------------------------------------------------------------------
class StripPathMiddleware(object):
    # Get that slash out of the request
    def __init__(self, a):
        self.a = a
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)

if __name__ == '__main__':
    bottle.run(app=StripPathMiddleware(app),
        host='0.0.0.0',
        port=8080)
