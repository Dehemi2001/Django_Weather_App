from django.shortcuts import render
import json
import urllib.request
from urllib.error import HTTPError, URLError
from urllib.parse import quote  # Add this import

# Create your views here.
def index(request):
    error_message = ''
    data = {}
    city = ''
    if request.method == 'POST':
        city = request.POST['city']
        city = city.title()  # Ensure city name is always in proper case
        try:
            city_encoded = quote(city)
            res = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city_encoded + '&appid=09cb4d15c38e2001c6cc8e6476b2ebc6'
            ).read()
            json_data = json.loads(res)
            temp_kelvin = float(json_data['main']['temp'])
            temp_celsius = round(temp_kelvin - 273.15, 2)
            icon_code = json_data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            description = json_data['weather'][0]['description']
            data = {
                'country_code': str(json_data['sys']['country']),
                'coordinate': str(json_data['coord']['lon']) + ' ' +
                str(json_data['coord']['lat']),
                'temp': f"{temp_celsius}°C",
                'pressure': f"{json_data['main']['pressure']} hPa",
                'humidity': f"{json_data['main']['humidity']}%",
                'icon_url': icon_url,
                'description': description,
            }
        except (HTTPError, URLError, KeyError, ValueError):
            error_message = "City not found or invalid input. Please enter a valid city name."
    return render(request, 'index.html', {'city': city, 'data': data, 'error_message': error_message})
