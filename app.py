from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

# Your OpenWeather API Key
API_KEY = "c84d81a9cd71106f1fea0d75750581be"


@app.route("/", methods=["GET", "POST"])
def index():

    weather = None
    forecast_list = []
    error = None

    if request.method == "POST":

        city = request.form.get("city")

        # Current Weather API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        # 5-Day Forecast API
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

        try:

            # Current Weather Data
            response = requests.get(url)
            data = response.json()

            # Forecast Data
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()

            if data["cod"] == 200:

                # Main Weather Data
                weather = {

                    "city": data["name"],
                    "country": data["sys"]["country"],

                    "temperature": round(data["main"]["temp"]),
                    "feels_like": round(data["main"]["feels_like"]),

                    "humidity": data["main"]["humidity"],
                    "pressure": data["main"]["pressure"],

                    "wind_speed": data["wind"]["speed"],

                    "description": data["weather"][0]["description"].title(),

                    "icon": data["weather"][0]["icon"],

                    "sunrise": datetime.fromtimestamp(
                        data["sys"]["sunrise"]
                    ).strftime("%I:%M %p"),

                    "sunset": datetime.fromtimestamp(
                        data["sys"]["sunset"]
                    ).strftime("%I:%M %p")
                }

                # Forecast Data
                for item in forecast_data["list"][:5]:

                    date_object = datetime.strptime(
                        item["dt_txt"],
                        "%Y-%m-%d %H:%M:%S"
                    )

                    formatted_date = date_object.strftime("%A")

                    forecast = {

                        "date": formatted_date,

                        "temp": round(item["main"]["temp"]),

                        "description": item["weather"][0]["description"].title(),

                        "icon": item["weather"][0]["icon"]
                    }

                    forecast_list.append(forecast)

            else:
                error = data.get(
                    "message",
                    "Something went wrong."
                )

        except Exception as e:
            error = f"Error: {e}"

    return render_template(
        "index.html",
        weather=weather,
        forecast_list=forecast_list,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)