import json
import xml.etree.ElementTree as ET


def open_file_and_make_news_list(file):
    file_name = file.split('.')
    if 'json' in file_name:
        with open(file, encoding='utf8') as f:
            json_data = json.load(f)
            news_list = json_data['rss']['channel']['items']
            words_in_news = []
            for news in news_list:
                words_in_news.append(news['description'])
        return words_in_news
    elif 'xml' in file_name:
        parser = ET.XMLParser(encoding='utf-8')
        tree = ET.parse(file, parser)
        root = tree.getroot()
        items_list = root.findall('channel/item/description')
        afr_news_list = []
        for description in items_list:
            afr_news_list.append(description.text)
        return afr_news_list


def make_list_of_words(str_list):
    news_words = []
    for news in str_list:
        words_in_news = news.split(' ')
        for word in words_in_news:
            if len(word) > 6:
                news_words.append(word)
    return sorted(news_words)


def print_top_10(words_list):
    top_words_dict = {}
    for word in words_list:
        if word in top_words_dict:
            top_words_dict[word] += 1
        else:
            top_words_dict[word] = 1
    sorted_top = sorted(top_words_dict.items(), key=lambda i: i[1], reverse=True)
    print('Топ 10 самых часто встречающихся в новостях слов:')
    for i, el in enumerate(sorted_top[:10]):
        print(str(i + 1) + '.', el[0], ':', el[1])


list_of_words = open_file_and_make_news_list('newsafr.xml')
# list_of_words = open_file_and_make_news_list('newsafr.json')
print_top_10(make_list_of_words(list_of_words))
