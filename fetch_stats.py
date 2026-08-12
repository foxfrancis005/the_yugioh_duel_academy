import urllib.request, json
url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?archetype=Rikka'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read().decode('utf-8'))
    for item in data['data']:
        print(f"{item['name']} - {item['type']} - Lvl/Rank: {item.get('level')} - ATK: {item.get('atk')} - DEF: {item.get('def')}")
except Exception as e:
    print(e)
