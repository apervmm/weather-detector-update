from django.shortcuts import render, redirect
from django.contrib import messages
import string
import json
import urllib.request


def index(request):
    if request.method == 'POST':
        try:
            city = request.POST['city']
            city_url = city.replace(' ', '+')
            apiKey = 'e0e17eb3df6ed8886f523f12d9437849'
            res = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city_url+"&appid="+apiKey).read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                "temp": str(round((int(json_data['main']['temp']) - 273.15) * 1.8 + 32))+'K',
                'pressure': str(json_data['main']['pressure']),
                'humidity':str(json_data['main']['humidity']),
            }
        except Exception:
            messages.info(request, "Invalid City Name")
            return redirect('/')
    else:
        city = ""
        data = {}

    return render(request, 'index.html', {"city": city, 'data':data})
