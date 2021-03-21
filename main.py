from bs4 import BeautifulSoup
import requests
import json

output_json = {}

req = requests.get(f"https://www.savethechildren.org/us/what-we-do/emergency-response")

soup = BeautifulSoup(req.text, "html.parser")

containers_articles = soup.find_all("div", {"class":"container parbase"})

i = 0

for container_article in containers_articles:
    
    title = container_article.find("h3").get_text()
    paragraph = container_article.find("p").get_text()

    output_json.update({ i : {"title": title, "paragraph": paragraph} })

    i = i + 1

with open('emercencies.json', 'w') as json_file:
    json.dump(output_json, json_file)
