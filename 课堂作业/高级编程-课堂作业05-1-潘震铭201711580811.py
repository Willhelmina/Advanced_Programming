#!/usr/bin/env python
# coding: utf-8
import os
import json
import pickle

#读取文件
def read_txt():
    filenames = os.listdir(r'.\books')
    text_info = {}
    for file in filenames:
        file_path = r'.\books\{}'.format(file)
        with open(file_path, 'r') as f:
            #删除文本中的换行符和空格
            text = f.read().replace('/n','').replace(' ','')
            text_info[file] = len(text) #将文件名和字数存储到字典中
    #json格式保存到txt文件中
    json_totxt(text_info)
    #二进制格式保存到txt文件中
    pickle_totxt(text_info)
    return text_info

#json格式保存到txt文件中 
def json_totxt(info):
    info_json = json.dumps(info)
    with open('json.txt','w') as f:
        f.write(info_json)
    print('保存为json格式文件成功！')

#二进制格式保存到txt文件中    
def pickle_totxt(info):
    with open('pickle.txt','wb') as f:
         pickle.dump(info, f)
    print('保存为pickle二进制文件成功！')

#主函数入口
if __name__ == '__main__':
    print(read_txt())