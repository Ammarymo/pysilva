import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
myLinks = soup.find_all('span', {'class': 'titleline'})

things = ["replit", "apple", "python","microsoft", ]
#for headings
for link in myLinks:
    text = link.text
    textList = text.split()
    containsWord = False
    for word in textList:
        if word.lower() in things: 
            containsWord = True
    if containsWord:
        print(link.text)

        myLink = link.find_all('a')
        print(myLink[0]["href"])
