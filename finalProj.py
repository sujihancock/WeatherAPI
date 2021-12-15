"""
    Course: CST 205
    Title: Weather API Project
    Abstract: This program will allow the user to input a city and will give back the temperature at that location.
    Authors: Matthew Fernandez, Irvine Martinez and Suji Hancock
    Date: December 15, 2021
"""

# Github link: https://github.com/mattf4171/WeatherAPI

# Needed imports to run files
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests
import random
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/", methods=["GET", "POST"])
def index():
    
    # initial values, will be filled in once the api retrieves the data once the user passes in the city
    temp = ''
    feels_like =''
    temp_max = ''
    city=''
    temp_min = ''
    weather = ''
    weather_time = ''
    weather_conditions = ['', 'cloud','rain', 'snow','sun', 'moon']

    if request.method == "POST":
        
        # User inputs the city, data is then retrieved from the html page
        city = request.form["city"]
        # link the the api, with city passed in
        url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=08eba528435fd4c005a6e7fd4d7668c1&units=imperial")
        data = url.json() 
        # temp = data['main']['temp']
        # feels_like = data['main']['feels_like']
        # temp_min = data['main']['temp_min']
        # temp_max = data['main']['temp_max']
        # return render_template('weather.html',city = city, temp = temp, feels_like = feels_like, temp_min = temp_min, temp_max = temp_max)
        
        # indexing the values retrieved from api
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        weather = data['weather'][0]['main']
        weather_time = data['weather'][0]['icon']

    # return the Flask Fn with the index.html file, and the weather data we'd like to display to the users. 
    return render_template('index.html', weather_time=weather_time, weather_conditions = weather_conditions, weather = weather,city=city, temp = temp, feels_like = feels_like, temp_max = temp_max, temp_min = temp_min)

# debug mode for sanity check
if __name__ == '__main__':
    app.run(debug = True)


