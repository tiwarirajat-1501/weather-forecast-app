from flask import Flask, render_template, request
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# API Key from .env file
API_KEY = os.getenv("API_KEY")


@app.route("/", methods=["GET", "POST"])
def index():

    weather = None
    forecast_list = []
    error = None

    if request.method == "POST":

        city = request.form.get("city")

        # Current Weather API
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        # 5-Day Forecast API
        forecast_url = (
            f"https://api.openweathermap.org/data/2.5/forecast"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        try:

            # Fetch Current Weather Data
            response = requests.get(url)
            data = response.json()

            # Fetch Forecast Data
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()

            # Check if city exists
            if data["cod"] == 200:

                # Current Weather Data
                weather = {

                    "city": data["name"],
                    "country": data["sys"]["country"],

                    "temperature": round(data["main"]["temp"]),
                    "feels_like": round(data["main"]["feels_like"]),

                    "humidity": data["main"]["humidity"],
                    "pressure": data["main"]["pressure"],

                    "wind_speed": data["wind"]["speed"],

                    "description": (
                        data["weather"][0]["description"].title()
                    ),

                    "icon": data["weather"][0]["icon"],

                    "sunrise": datetime.fromtimestamp(
                        data["sys"]["sunrise"]
                    ).strftime("%I:%M %p"),

                    "sunset": datetime.fromtimestamp(
                        data["sys"]["sunset"]
                    ).strftime("%I:%M %p")
                }

                # 5-Day Forecast Data
                added_days = set()

                for item in forecast_data["list"]:

                    date_object = datetime.strptime(
                        item["dt_txt"],
                        "%Y-%m-%d %H:%M:%S"
                    )

                    day_name = date_object.strftime("%A")

                    # Avoid duplicate days
                    if day_name not in added_days:

                        forecast = {

                            "date": day_name,

                            "temp": round(
                                item["main"]["temp"]
                            ),

                            "description": (
                                item["weather"][0]["description"].title()
                            ),

                            "icon": item["weather"][0]["icon"]
                        }

                        forecast_list.append(forecast)

                        added_days.add(day_name)

                    # Limit to 5 forecast days
                    if len(forecast_list) == 5:
                        break

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
    app.run(host="0.0.0.0", port=5000)