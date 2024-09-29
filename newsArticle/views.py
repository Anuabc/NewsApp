from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
import json

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

    p = soup.find_all('p', class_='')

    for i in p:
        news.append(str(i))

    for ind, j in enumerate(news):
        text = ''
        i = 0
        while i != len(j):
            if j[i] == '<' and j[i+1]=='a':
                for x in range(i, len(j)):
                    if j[x] == ">":
                        i+=1
                        break
                    i+=1
            else:
                text += j[i]
                i+=1

        text = text.replace('</a>', '')
        news[ind] = text


    context = {
        'heading':heading,
        'content':news,
    }


    return render(request, 'article.html', context=context)

def meaning(request):
    word = request.GET.get('word', '').strip()
    if word:
        req = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if req.status_code == 200:
            data = req.json()

            meaning = {}

            for x in data:
                for i in x['meanings']:
                    part = []
                    for j in i['definitions']:
                        part.append(j['definition'])
                    meaning[i['partOfSpeech']] = part

            # data = req.json()
            # meaning = data[0]['meanings'][0]['definitions'][0]['definition']
            return JsonResponse({'meaning': meaning})
        return JsonResponse({'meaning': None})

            # return JsonResponse({'meaning': definition})

    return redirect('home')