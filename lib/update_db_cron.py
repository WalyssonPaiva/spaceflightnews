import requests
from database import article

def update_db():
    elements = []
    n = 0
    item_id = article.get_next_id()
    total = requests.get("https://api.spaceflightnewsapi.net/v3/articles/count").json()
    stop = False
    while n < total+400 and not stop:
        response = requests.get(f"https://api.spaceflightnewsapi.net/v3/articles?_limit=400&_start={n}")
        data = response.json()
        if data == []:
            break
        for item in data:
            if not article.get_by_title(item['title']):
                item['id'] = item_id
                item_id += 1
                elements.append(item)
            else:
                stop = True
                break
        n += 400
    if elements:
        print("Inserindo novos artigos no banco...")
        article.insert_many(elements)
    else:
        print("Sem novos artigos!")
    print("Concluído!")