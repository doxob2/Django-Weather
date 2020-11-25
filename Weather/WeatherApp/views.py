from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .admin import City
from .services import get_city_weather
from .forms import CityForm

# Create your views here.

def main(request):
	cities = City.objects.all()[::-1]
	data = get_city_weather(cities)
	return render(request, 'weather.html', data)


def add_city_in_db(request):
	available_data = [i.name.lower() for i in City.objects.all()]
	if (request.method == 'POST' and request.POST['name'].lower() not in available_data):
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	return HttpResponseRedirect('/')

def delete_city_from_db(request, id):
	try:
		city = City.objects.get(id=id)
		city.delete()
		return HttpResponseRedirect('/')
	except City.DoesNotExist:
		pass

def delete_all_city_from_db(request):
	try:
		cities = City.objects.all()
		for city in cities:
			city.delete()
		return HttpResponseRedirect('/')
	except:
		pass

