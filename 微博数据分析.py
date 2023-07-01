import jieba

import collections

import re

from pyecharts.charts import WordCloud

from pyecharts.globals import SymbolType

from pyecharts import options as opts

from pyecharts.globals import ThemeType

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
# 去除分词结果中的无用词汇

def deal_txt(seg_list_exact):
    result_list = []
    with open('stop_words.txt', encoding='utf-8') as f:
        con = f.readlines()
        stop_words = set()
        #set函数用于创建一个无序的、不重复（可利用这一点删除重复元素）元素集，并可进行与或等运算。
        # x = set('abbbc')
        # y = set('deefffgg')
        # print(x, y)
        # {'c', 'b', 'a'}
        # {'e', 'd', 'g', 'f'}
        for i in con:
            i = i.replace("\n", "")  # 去掉读取每一行数据的\n
            stop_words.add(i)
    for word in seg_list_exact:
# 设置停用词并去除单个词
        if word not in stop_words and len(word) > 1:
            result_list.append(word)

    return result_list;
# 渲染词云

def render_cloud(word_counts_top100):

    word1 = WordCloud(init_opts=opts.InitOpts(width='1350px', height='750px', theme=ThemeType.MACARONS))

    word1.add('词频', data_pair=word_counts_top100,word_size_range=[15, 108], textstyle_opts=opts.TextStyleOpts(font_family='cursive'),shape=SymbolType.DIAMOND)

    word1.set_global_opts(title_opts=opts.TitleOpts('微博云图'),toolbox_opts=opts.ToolboxOpts(is_show=True, orient='vertical'),tooltip_opts=opts.TooltipOpts(is_show=True, background_color='red', border_color='yellow'))

# 渲染在html页面上

    word1.render("微博云图.html")
def draw_bar(key_name, key_values):
    # my_font = font_manager.FontProperties(fname='./STHeiti Medium.ttc')  # 设置中文字体（图表中能显示中文）
    #
    # # 为了坐标轴上能显示中文
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False

    # print(dm_com_score)
    # **********************************************************************综合评分和播放量对比
    # *******综合评分条形图
    # fig, ax1 = plt.subplots()
    plt.bar(key_name, key_values, color='red')  # 设置柱状图
    plt.title('微博高频词', fontproperties=my_font)  # 表标题
    ax1.tick_params(labelsize=6)
    plt.xlabel('热词')  # 横轴名
    plt.ylabel('综合数量')  # 纵轴名
    plt.xticks(rotation=90, color='green')  # 设置横坐标变量名旋转度数和颜色

    # # *******播放量折线图
    # ax2 = ax1.twinx()  # 组合图必须加这个
    # ax2.plot(dm_play, color='cyan')  # 设置线粗细，节点样式
    # plt.ylabel('播放量')  # y轴

    # plt.plot(1, label='综合评分', color="red", linewidth=5.0)  # 图例
    # plt.plot(1, label='播放量', color="cyan", linewidth=1.0, linestyle="-")  # 图例
    # plt.legend()

    plt.savefig(r'E:1.png', dpi=1000, bbox_inches='tight')  # 保存至本地

    plt.show()


if __name__ == '__main__':

# 读取弹幕文件

    with open('jdcomment33.txt', encoding='utf-8') as f:

        data = f.read()



# 文本预处理去除一些无用的字符只提取出中文出来

    new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)#去除数字

    new_data = " ".join(new_data)

    # jieba分词将整句切成分词

    seg_list_exact = jieba.cut(new_data, cut_all=True)

    # 去掉无用词汇

    final_list = deal_txt(seg_list_exact)

    # 筛选后统计

    word_counts = collections.Counter(final_list)
    # 获取前100最高频的词

    word_counts_top200 = word_counts.most_common(200)

    # 可以打印出来看看统计的词频

    print(word_counts_top200)

  #  渲染词云
    lista=[]
    listb=[]
    render_cloud(word_counts_top200)

    for i in word_counts_top200:
        lista.append(i[0])
        listb.append([i[1]])
    print(lista)
    # draw_bar(lista, listb)

