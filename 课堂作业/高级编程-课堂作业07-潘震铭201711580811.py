#!/usr/bin/env python
# coding: utf-8
import requests
import requests
def urlQuery(url):

    headers = get_headers(url)

    res = requests.get(url)

    info = res.text
    print("连接状态码：", res.status_code)
    print("返回对象属性", type(info))
    print("保存成功:", to_txt(info, url))
    return info
    
def to_txt(infomation, url):
    if 'www' in url:
        file_name = url[url.index('www'):url.index('com')-1].split('.')[1] + '_info.txt'
    else:
        file_name = url[url.index('//')+2:url.index('com')-1] + '_info.txt'
    with open(file_name, 'w+', encoding='utf-8') as f:
        f.write(infomation)
    return file_name
 
def get_headers(url):
    res = requests.head(url)
    return res.headers
    
if __name__ == '__main__':
    url1 = 'https://www.guazi.com/bj/buy/'
    url2 = 'https://bj.fang.com/quanwangso/search.html?city=bj&refer=sy_search'
    urlQuery(url1)
    urlQuery(url2)

