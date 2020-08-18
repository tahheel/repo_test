# import data

# #print (data.weather)

# weather_data = data.weather

# print(weather_data.keys())
# #print(weather_data["list"])

# forcast_container = weather_data["list"]
# print(type(forcast_container))
# print(len(forcast_container))

# first_item_in_forcast_container = forcast_container[0]
# print(first_item_in_forcast_container.keys())

# ##ATTEMPT TO ACCESS REQD VALUES FROM FIRST ITEM IN FORCAST LIST:

# time = first_item_in_forcast_container['dt_txt']
# temp = first_item_in_forcast_container['main']['temp']
# wind = first_item_in_forcast_container['wind']['speed']
# clouds = first_item_in_forcast_container['weather']
# pressure = first_item_in_forcast_container['main']['pressure']
# print(clouds[0]['description'])

# cloud_description = clouds[0]['description']

# tion,pressure)print(time,temp,wind,cloud_descrip

# print(time,temp,wind,cloud_description,pressure)
# print("Time".center(20),"Temp".center(7),"Pressure".center(10),"Wind".center(10),"Cloud_desc".center(19),sep = " | ")
# print("-"*70)

# def kelvin_to_celsius(k):
# 	return round(k - 273.5, 2) 


# ## ATTEMPT TO ACCESS FOR ALL 40 FORCAST IN LIST:

# for forcast in forcast_container:
#     time = forcast['dt_txt']
#     temp = forcast['main']['temp']
#     pressure = forcast['main']['pressure']
#     wind = forcast['wind']['speed']
#     clouds = forcast['weather']
#     cloud_description = clouds[0]['description']
    
#     print(f"{time}".center(20),f"{temp} k".center(7), f"{kelvin_to_celsius(temp)} c".center(7), f"{pressure}mbar".center(10),f"{wind}km/hr".center(10),f"{cloud_description}".center(19),sep = " | ")





# import requests

# r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Lagos,&APPID=cccf7df52d9c4ec0b3af9252c4867a17')
# #print(r.text)
# weather_data = r.text
# print(weather_data)
# print((type)(weather_data))

# import ast
# owm_data = ast.literal_eval(weather_data)
# #print(type(owm_data))
# print(owm_data.keys())

# cloud_description = (owm_data['weather'][0]['description'])
# pressure = (owm_data['main']['pressure'])
# wind = (owm_data['wind']['speed'])
# time = (owm_data['timezone'])
# temperature = (owm_data['main']['temp'])
# clouds = (owm_data['weather'])


import pyowm
