from flask import Flask, render_template, request

import requests

import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    temp = ''
    feels_like =''
    temp_max = ''
    city=''
    temp_min = ''
    weather = ''

    if request.method == "POST":

        city = request.form["city"]

        url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=08eba528435fd4c005a6e7fd4d7668c1&units=imperial")

        data = url.json()

        # temp = data['main']['temp']
        # feels_like = data['main']['feels_like']
        # temp_min = data['main']['temp_min']
        # temp_max = data['main']['temp_max']
        # return render_template('weather.html',city = city, temp = temp, feels_like = feels_like, temp_min = temp_min, temp_max = temp_max)
        
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        weather = data['weather'][0]['main']



    return render_template('index.html', weather = weather,city=city, temp = temp, feels_like = feels_like, temp_max = temp_max, temp_min = temp_min)

if __name__ == '__main__':
    app.run(debug = True)