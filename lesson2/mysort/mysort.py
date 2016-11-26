# coding: utf-8

import math

# 冒泡排序
def bubbleSort(list):
    for j in xrange(len(list), -1, -1):
        for i in xrange(0, j - 1, 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]

# 快速排序：
def partition(list, p, r):
    flag = list[r]
    i = p - 1
    for j in range(p, r):
        if list[j] <= flag:
            i += 1
            list[i], list[j] = list[j], list[i]
            # print j,list
    list[i + 1], list[r] = list[r], list[i + 1]
    return i + 1


def quick_sort_inner(list, p, r):
    if p >= r:
        return
    q = partition(list, p, r)
    quick_sort_inner(list, p, q - 1)
    quick_sort_inner(list, q + 1, r)


def quick_sort(list):
    quick_sort_inner(list, 0, len(list) - 1)


# 绝对值比较
def func(x, y):
    if abs(x) > abs(y):
        return 1
    else:
        return -1

def sin_func(x, y):
    if (math.sin(x) > math.sin(y)):
        return 1
    else:
        return -1

def cos_func(x, y):
    if (math.cos(x) > math.cos(y)):
        return 1
    else:
        return -1

def tuple_func(x, y):
    if (x[1] > y[1]):
        return 1
    else:
        return -1

def mysort(data, key=func, reveresed=False):
    for j in xrange(len(data), -1, -1):
        for i in xrange(0, j - 1, 1):
            if key(data[i], data[i + 1]) > 0:
                data[i], data[i + 1] = data[i + 1], data[i]
    if reveresed == True:
        data.reverse()
    return data


def readFile(filename):
    f = open(filename, 'r')
    y = []
    x = f.readlines()
    # 获取word
    for line in x:
        y.extend(line.split())
    f.close()
    word_list = []

    # 过滤不需要的字符
    for word in y:
        word1 = word
        while True:
            lastchar = word1[-1:]
            if lastchar in [",", ".", "!", "?", ";", '"']:
                word2 = word1.rstrip(lastchar)
                word1 = word2
            else:
                word2 = word1
                break

        while True:
            firstchar = word2[0]
            if firstchar in [",", ".", "!", "?", ";", '"']:
                word3 = word2.lstrip(firstchar)
                word2 = word3
            else:
                word3 = word2
                break
        word_list.append(word3)

    # 计算词频
    freq_list = []
    word_saved = []
    for word in word_list:
        if not word in word_saved:
            word_saved.append(word)
            freq_list.append((word, word_list.count(word)))
    return freq_list


if __name__ == "__main__":
    a = [1,2,6,4,543,4]
    b = mysort(a, func, False)
    print b
    b = mysort(a, func, True)
    print b
    b = mysort(a, sin_func, False)
    print b
    b = mysort(a, sin_func, True)
    print b
    b = mysort(a, cos_func, False)
    print b
    b = mysort(a, cos_func, True)
    print b
    freq_list = readFile("wordcount.txt")
    # sort_list = mysort(freq_list, tuple_func, True)
    sort_list = mysort(freq_list, (lambda x, y: 1 if x[1] > y[1] else -1), True)
    print sort_list
