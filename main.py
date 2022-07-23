
import requests
from pprint import pprint



def intelligence_superheroes(name_heroes):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    all_superheroes = requests.get(url)
    all_superheroes = all_superheroes.json()
    for superheroes in all_superheroes:
        if superheroes["name"] == name_heroes:
            intelligence_superheroes = superheroes["powerstats"]["intelligence"]
            return intelligence_superheroes

def max_intelligence(heroes1, heroes2, heroes3):
    dict_heroes = {}
    max_intelligence = 0
    heroes_max_intelligence = None
    dict_heroes[heroes1] = intelligence_superheroes(heroes1)
    dict_heroes[heroes2] = intelligence_superheroes(heroes2)
    dict_heroes[heroes3] = intelligence_superheroes(heroes3)
    for heroes, intelligence in dict_heroes.items():
        if intelligence > max_intelligence:
            max_intelligence = intelligence
            heroes_max_intelligence = heroes

    return f" Максимальный интеллект у супергероя {heroes_max_intelligence} - {max_intelligence}"

pprint(max_intelligence( "Hulk", "Captain America", "Thanos"))

#Задание 2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {"path": disk_file_path, "overwrite": "True"}
        response = requests.get(upload_url, headers=headers, params=params)
        response = response.json()
        href = response.get("href", "")
        response = requests.put( href, data=open("net_23.07.txt", 'rb'))
        return response.raise_for_status()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "23.07/net_23.07.txt"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


