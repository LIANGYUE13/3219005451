import sys
import gensim
import jieba
import re
import os

#获取文本路径，很简单的读取文本的方法
def get_file(path):
    string = ''
    f = open(path, 'r', encoding='UTF-8') #设置UTF-8以防乱码
    line = f.readline()
    while line:
        string = string + line
        line = f.readline()
    f.close()  #读完记得关闭以免占用资源
    return string


