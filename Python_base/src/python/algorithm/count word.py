"""
计算句子中每个单词的出现次数。
句子中可能包含标点符号，包括`','`, `'.'`, 和` ! `，但在计数时不应考虑它们。此外，计数器是不区分大小写的，字典中的每个单词都应该是小写的。
"""


def counter(sentence):
    dic = {}
    sentence = sentence.lower()
    temp = ''
    lst = []
    for x in sentence:
        if 97 <= ord(x) <= 122:
            temp += x
        else:
            if temp != '':
                lst.append(temp)
                temp = ''
    for i in lst:
        dic[i] = sentence.count(i)
    return dic


print(counter('Good good study, day day up!'))
