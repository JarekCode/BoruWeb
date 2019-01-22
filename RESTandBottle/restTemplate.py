#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Set up -----------------------------------------------
import bottle
from bottle import run, get, post, request, delete
# App
app = application = bottle.Bottle()
# ------------------------------------------------------

# ------------------------------------------------------
# My Data (in memory)
# ------------------------------------------------------
myData = [{'name' : 'Jarek', 'age' : '21'},
        {'name' : 'John', 'age' : '25'}]

# ------------------------------------------------------
# Get All Data
# ------------------------------------------------------
@app.get('/people')
def getAll():
        return {'myData' : myData}

# ------------------------------------------------------
# Get Specific JSON Object
# ------------------------------------------------------
# In Get add: /people/Jarek
# ------------------------------------------------------
@app.get('/people/<name>')
def getOne(name):
        my_person = [person for person in myData if person['name'] == name]
        return {'person' : my_person[0]}

# ------------------------------------------------------
# Post JSON Object
# ------------------------------------------------------
# In Post add: {"name" : "JohnO", "age" : "24"}
# ------------------------------------------------------
@app.post('/people')
def addOne():
        newPerson = {'name' : request.json.get('name'), 'age' : request.json.get('age')}
        myData.append(newPerson)
        return {'myData' : myData}

# ------------------------------------------------------
# Delete JSON Object
# ------------------------------------------------------
# In Delete add: /people/Jarek
# ------------------------------------------------------
@app.delete('/people/<name>')
def deleteOne(name):
        thePerson = [person for person in myData if person['name'] == name]
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