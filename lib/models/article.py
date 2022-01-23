
def create_launch(id: str, provider: str):
    return {
        "id": id,
        "provider": provider,
    }

def create_event(id: str, provider: str):
    return {
        "id": id,
        "provider": provider,
    }

def create_article(id:int, featured:bool, provider:str, title:str, description:str, url:str, image:str, published:str, content:str, tags:list, launches:list, events:list):
    return {
        "id": id,
        "featured": featured,
        "provider": provider,
        "title": title,
        "description": description,
        "url": url,
        "image": image,
        "published": published,
        "content": content,
        "tags": tags,
        "launches": launches,
        "events": events,
    }

