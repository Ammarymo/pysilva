import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Penis"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#mw-parser-output
#div
article = soup.find_all("div", {"class": "mw-parser-output"})[1]


content = article.find_all("p")

text = ""
for p in content:
  text += p.text

#todo- send this text to openAI and return a summary

refs = soup.find_all("ol", {"class": "references"})
for ref in refs:
  print(ref.text.replace("^ ", ""))
