from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    
    header ={
        "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "referer": "https://www.hindustantimes.com/india-news/page-1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        }

    url = "https://www.hindustantimes.com/india-news/page-1"
    page_request = requests.get(url, headers=header)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")

    card = {}

    counter = 0

    for divtag in soup.find_all('div', {'class': 'articleClick'}):
        link = divtag['data-weburl']
        imgtag = divtag.find('img')
        img = imgtag['src']
        title = imgtag['alt']
        card[counter]  = {'title':title, 'link':link, 'img':img}
        counter += 1

    length = len(card)
    card['length'] = [x for x in range(length)]

    context = {
        'card': card,
    }

    return render(request, 'index.html', context=context)