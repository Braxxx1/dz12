import requests


def get_requests():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    all_hero = {"Hulk": 0, 'Captain America': 0 , 'Thanos': 0}
    response = requests.get(url)
    for i in response.json():
        if i['name'] in "Hulk Captain America Thanos":
            all_hero[i['name']] = i['powerstats']['intelligence']
    all_hero = sorted(all_hero.items(), key=lambda x: x[1])
    print(all_hero[-1][0], all_hero[-1][-1])


if __name__ == "__main__":
    get_requests()