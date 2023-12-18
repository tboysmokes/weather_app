Weather App with Flask
This is a simple weather application built using Flask that allows users to check the current weather conditions 
in a specified city. The app utilizes the OpenWeatherMap API to fetch weather data for the provided city.

Features
Users can enter the name of a city to get the current weather conditions.
If no city name is provided, the app defaults to displaying weather information for Lagos.
The app displays the city name, weather description, temperature, feels-like temperature, minimum temperature, and maximum temperature.
Prerequisites
Before running the application, make sure you have the following set up:

Python 3.x installed on your machine.
API key from OpenWeatherMap. You can obtain one by signing up at OpenWeatherMap.

Installation
Clone this repository to your local machine:

bash
git clone https://github.com/tboysmokes/weather-flask-app.git
Navigate to the project directory:

bash
cd weather-flask-app
Create a virtual environment (recommended):

bash
python -m venv venv
Activate the virtual environment:

On Windows:

bash
venv\Scripts\activate
On macOS and Linux:

bash
source venv/bin/activate
Install the required dependencies:

bash
pip install -r requirements.txt
Create a .env file in the project directory and add your OpenWeatherMap API key:

makefile
API_KEY=your_api_key_here
Usage
Run the Flask application:

bash
python app.py
Open a web browser and go to http://localhost:5000/ to access the weather app.

Enter the name of a city and click the "Get Weather" button to view the current weather conditions for that city.

Contributing
If you'd like to contribute to this project, please follow these guidelines:

Fork the repository.

Create a new branch for your feature or bug fix:

bash
git checkout -b feature-name
Make your changes and commit them:

bash
git commit -m "Add your commit message here"
Push your changes to your fork:

bash
git push origin feature-name
Create a pull request to merge your changes into the main repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project uses the OpenWeatherMap API to fetch weather data.
Feel free to customize this README to include any additional information about your project or any special instructions for users. Good luck with your Flask weather app!
