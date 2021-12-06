from flask import Flask, render_template, request

import requests

import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():


    if request.method == "POST":
        city = request.form["city"]


        url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=08eba528435fd4c005a6e7fd4d7668c1&units=imperial")

        data = url.json()

        # weather_data = {
        #     'temp' : data['main']['temp']
        #     # 'feels_like' : data.main.feels_like,
        #     # 'temp_min' : data.main.feels_like,
        #     # 'temp_max' : data.main.temp_max
        # }

        # print(data['main']['temp'])
        temp = data['main']['temp']



    return render_template('index.html', temp = temp)

if __name__ == '__main__':
    app.run(debug = True)


    # http://api.openweathermap.org/data/2.5/weather?q=Salinas&APPID=08eba528435fd4c005a6e7fd4d7668c1
