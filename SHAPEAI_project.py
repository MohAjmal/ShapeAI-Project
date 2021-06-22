#importing required modules
import requests
from datetime import datetime

#required inputs and api key
api_key = "f16235f0c71d46d86d67c62d02cf1a16"
city = input("Enter city name: ")

#requesting data
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#assigning variables to required data
city_temp = ((api_data['main']['temp']) - 273.15)
wthr_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
windspd = ((api_data['wind']['speed']) * 3.6)   #converting meter per sec to kmph
date_time = datetime.now().strftime("%d %b %Y  | %I:%M:%S %p")

#displaying required data
print("WEATHER STATS FOR ", city.upper()," ON ", date_time)
print()
print("Temperarure is             :  {:.2f} deg C".format(city_temp))
print("Weather description    :  ", wthr_desc.title())
print("Humidity                        :  ", hmdt, "%")
print("Wind Speed                   :  ", windspd," kmph")

#writing data to text file
with open("weatherdata.txt", "a") as wdfile:
    wdfile.write(str(city_temp))
    wdfile.write(wthr_desc)
    wdfile.write(str(hmdt))
    wdfile.write(str(windspd))
    wdfile.write(str(date_time))
    wdfile.close()
    


