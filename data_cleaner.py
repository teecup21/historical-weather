import json
from datetime import datetime
from collections import defaultdict
with open("weather.json") as file:
    data = json.load(file)
#data is a list of 3 dictionaries. The dictionaries are duplicates so we only need one of the dictionaries
data=data[0]
#the first dict is some details on the data (lat, long, time captured, etc). 
#the second dict is "hourly" which is every hour and its corresponding humidity. Format: 2025-02-01T00:00 
hours_humid = data["hourly"]
timestamps = hours_humid['time']
humidity_at_hour=hours_humid['relative_humidity_2m']
daily_humidity = defaultdict(list)
for timestamp, humidity_at_hour in zip(timestamps, humidity_at_hour):
    timestamps_formatted = datetime.fromisoformat(timestamp)
    date=timestamps_formatted.date()
    daily_humidity[date].append(humidity_at_hour)

for key in daily_humidity:
    daily_humidity[key]=round(sum(daily_humidity[key])/len(daily_humidity[key]),2)
#print(daily_humidity)
daily_temp_precip_wind = data["daily"]

dailyweather=defaultdict(dict)
for date in daily_temp_precip_wind['time']: #create a dictionary with the date as the key and the weather data as the value
    index=daily_temp_precip_wind['time'].index(date)
    date = datetime.fromisoformat(date).date()
    dailyweather[date]={
        "temperature":daily_temp_precip_wind['temperature_2m_mean'][index],
        "precipitation":daily_temp_precip_wind['precipitation_sum'][index],
        "wind_speed":daily_temp_precip_wind['wind_speed_10m_max'][index], 
        "humidity":daily_humidity[date]
    }
