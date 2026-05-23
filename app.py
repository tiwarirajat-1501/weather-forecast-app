from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:

                weather = {
                    "city": data["name"],
                    "country": data["sys"]["country"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"],
                    "icon": data["weather"][0]["icon"]
                }

            else:
                error = "City not found."

        except Exception as e:
            error = f"Error: {e}"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)