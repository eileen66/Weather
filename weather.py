import requests
import pandas as pd
from bs4 import BeautifulSoup

while True:
  period = input('Enter \'h\' for hourly weather or \'t\' for 10 day weather\n')

  if period == 'h':
    period = 'hourbyhour'
    break
  elif period == 't':
    period = 'tenday'
    break

page = requests.get('https://weather.com/weather/' + period + '/l/USNY0996:1:US')
soup = BeautifulSoup(page.content, 'html.parser')
time_frame = soup.find(class_="region region-main")

if period == 'tenday':
  time = time_frame.find_all(class_="day-detail clearfix")
  desc = time_frame.find_all(class_="description")
  temp = time_frame.find_all(class_='temp')
  precip = time_frame.find_all(class_='precip')

  time = [times.get_text() for times in time]
  desc = [descs.get_text() for descs in desc]
  temp = [temps.get_text() for temps in temp]
  precip = [precips.get_text() for precips in precip]

  desc.pop(0)
  temp.pop(0)
  precip.pop(0)

  weather = pd.DataFrame(
        {
            'Time': time,
            'Description': desc,
            'Temp': temp,
            'Precip': precip,
        })

  print(weather)    

else:
  time = time_frame.find_all(class_='dsx-date')
  desc = time_frame.find_all(class_='hidden-cell-sm description')
  temp = time_frame.find_all(class_='temp')
  precip = time_frame.find_all(class_='precip')

  time = [times.get_text() for times in time]
  desc = [descs.get_text() for descs in desc]
  temp = [temps.get_text() for temps in temp]
  precip = [precips.get_text() for precips in precip]
  
  temp.pop(0)
  precip.pop(0)

  weather = pd.DataFrame(
        {
            'Time': time,
            'Description': desc,
            'Temp': temp,
            'Precip': precip,
        })

  print(weather)