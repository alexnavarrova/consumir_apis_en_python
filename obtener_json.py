import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    # url = 'http://httpbin.org/get?nombre=alexnavarrova&curso=python'
    args = {
        'name': 'Alexander Navarro',
        'course': 'Python',
        'level': 'Intermedio'
    }

    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        # response_json = response.json() # Dic
        # origin = response_json['origin']
        # print(origin)

        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)