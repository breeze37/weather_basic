import requests

API_KEY = "ebfdc2c1224bd117c2b12f65b342efdc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

CITY = input("Enter the desired city : ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={CITY}"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]['description']
    temperature = round(data["main"]["temp"]-273.15, 2)
    
    print ("weather : ", weather)
    print ("temperature : ", temperature, "C")
else:
    print("Error")

     