from django.shortcuts import render, redirect, HttpResponse
import requests
from bs4 import BeautifulSoup

# Create your views here.
def article(request, link):
    header ={
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "Sec-GPC": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows"
    }

    response = requests.get(link, headers=header)
    data = response.content
    soup = BeautifulSoup(data, "html.parser")

    news = []

    heading = soup.find(class_='hdg1').get_text()
    print(heading)

    p = soup.find_all('p', class_='')

    for i in p:
        news.append(str(i))

    context = {
        'heading':heading,
        'content':news,
    }

    print(news)

    return render(request, 'article.html', context=context)