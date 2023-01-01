import requests

API_KEY = "e68fb5ae8958b7fc23a755b9da9d2116"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city= input("Enter a city name: ")

request=f"{BASE_URL}?appid={API_KEY}&q={city}"

response=requests.get(request)

if response.status_code==200:
    data=response.json()
    weather=data['weather'][0]['description']
    temp= round((data['main']['temp'])-273, 2)
    hum=data['main']['humidity']
    
    print("Weather: ", weather)
    print("Temperature: "+ str(temp) + "C")
    print("Humidity: ", hum, '%')

else:
    print("An error occured")
    

