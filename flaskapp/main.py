from app import app
from flask import Flask, render_template, request, make_response
from pymongo import MongoClient
import json
from bson import json_util
from random import random
from time import time

client = MongoClient("mongodb+srv://Erik:223SZe2we@cluster0.qxy4y.mongodb.net/Stocks_db?retryWrites=true&w=majority")
db = client["Stocks_db"]
coll = db['goog']
pred = db['prediction']

close = []
open = []
date = []
for doc in coll.find():
    close.append(doc['close'])
    open.append(doc['open'])
    date.append(doc['date'])

@app.route('/google-charts/pie-chart')
def google_pie_chart():
	data = {'Task' : 'Hours per Day', 'Work' : 8, 'Eat' : 3, 'Commute' : 0.5, 'Watching TV' : 3, 'Sleeping' : 8, 'Making Music' : 1.5}
	#print(data)
	return render_template('pie-chart.html', data=data)

@app.route('/google-charts/line-chart')
def google_line_chart():
	data1 = {'Task' : 'Hours per Day', 'Work' : 8, 'Eat' : 3, 'Commute' : 0.5, 'Watching TV' : 3, 'Sleeping' : 8, 'Making Music' : 1.5}
	return render_template('line-chart.html', data=data1)

@app.route('/home', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		uDetails = request.form
		name = uDetails['name']
		prediction = uDetails['prediction']
		#return prediction
		prediction = {"name": name, "prediction": prediction}
		pred.insert_one(prediction)
		return "success"
	return render_template('Home.html')

@app.route('/raw', methods=['GET'])
def get_data():
	all_data = list(coll.find({}))
	return json.dumps(all_data, default=json_util.default)

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]
	find = coll.find()
	it = find.next()
	#google = coll.find_one({})
	open = it["open"]
	close = it["close"]
	date = it['date']
	data = [date, close, open]
	response = make_response(json.dumps(data))
	response.content_type  ='application/json'
	return response

    #data = [time() * 1000, Temperature, Humidity]

if __name__ == "__main__":
	app.run()
