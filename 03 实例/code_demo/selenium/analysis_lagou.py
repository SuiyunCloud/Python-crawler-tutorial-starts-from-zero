import pandas as pd
import jieba
import jieba.analyse
from itertools import chain
from collections import Counter
import json

def read_first_run():
    data = pd.DataFrame()
    import json
    with open('first_run.json', 'r') as fp:
        json_data = json.load(fp)

    for index, job in enumerate(json_data['items']):
        job['key'] = str(job['key'])
        data = data.append(pd.DataFrame(job, index=[index]))
    data.drop_duplicates(subset='url',keep='first', inplace=True)
    return data


def cut_word(data):
    jieba.analyse.set_stop_words('stop.txt')
    # jieba.analyse.set_stop_words('stop2.txt')
    data['cut'] = data['detail'].map(jieba.analyse.extract_tags)
    return data


def count_keyword(series):
    words = []
    for generator in list(series.values):
        tmp = [w.lower() for w in generator]
        words.extend(tmp)
    counter = Counter(words)
    return counter


if __name__ == '__main__':
    raw_data = read_first_run()
    data = cut_word(raw_data)
    counter = count_keyword(data['cut'])
    # counter.pop('')
    with open('high_freq.json', 'a') as fp:
        fp.write(str(counter.most_common(100)))

