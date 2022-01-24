import requests
from database import article

elements = []
n = 0
item_id = 0
total = requests.get("https://api.spaceflightnewsapi.net/v3/articles/count").json()

while n < total+400:
    response = requests.get(f"https://api.spaceflightnewsapi.net/v3/articles?_limit=400&_start={n}")
    data = response.json()
    if data == []:
        break
    for item in data:
        item['id'] = item_id
        item_id += 1
        elements.append(item)
    n += 400
print("Inserindo dados no banco...")
article.insert_many(elements)