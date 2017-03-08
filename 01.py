import requests
import json

api_url = 'https://api.vk.com/method/'
# client_id = 5899797


def make_news_list(api_url):
    news_method = 'newsfeed.search'
    params = {
        'count': 200,
        'q': 'python, программирование'
    }
    all_news = json.loads(requests.get(api_url + news_method, params).text)
    news_list = []
    for news in all_news['response']:
        if type(news) == dict:
            news_list.append(news)
    return news_list


def write_to_file(news_list):
    with open('news_base.json', 'w', encoding='utf8') as file:
        json.dump(news_list, file, ensure_ascii=False, indent=2)

write_to_file(make_news_list(api_url))
print('eee')
