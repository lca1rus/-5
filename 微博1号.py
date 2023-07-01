import time

import requests
from multiprocessing.dummy import Pool#导出线城池模块对应的类
class jdpa(object):

    headers = {
        'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'   }

    def openfile(self, file_name='jdcomment33'):#存储

        self.fp = open(f'./{file_name}.txt', 'w', encoding='utf-8')
        print(f'正在打开文件{file_name}.txt文件!')
    def b_noe(self,url):#处理一个的数据
        reponse=requests.get(url,headers=self.headers)
        reponsedata=reponse.json()
        statuses_list=reponsedata["statuses"]
        for i in statuses_list:
            idr=i.get("topic_title")
            text_raw=i.get("text_raw")
            text_raw= ' '.join(text_raw.split('\n'))
            print(text_raw)
            # 循环写出数据
            self.fp.write(f'{idr}\t{text_raw}\n')

    def c_max(self):#选择多少页
#shift+tab 向左移动
        time.sleep(0.5)
        new_url="https://weibo.com/ajax/feed/hottimeline?since_id=0&refresh=0&group_id=102803&containerid=102803&extparam=discover%7Cnew_feed&max_id=0&count=10"
        self.b_noe(url=new_url)
            #https://club.jd.com/comment/productPageComments.action?productId=100026667884&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
    def close_files(self):
        self.fp.close()
        print('爬虫结束，关闭文件！')
j=jdpa()
j.openfile()

i=eval(input("请输入次数："))
for ii in range(i):
    time.sleep(0.5)
    j.c_max()
    print(f"********正在打印第{ii}个页面的数据********")
j.close_files()
#print(a1)
