# Dockerizing a simple python weather app

### What will this app does?
This custom python scripts prompts the user to enter a valid city name and prints out the city's current temperature in Celcius.

## Steps to dockerize the weather app

1. Build the python app as shown in .\dockerizing-simple-python-app\python-weather-app.py
2. Build the Dockerfile as shown in .\dockerizing-simple-python-app\python-weatherapp.Dockerfile
3. Run the docker build command: ``` docker build -f python-weatherapp.Dockerfile -t python-weather-app-docker . ```