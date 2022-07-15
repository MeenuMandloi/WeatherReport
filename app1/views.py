from django.shortcuts import render
import json
import urllib.request

def index(request):
    return render(request,"index.html")

def weather(request):
    if request.method == 'POST':
        city=request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city +
            '&appid=2a6624327a51b0e2c63ac75a4241f1c5').read()
        list_data = json.loads(source)
        data = {
            'city': city,
            "country_code": str(list_data['sys']['country']),
            "coordinate": str(list_data['coord']['lon']) + ' '
                          + str(list_data['coord']['lat']),
            "temp": str(list_data['main']['temp']) + 'c',
            "pressure": str(list_data['main']['pressure']),
            "humidity": str(list_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "weather.html", data)


def bitcoin(request):
    if request.method == 'POST':
        key = "https://api.coinmarketcap.com/v1/ticker/?limit=10" + currency
        get_data = key.json()
        data = {
            "currency" : currency
            "price" : get_data[]
        }
    return render(request,"bitcoin.html",data)