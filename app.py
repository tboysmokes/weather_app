from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
import requests
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'weatherapp'


# I set city to a defalt value incase the user doesn't input anything
def get_weather_data(city = "lagos"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()
    print(weather_data)


    return weather_data


@app.route('/',  methods = ['GET', 'POST'])
def get_data():
    if request.method == "POST":
        city = request.form['input']


        if city == "":
            city = "lagos"


        weather_data = get_weather_data(city)

        return render_template(
            "weather.html",
            title = weather_data["name"],
            status = weather_data["weather"][0]["description"],
            temp = f"{weather_data['main']['temp']}",
            feels_like = f"{weather_data['main']['feels_like']}",
            min_temp = f"{weather_data['main']['temp_min']}",
            max_temp = f"{weather_data['main']['temp_max']}",
        )
    return render_template("weather.html")

if __name__ == ('__main__'):
    app.run(debug=True)
