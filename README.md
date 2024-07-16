# Simple Weather App

A simple Python-based command-line application to fetch current weather data for a specified city using the OpenWeatherMap API.

## Features
- Fetches current weather data for a specified city.
- Displays city name, temperature in Celsius, pressure, humidity, and a brief weather description.

## Requirements
- Python 3.x
- `requests` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/weather-app.git
    cd weather-app
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Obtain your API key from [OpenWeatherMap](https://openweathermap.org/api).

2. Update the `api_key` variable in `weather.py` with your API key.

3. Run the application:
    ```sh
    python weather.py
    ```

4. Enter the city name when prompted.
