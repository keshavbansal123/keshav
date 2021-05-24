# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:34:04 2021

@author: Dell
"""

# from pymongo import MongoClient

# client=MongoClient('mongodb+srv://keshav123:mongodb@cluster0.vadzf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

# db=client.gettingstarted
# people=db.people

# persondocument={
#     "name":{"first":"keshav","last":"bansal"}
#     }

# people.insert_one(persondocument)   

from flask import Flask, render_template
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config["MONGO_URI"]="mongodb+srv://keshav123:mongodb@cluster0.vadzf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongo=PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)











