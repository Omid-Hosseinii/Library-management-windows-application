from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data["city"]


def get_temperature():

    city=get_location()       
    geolocator=Nominatim(user_agent="geoapiExercises")       
    location=geolocator.geocode(city)       
    obj=TimezoneFinder()     
    lng1=int(location.longitude)
    lat1=int(location.latitude)
    result=obj.timezone_at(lng=location.longitude,lat=location.longitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")  

    parametrs={"lat":str(lat1),"lon":str(lng1),"appid":"ef0593b766c8ce186824a4558cff8e52"}
    api="https://api.openweathermap.org/data/2.5/weather"
    data=requests.get(api,parametrs)
    jdata=data.json()
    condition=jdata['weather'][0]['main']
    description=jdata["weather"][0]["description"]
    temp=int(jdata['main']['temp']-273.15)
    pressure=jdata['main']['pressure']
    humidity=jdata['main']['humidity']
    wind=jdata['wind']['speed']

    info={'temp':temp,'time':current_time}
    return info

print(get_temperature())    





