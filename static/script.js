// Weather App JavaScript

// Select elements
const weatherCard = document.querySelector(".weather-card");
const searchButton = document.querySelector("button");
const inputField = document.querySelector("input");

// Add button click animation
searchButton.addEventListener("click", () => {
    searchButton.style.transform = "scale(0.95)";

    setTimeout(() => {
        searchButton.style.transform = "scale(1)";
    }, 150);
});

// Input focus effect
inputField.addEventListener("focus", () => {
    inputField.style.boxShadow = "0 0 15px rgba(255,255,255,0.8)";
});

inputField.addEventListener("blur", () => {
    inputField.style.boxShadow = "none";
});

// Fade-in animation for weather card
if (weatherCard) {
    weatherCard.style.opacity = "0";
    weatherCard.style.transform = "translateY(20px)";

    setTimeout(() => {
        weatherCard.style.transition = "all 0.8s ease";
        weatherCard.style.opacity = "1";
        weatherCard.style.transform = "translateY(0)";
    }, 200);
}

// Dynamic background based on temperature
const temperatureElement = document.querySelector(".weather-card h3");

if (temperatureElement) {

    let temp = parseInt(temperatureElement.innerText);

    if (temp <= 10) {
        document.body.style.background =
            "linear-gradient(135deg, #4facfe, #00f2fe)";
    }

    else if (temp > 10 && temp <= 25) {
        document.body.style.background =
            "linear-gradient(135deg, #43cea2, #185a9d)";
    }

    else {
        document.body.style.background =
            "linear-gradient(135deg, #ff9966, #ff5e62)";
    }
}

// Press Enter to search
inputField.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {
        searchButton.click();
    }
});