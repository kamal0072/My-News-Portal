import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

requests.packages.urllib3.disable_warnings()

from django.contrib.auth.forms import UserCreationForm
def admin_login(request):
	form=UserCreationForm()
	return render(request,'news/login.html',{'fm':form})


import datetime
def news_list(request):
		dt=datetime.datetime(2021,12,3)
		headlines = Headline.objects.all()[::-1]
		context = {
			'object_list': headlines,
			'dt':dt,
		}
		return render(request, "news/home.html", context)

def scrape(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	url = "https://www.theonion.com/"

	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	News = soup.find_all('div', {"class":"curation-module__item"})
	for artcile in News:
		main = artcile.find_all('a')[0]
		link = main['href']
		image_src = str(main.find('img')['srcset']).split(" ")[-4]
		title = main['title']
		new_headline = Headline()
		new_headline.title = title
		new_headline.url = link
		new_headline.image = image_src
		new_headline.save()
	return redirect("../")

