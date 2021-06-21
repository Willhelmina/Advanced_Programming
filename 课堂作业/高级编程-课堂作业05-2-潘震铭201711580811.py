#!/usr/bin/env python
# coding: utf-8
import argparse
#获取输入的命令行参数，并赋值给filepath字段
parser = argparse.ArgumentParser()
parser.add_argument('filepath')
args = parser.parse_args()
filepath = args.filepath
try:
    text, filename = '', ''
    #打开文件，读取文件中的文本
    with open(filepath,'r') as f:  
        filename = filepath.split('\\')[-1].split('.')[0]
        print("文件读取成功:", filename)        
        text = f.read().replace('/n','').replace(' ','')
    #创建两个文件流，一个存储中文，一个存储英文
    CN_filename = filename + '_CN.txt'
    EN_filename = filename + '_EN.txt'
    CN_fo = open(CN_filename, 'w+')
    EN_fo = open(EN_filename, 'w+')
    #对字符进行遍历
    for char in text:
        #判断当前字符是否是中文
        if '\u4e00' <= char <= '\u9fa5':
            CN_fo.write(char)
        #判断当前字符是否是英文
        elif (u'\u0041'<= char <= u'\u005a') or (u'\u0061'<= char <= u'\u007a'):
            EN_fo.write(char)
    #关闭所有的文件流
    CN_fo.close()
    EN_fo.close()
    print("保存成功\n英文保存文件名：{}\n中文保存文件名：{}".format(CN_filename, EN_filename))

#捕捉文件不存在异常
except IOError:
    print("FileNotFoundError: 没有找到文件或读取文件失败！")
