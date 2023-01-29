import requests
from settings import WEATHER_KEY, GOOGLE_KEY


def weather(city_name, weather_key=WEATHER_KEY):
    source = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_key}&units=metric'
    try:
        request = requests.get(source).json()
        longitude = request['coord']['lon']
        latitude = request['coord']['lat']
        data = f"country_code: {request['sys']['country']},\n" \
               f"city: {city_name.capitalize()},\n" \
               f"longitude: {request['coord']['lon']}°,\n" \
               f"latitude: {request['coord']['lat']}°,\n" \
               f"weather_type: {request['weather'][0]['main']},\n" \
               f"temperature: {request['main']['temp']} °C"
        return data, longitude, latitude
    except KeyError:
        return False


def get_image(longitude, latitude, google_key=GOOGLE_KEY):
    source = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}" \
             f"&zoom=10&size=400x400&key={google_key}"
    return source
