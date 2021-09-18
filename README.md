# 3219005451
# 第一次个人编程作业


| 这个作业属于哪个课程 | [软件工程](https://edu.cnblogs.com/campus/gdgy/InformationSecurity1912-Softwareengineering) |
| -------------------- | :----------------------------------------------------------: |
| 这个作业要求在哪里   | [个人项目作业](https://edu.cnblogs.com/campus/gdgy/InformationSecurity1912-Softwareengineering/homework/12146) |
| 这个作业的目标       | 实现查重算法+单元测试+性能分析+异常处理+记录PSP表格+熟悉Git  |

* 项目代码已上传到[作业GitHub](https://github.com/LIANGYUE13/3219005451)，使用python3实现

<由于之前没有接触过python，在开始本项目之前花费了比较多的时间学习新语言>


---



## 一、PSP表格

| PSP2.1                                  | Personal Software Process Stages        | 预估耗时（分钟） | 实际耗时（分钟） |
| --------------------------------------- | --------------------------------------- | :--------------: | :--------------: |
| Planning                                | 计划                                    |        30        |        30        |
| · Estimate                              | · 估计这个任务需要多少时间              |        30        |        30        |
| Development                             | 开发                                    |       1515       |       1980       |
| · Analysis                              | · 需求分析 (包括学习新技术)             |       850        |       1150       |
| · Design Spec                           | · 生成设计文档                          |        20        |        15        |
| · Design Review                         | · 设计复审                              |        10        |        5         |
| · Coding Standard                       | · 代码规范 (为目前的开发制定合适的规范) |        15        |        10        |
| · Design                                | · 具体设计                              |       120        |       100        |
| · Coding                                | · 具体编码                              |       350        |       550        |
| · Code Review                           | · 代码复审                              |        30        |        20        |
| · Test                                  | · 测试（自我测试，修改代码，提交修改）  |       120        |       130        |
| Reporting                               | 报告                                    |        75        |        65        |
| · Test Repor                            | · 测试报告                              |        30        |        30        |
| · Size Measurement                      | · 计算工作量                            |        15        |        15        |
| · Postmortem & Process Improvement Plan | · 事后总结, 并提出过程改进计划          |        30        |        20        |
|                                         | · 合计                                  |       1620       |       2075       |









---



## 接口的设计与实现过程

### 代码组织（类、函数及之间的关系、关键函数流程图、算法关键、独到之处）

  	 通过上网了解到论文查重算法实际上就是计算文本的相似度，通过比对各种算法的优缺点，本项目中最终参考了[python实现余弦相似度文本比较](https://blog.csdn.net/weixin_34186931/article/details/93403206)，具体过程参考该博客。

​		**整体思路：**读取文件路径，将文件字节流转换成字符串，使用jieba分词后过滤掉标点符等，，根据分词词典通过doc2bow稀疏向量生成语料库，然后直接调用similarity获取文本相似度（省略了计算TF、IDF值、文档向量、权重等步骤），最后将输出结果保存到指定路径。

* 调用库：jieba、re、gensim、os

### 函数：

1. **get_content()**中读取目标文件字节流，转换成字符串后，调用过滤函数**Symbol_filter()**。

```python
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
```

2. **turn_vector()**函数调用jieba.lcut切片后用list保存

```python
# 分词
def turn_vector(str):
    # 将字符串使用jieba.lcut切片用list保存
    string = jieba.lcut(str)
    return string
```

3. **算法关键：similarity_vul()**函数调用gensim.corpora获得语料库，利用doc2bow作为词袋模型，调用gensim.similarities.Similarity计算文章相似度

```python
# 计算相似度
def similarity_vul(str_x, str_y):
    texts = [str_x, str_y]
    # 使用gensim.corpora获得语料库
    dictionary = gensim.corpora.Dictionary(texts)
    num_features = len(dictionary.token2id)
    # 利用doc2bow作为词袋模型
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features)
    # 获取文章相似度
    test_corpus_1 = dictionary.doc2bow(str_x)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim
```

### 流程图：

此处利用pycharm自带插件profile生成的函数调用图





## 接口部分的性能改进

记录在改进计算模块性能上所花费的时间，描述你改进的思路，并展示一张性能分析图（由VS 2017/JProfiler的性能分析工具自动生成），并展示你程序中消耗最大的函数。





## 部分单元测试展示

展示出项目部分单元测试代码，并说明测试的函数，构造测试数据的思路。并***\*将单元测试得到的测试覆盖率截图\****，发表在博客中





## 部分异常处理说明

在博客中详细介绍每种异常的设计目标。每种异常都要选择一个单元测试样例发布在博客中，并指明错误对应的场景





1. 算法的性能（耗费的时间、占用的系统资源、准确度等）**（20'）**
2. 代码的可读性（至少要有点注释吧？）**（10'）**
3. 变量、函数、类命名的规范化**（10'）**
