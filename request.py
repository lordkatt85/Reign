#Requests

import requests

import user_interface

lat = 51.50
lon = 0.12
APIKEY = "b903d80ef10ec6f709b4272d8fae5d1a"

try:
	response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&appid="+APIKEY)

	#Checks if the authorozisation was done
	print(response)

	with open("weather.json","w+") as file:
		file.write(response.text)
		print("completed")
		print(response.text)

except:
	print("Network Error... Please try again")
	
