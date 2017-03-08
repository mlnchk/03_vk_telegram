import requests
import json


def make_news_list(api_url):
    news_method = 'newsfeed.search'
    params = {
        'count': 200,
        'q': 'python, программирование'
    }
    all_news = json.loads(requests.get(api_url + news_method, params).text)
    news_list = []
    stop_words = ['бесплатн', 'скидк', 'помощ', 'промо']
    for news in all_news['response']:
        flag = True
        if type(news) == dict:
            for stop_word in stop_words:
                if news['text'].lower().count(stop_word) != 0:
                    flag = False
            if flag:
                news_list.append(news)
                # print(news['text'].lower().count)
    return news_list


def write_to_file(news_list):
    with open('news_base.json', 'w', encoding='utf8') as file:
        json.dump(news_list, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    api_url = 'https://api.vk.com/method/'
    write_to_file(make_news_list(api_url))
    print('Done!')
