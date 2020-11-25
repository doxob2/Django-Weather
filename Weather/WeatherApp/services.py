import datetime

import requests

from .forms import CityForm


def get_city_weather(CityObjects):
	full_data = _get_weather_data_from_owm(CityObjects)
	date_time_server = _get_time()
	form = CityForm()

	context = {'info': full_data, 'form': form, 'time': date_time_server}

	return context


def _get_weather_data_from_owm(cities):
	'''Получение информации по городу с сайта openweathermap по токену'''

	data = []
	token = 'adf906c5e34b033aee163087e8bfa9b2'
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
	for city in cities:
		try:
			result = requests.get(url.format(city.name, token)).json()
			city_info={
					'id': city.id,
					'city':result['name'],
					'temp':result['main']['temp'],
					'status': True,
					'icon':'http://openweathermap.org/img/w/{}.png'.format(result['weather'][0]['icon']),
					}
			data.append(city_info)
		except:
			city_info={
					'city':city.name,
					'temp':'Ошибка связанная с именим',
					'status': False,
					'icon':'https://eldesalarms.com/wp-content/uploads/2015/08/error-fail-50x50.png',
					}
			data.append(city_info)

	return data



def _get_time():
	now = datetime.datetime.now()
	day = now.strftime("%d.%m.%Y")
	time = now.strftime("%H:%M")

	return([day, time])
