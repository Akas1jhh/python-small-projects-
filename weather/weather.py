import requests

# api key 
API_KEY = '92e6cb41bd819b788a1e73b28e29b9a1'

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# taking city from user input
city = input('Enter City Name: ')

# creating requst_url
requst_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

#getting the response from requst_url
response = requests.get(requst_url)

# if the city name is found
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather : ", weather)
    temperature = round(data['main']['temp'] - 273.15, 2)
    print("Temperature :" ,temperature, "°C")

else:
    print('request failed')
