#!/usr/bin/env python
# coding: utf-8

# 3219005451 肖丽萍 19级信息安全1班
# 软件工程个人项目 论文查重
import gensim
import jieba
import re
import os


def get_content(path):
    # 文本处理，将我们的文本处理为字符串，并且过滤掉标点符号
    string = ''
    file = open(path, 'r', encoding='UTF-8')
    one_line = file.readline()
    while one_line:
        string += one_line
        one_line = file.readline()
    # 调用标点符号过滤函数
    string = Symbol_filter(string)
    file.close()
    return string


# 过滤器
def Symbol_filter(str):
    # 使用正则表达式过滤，保留字母与汉字
    result = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]").sub("", str)
    return result


# 分词
def turn_vector(str):
    # 将字符串使用jieba.lcut切片用list保存
    string = jieba.lcut(str)
    return string


# 计算相似度
def similarity_vul(str_x, str_y):
    texts = [str_x, str_y]
    # 使用gensim.corpora获得语料库
    dictionary = gensim.corpora.Dictionary(texts)
    # 利用doc2bow作为词袋模型
    corpus = [dictionary.doc2bow(text) for text in texts]
    # 通过token2id得到特征数（字典里面键的个数）
    num_features = len(dictionary.token2id.keys())
    sim = gensim.similarities.Similarity('-Similarity-index', corpus, num_features)
    # 获取文章相似度
    test_corpus = dictionary.doc2bow(str_x)
    cosine_sim = sim[test_corpus][1]
    return cosine_sim


# 主函数
def main_test():
    # 为了方便命令行输入，这里加了一些提示性文本使用户体验更加友好
    txt_1 = input("参考论文的绝对路径：")
    txt_2 = input("待检察文件的绝对路径：")
    # 输出结果的文件路径
    save_path = input("保存结果的绝对路径：")

    # 简单的异常处理
    if not os.path.exists(txt_1):
        print("参考论文文件不存在！")
        exit()
    if not os.path.exists(txt_2):
        print("待检察文件不存在！")
        exit()
    if not txt_1.endswith('.txt'):
        print("参考论文文件格式错误!")
        exit()
    if not txt_2.endswith('.txt'):
        print("待检察文件格式错误!")
        exit()
    if not save_path.endswith('.txt'):
        print("输出结果文件格式错误!")
        exit()
    if os.path.getsize(txt_1) == 0:
        print("参考论文文件为空！")
        exit()
    if os.path.getsize(txt_2) == 0:
        print("待检察文件为空！")
        exit()

    # 将文本提取出来，去除标点符号，转化为字符串
    str_1 = get_content(txt_1)
    str_2 = get_content(txt_2)
    # 获取分词后的字符串
    vector_1 = turn_vector(str_1)
    vector_2 = turn_vector(str_2)
    # 计算相似度
    similarity = similarity_vul(vector_1, vector_2)
    print("这两篇文章的相似度： %.4f" % similarity)
    #  将相似度结果写入指定文件
    f = open(save_path, 'w', encoding="UTF-8")
    f.write("这两篇文章的相似度： %.4f" % similarity)
    f.close()


if __name__ == '__main__':
    main_test()
