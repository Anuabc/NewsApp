from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    
    header ={
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows"
        }

    url = "https://www.hindustantimes.com/"
    page_request = requests.get(url, headers=header)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")

    card = {}

    counter = 0

    for divtag in soup.find_all('div', {'class': 'articleClick'}):
        if 'liveStory' not in divtag['class']:
            head = divtag.find(class_="hdg3")
            title = head.get_text()
            link = divtag['data-weburl']
            imgtag = divtag.find('img')
            try:
                img = imgtag['data-src']
            except:
                img = imgtag['src']
            card[counter]  = {'title':title, 'link':link, 'img':img}
            counter += 1

    context = {
        'card': card,
    }

    return render(request, 'index.html', context=context)