from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    url = "https://timesofindia.indiatimes.com/"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")

    card = {}

    counter = 0
    for divtag in soup.find_all('div', {'class': 'col_l_6'}):
        for atag in divtag.find_all('a', {'class': 'Hn2z7'}):
            imgtag = atag.find('img')
            card[counter]  = {'title':imgtag['alt'], 'link':atag['href']}
            counter += 1

    length = len(card)
    card['length'] = [x for x in range(length)]

    context = {
        'card': card,
    }

    return render(request, 'index.html', context=context)