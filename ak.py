import jieba

from 爬虫5.微博数据分析 import render_cloud


def word_extract(retrun=None):
    # 读取文件
    corpus = []
    path = 'C:/Users/Yangfanfan/Desktop/129杨帆/二、知识的综合运用/data/甘肃省政府工作报告.txt'
    content = ''
    for line in open(path, 'r', encoding='utf-8', errors='ignore'):
        line = line.strip()
        content += line
    corpus.append(content)
    # 加载停用词
    stop_words = []
    path = 'C:/Users/Yangfanfan/Desktop/129杨帆/二、知识的综合运用/data/stopword.txt'
    for line in open(path, encoding='utf-8'):
        line = line.strip()
        stop_words.append(line)
        # jieba分词
    split_words = []
    word_list = jieba.cut(corpus[0])
    render_cloud(word_list)
    for word in word_list:
        if word not in stop_words:
            split_words.append(word)
    # 提取前10个高频词
    dic = {}
    word_num = 10
    for word in split_words:
        dic[word] = dic.get(word, 0) + 1
    freq_word = sorted(dic.items(), key = lambda x: x[1],
                       reverse=True) [: word_num]
    print('样本：' + corpus[0])
    print('样本分词效果：' + '/ '.join(split_words))
    print('样本前10个高频词：' + str(freq_word))
