from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')


# Define response function from OpenWeatherAPI using city as filter
def get_weather(city):
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    response = requests.get(url)
    data = response.json()
    return data

def response(city):
    weather = get_weather(city)
    response_text = f"The weather in {city} is {weather['current']['condition']['text']} with a temperature of {weather['current']['temp_c']} degrees Celsius."
    return response_text

# Initialize Flask app
app = Flask(__name__)

# Define route for POST request on /api/weather using 'city' parameter
@app.route('/api/weather', methods=['POST'])
def weather():
    # Get the city name from the request
    data = request.get_json()
    user_response = data['city']
    response_text = response(user_response)
    return jsonify({'message': response_text})


# Start the App
if __name__ == '__main__':
    app.run()
