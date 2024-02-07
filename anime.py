import requests
from episode import Episode

def remove_quotes(s):
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    return s

def search(type, title, num):
    url = "https://api.anify.tv/search/"+type+"/"+title+"/1/"+str(int(num))
    response = requests.get(url)
    data = response.json()
    results = [{'id': result['id'], 'title': result['title']} for result in data['results']]
    return results

def info(id):
    id  = remove_quotes(id)
    url = "https://api.anify.tv/info/"+str(id)
    response = requests.get(url)
    data = response.json()
    return data

def episodes(id):
    id  = remove_quotes(id)
    url = "https://api.anify.tv/episodes/"+str(id)
    response = requests.get(url)
    data = response.json()
    arr = []
    for x in data:
        for y in x['episodes']:
            arr.append(Episode(x['providerId'], y['id'], y['title'], y['number'], id))
    return arr