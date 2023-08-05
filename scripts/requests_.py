import requests
import json

def get_course_json(course_url: str) -> list[dict]:
  headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
      'Accept': '*/*',
      'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
      # 'Accept-Encoding': 'gzip, deflate, br',
      'Referer': 'https://abit.etu.ru/',
      'Origin': 'https://abit.etu.ru',
      'Connection': 'keep-alive',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'If-Modified-Since': 'Sat, 29 Jul 2023 21:06:06 GMT',
  }

  response = requests.get(course_url, 
                          headers=headers)
  js = json.loads(response.text)
  try:
    return js['data']['list']
  except:
    try:
      response = requests.get(course_url, 
                            headers=headers)
      js = json.loads(response.text)
      return js['data']['list']
    except:
      return []
