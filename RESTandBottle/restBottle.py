#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Set up -----------------------------------------------
import bottle, subprocess, json
from bottle import run, get, post, request, delete
from datetime import date

# App
app = application = bottle.Bottle()
# ------------------------------------------------------

# ------------------------------------------------------
# My Data (in memory)
# ------------------------------------------------------
#myData = [{'accountName' : 'AVTestStudent', 'password' : 'Password1!', 'region' : 'us-east-1', 'course' : 'ANYDC', 'sensor' : 'no', 'tag' : 'myTagHere', 'beginDate' : '2019-01-03', 'endDate' : '2019-01-04', 'timezone' : 'EST'}]
myData = [{'Initialization' : 'NULL'}]

# ------------------------------------------------------
# Get All Data
# ------------------------------------------------------
@app.get('/data')
def getAll():
        return {'myData' : myData}

# ------------------------------------------------------
# Get Specific JSON Object | Returns account
# ------------------------------------------------------
# In Get add: /data/AVStudent199
# ------------------------------------------------------
@app.get('/data/<accountName>')
def getOne(accountName):
        myStudent = [student for student in myData if student['accountName'] == accountName]
        return {'student' : myStudent[0]}

# ------------------------------------------------------
# Post JSON Object | Returns user data
# ------------------------------------------------------
# In Post add: {"accountName" : "AVStudent199", "password" : "Password1!", "region" : "us-east-1", "course" : "ANYDC", "sensor" : "no", "tag" : "myTagHere", "beginDate" : "2019-01-03", "endDate" : "2019-01-04", "timezone" : "EST"}
# ------------------------------------------------------
@app.post('/data')
def addOne():
# No error chacking for the script
	myStudent = {'accountName' : request.json.get('accountName'),
			'password' : request.json.get('password'),
			'region' : request.json.get('region'),
			'course' : request.json.get('course'),
			'sensor' : request.json.get('sensor'),
			'tag' : request.json.get('tag'),
			'beginDate' : request.json.get('beginDate'),
			'endDate' : request.json.get('endDate'),
			'timezone' : request.json.get('timezone')}

	# Getting todays date
	currentDate = str(date.today())

	# labStart Command with the inputs from the JSON Object
	labStartCommand = ('sudo -u jarek /usr/local/bin/labStart -a ' +
				myStudent['accountName'] +
				' -p ' + myStudent['password'] +
				' -r ' + myStudent['region'] +
				' -c ' + myStudent['course'] +
				' -s ' + myStudent['sensor'] +
				' -t ' + myStudent['tag'] +
				' -b ' + myStudent['beginDate'] +
				' -e ' + myStudent['endDate'] +
				' -z ' + myStudent['timezone'] +
				' | tee -a /var/log/labs/labStart/' +
				currentDate +
				'-' + myStudent['accountName'] +
				'-' + myStudent['course'] +
				'-' + myStudent['timezone'] +
				'-' + myStudent['tag'] +
				'-labStart.log &')

	# Starting the Lab Script
###	subprocess.call(labStartCommand, shell=True)

	# Adding to myData (Will be MongoDB)
	myData.append(myStudent)

	# Returns user input
	return ("Starting Lab for ", json.dumps(myStudent))

# ------------------------------------------------------
# Delete JSON Object | Returns accounts left in database
# ------------------------------------------------------
# In Delete add: /data/AVStudent199
# ------------------------------------------------------
@app.delete('/data/<accountName>')
def deleteOne(accountName):
	# Goes through the data and finds the one with matching accountName
	thePerson = [student for student in myData if student['accountName'] == accountName]
        # Removes the date form myData
	myData.remove(thePerson[0])
	return {'myData' : myData}

# RUN --------------------------------------------------
class StripPathMiddleware(object):
    # Get that slash out of the request
    def __init__(self, a):
        self.a = a
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)
# Run
if __name__ == '__main__':
        bottle.run(app=StripPathMiddleware(app),
        host='0.0.0.0',
        port=8080)