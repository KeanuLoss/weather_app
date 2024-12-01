from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')   # get the city

    if not bool(city.strip()):
        city = "Hamburg"

    

    weather_data = get_current_weather(city)  # get the weather of that city

    if not weather_data['cod'] == 200:
        return render_template('city_not_found.html')
    
    
    return render_template(           # send the data to the template / html file
        "weather.html",     #first the value of the template itself, then all the other values you're using
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",  #:.1f formats to one decimal after the ,
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )         


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)