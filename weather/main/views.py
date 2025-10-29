import requests
from django.shortcuts import render

def index(request):
    """
    Renders weather data into the template.
    Example: /?city=London
    """
    # city = request.GET.get('city', 'Delhi')
    city = request.GET.get('city', 'Mumbai')
    weather_data = None

    # --- Step 1: Get coordinates ---
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_response = requests.get(geocode_url)
    geo_data = geo_response.json()

    if "results" in geo_data and geo_data["results"]:
        location = geo_data["results"][0]
        lat, lon = location["latitude"], location["longitude"]

        # --- Step 2: Fetch weather ---
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current_weather=true"
        )
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json().get("current_weather")

        if weather_data:
            weather_data.update({
                "city": location["name"],
                "latitude": lat,
                "longitude": lon,
                "country_code": location.get("country_code", ""),
            })

    context = {
        'weather': weather_data
    }

    return render(request, 'main/index.html', context)
