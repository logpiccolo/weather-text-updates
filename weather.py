import requests
import smtplib
import socket

socket.getaddrinfo('localhost', 25)

url = 'https://api.openweathermap.org/data/2.5/onecall?lat=2&lon=-2&exclude=hourly,minutely&appid={API_KEY}&units=imperial'

response = requests.get(url)
weather_json = response.json()
degree = ' Degrees'

#obtains current and daily weather information
current_weather = weather_json['current']
todays_weather = weather_json['daily'][0]

#saving the current temp, feels like, wind speed, direction of wind, and current precip type, if any
#later should update this for humidity, dew point
current_temp = current_weather['temp']
feels_like = current_weather['feels_like']
wind_speed = current_weather['wind_speed']
current_precipitation_type = current_weather['weather'][0]['description']

#saving forecast high and low, as well as what type of precipitation to be had
#later should update this for humidity, dew point
forecast = weather_json['daily'][0]['temp']
forecast_high = forecast['max']
forecast_low = forecast['min']
forecast_precipitation = weather_json['daily'][0]['weather'][0]['main']

message = 'Current temperature for your area: ' + str(current_temp) + degree + '\nFeels like: '+ str(feels_like) + degree + '\nWind speed: ' + str(wind_speed) + 'MPH\nCurrent Precipition: '+ str(current_precipitation_type) + '\n\nHigh for today: ' + str(forecast_high) + degree + '\nLow:' + str(forecast_low) + degree + '\nPreciptation expected today: '+ forecast_precipitation

server = smtplib.SMTP('64.233.184.108', 587)
server.starttls()
server.login('youremail@email.com', 'yourpassword')
server.sendmail('youremail@email.com', 'recipient', 'Weather\n\n' + message)

#joshweather567@gmail.com


from bs4 import BeautifulSoup
import requests, re

#HOW TO SCRAPE ONE PAGE OF QUOTES
'''
req = requests.get("https://transcripts.foreverdreaming.org/viewtopic.php?t=25301")
soup = BeautifulSoup(req.content, "html.parser")

page_text = soup.get_text()

regex = (r'Michael: \s*([^\n\r]*)')
match = re.findall(regex, page_text)
print(match)
'''

#HOW TO SCRAPE MULTIPLE PAGES?
url_for_multiple_quotes = "https://transcripts.foreverdreaming.org/viewforum.php?f=574&sid=34f5b8811213289fa5f508f836af3f4f"
req = requests.get(url_for_multiple_quotes)
soup = BeautifulSoup(req.content, "html.parser")
url_list = []
for link in soup.find_all("a"):
    get_links = link.get('href')
    print(type(get_links))
#     # url_list.append(test)

# print(url_list)
#remove each string that does not match the pattern of ./viewtopic.php?t=25498



# add them to the end of https://transcripts.foreverdreaming.org/; might look like ./viewtopic.php?t=25498
