import requests
from datetime import datetime

api_key = 'd732886668d0395e49adb40243417c67'
location = input("Enter the city name : ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
hmdt = api_data['main']['humidity']
weather_desc = api_data['weather'][0]['description']
wind_spd = api_data['wind']['speed']
wind_direct = api_data['wind']['deg'] 
date_time = datetime.now().strftime("%d %m %Y | %I:%M:%S %p")


report = open('report.txt','w')

report.write("------------------------------------------------------------------------------\n")
report.write("Weather Stats for - {}  || {}".format(location.upper(), date_time)+'\n')
report.write("------------------------------------------------------------------------------\n")

report.write("Current temperature is : {:.2f} deg C ".format(temp_city)+'\n')
report.write("Current weather desc   : "+ weather_desc +'\n')
report.write("Current Humidity       : "+ str(hmdt)+ ' %\n')
report.write("Current wind speed     : "+ str(wind_spd )+' kmph\n')
report.write("Current wind direction : "+ str(wind_direct )+' degrees\n')

report.close()


