from flask import Flask, render_template, redirect, url_for, request
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'weatherapp'

@app.route('/',  methods = ['GET', 'POST'])
def get_weather_app():
    if request.method == 'POST':
        city = request.form['input']

    return render_template('interface.html')

if __name__ == ('__main__'):
    app.run(debug=True)
