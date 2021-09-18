import unittest
from paperpass import *


class MyTestCase(unittest.TestCase):
    test_0 = "d:/homework/test/orig.txt"
    test_1 = "d:/homework/test/orig_0.8_add.txt"
    test_2 = "d:/homework/test/orig_0.8_del.txt"
    test_3 = "d:/homework/test/orig_0.8_dis_1.txt"
    test_4 = "d:/homework/test/orig_0.8_dis_10.txt"
    test_5 = "d:/homework/test/orig_0.8_dis_15.txt"
    save = "d:/homework/test/save.txt"

    def test_01(self, orig=test_0, check=test_1):
        str1 = get_content(orig)
        str2 = get_content(check)
        text1 = turn_vector(str1)
        text2 = turn_vector(str2)
        similarity = similarity_vul(text1, text2)
        res = round(similarity.item(), 4)
        print('与参考论文的相似度为：', res)

    def test_02(self, orig=test_0, check=test_2):
        str1 = get_content(orig)
        str2 = get_content(check)
        text1 = turn_vector(str1)
        text2 = turn_vector(str2)
        similarity = similarity_vul(text1, text2)
        res = round(similarity.item(), 4)
        print('与参考论文的相似度为：', res)

    def test_03(self, orig=test_0, check=test_3):
        str1 = get_content(orig)
        str2 = get_content(check)
        text1 = turn_vector(str1)
        text2 = turn_vector(str2)
        similarity = similarity_vul(text1, text2)
        res = round(similarity.item(), 4)
        print('与参考论文的相似度为：', res)

    def test_04(self, orig=test_0, check=test_4):
        str1 = get_content(orig)
        str2 = get_content(check)
        text1 = turn_vector(str1)
        text2 = turn_vector(str2)
        similarity = similarity_vul(text1, text2)
        res = round(similarity.item(), 4)
        print('与参考论文的相似度为：', res)

    def test_05(self, orig=test_0, check=test_5):
        str1 = get_content(orig)
        str2 = get_content(check)
        text1 = turn_vector(str1)
        text2 = turn_vector(str2)
        similarity = similarity_vul(text1, text2)
        res = round(similarity.item(), 4)
        print('与参考论文的相似度为：', res)


if __name__ == '__main__':
    unittest.main()
