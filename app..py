from flask import Flask, render_template, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'weatherapp'

@app.route('/',  methods = ['GET', 'POST'])
def get_weather_app():
    pass

if __name__ == ('__main__'):
    app.run(debug=True)
