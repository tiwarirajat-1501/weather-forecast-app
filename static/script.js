// Weather App JavaScript

// Select Elements
const weatherCard = document.querySelector(".weather-card");
const searchButton = document.querySelector("button");
const inputField = document.querySelector("input");
const form = document.querySelector("form");
const loader = document.getElementById("loader");
const descriptionElement = document.querySelector(".description");

// Button Click Animation
searchButton.addEventListener("click", () => {

    searchButton.style.transform = "scale(0.95)";

    setTimeout(() => {

        searchButton.style.transform = "scale(1)";

    }, 150);
});

// Input Focus Effect
inputField.addEventListener("focus", () => {

    inputField.style.boxShadow =
        "0 0 15px rgba(255,255,255,0.8)";
});

inputField.addEventListener("blur", () => {

    inputField.style.boxShadow = "none";
});

// Fade-In Animation for Weather Card
if (weatherCard) {

    weatherCard.style.opacity = "0";

    weatherCard.style.transform =
        "translateY(20px)";

    setTimeout(() => {

        weatherCard.style.transition =
            "all 0.8s ease";

        weatherCard.style.opacity = "1";

        weatherCard.style.transform =
            "translateY(0)";

    }, 200);
}

// Dynamic Background Based on Weather Condition
if (descriptionElement) {

    let weatherCondition =
        descriptionElement.innerText.toLowerCase();

    // Remove default animated background
    document.body.style.animation = "none";

    // Clear Sky
    if (weatherCondition.includes("clear")) {

        document.body.style.background =
            "linear-gradient(135deg, #f6d365, #fda085)";
    }

    // Clouds
    else if (
        weatherCondition.includes("cloud")
    ) {

        document.body.style.background =
            "linear-gradient(135deg, #bdc3c7, #2c3e50)";
    }

    // Rain
    else if (
        weatherCondition.includes("rain")
    ) {

        document.body.style.background =
            "linear-gradient(135deg, #4b79a1, #283e51)";
    }

    // Snow
    else if (
        weatherCondition.includes("snow")
    ) {

        document.body.style.background =
            "linear-gradient(135deg, #e6dada, #274046)";
    }

    // Thunderstorm
    else if (
        weatherCondition.includes("thunderstorm")
    ) {

        document.body.style.background =
            "linear-gradient(135deg, #232526, #414345)";
    }

    // Haze / Mist / Fog
    else if (
        weatherCondition.includes("haze") ||
        weatherCondition.includes("mist") ||
        weatherCondition.includes("fog")
    ) {

        document.body.style.background =
            "linear-gradient(135deg, #757f9a, #d7dde8)";
    }

    // Default Background
    else {

        document.body.style.background =
            "linear-gradient(135deg, #4facfe, #00f2fe)";
    }
}

// Loader Animation on Form Submit
form.addEventListener("submit", () => {

    loader.style.display = "block";
});

// Press Enter to Search
inputField.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {

        searchButton.click();
    }
});

// Forecast Cards Hover Animation
const forecastCards =
    document.querySelectorAll(".forecast-card");

forecastCards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transform =
            "translateY(-8px) scale(1.03)";
    });

    card.addEventListener("mouseleave", () => {

        card.style.transform =
            "translateY(0) scale(1)";
    });
});