"""
dict.update(dict2)：把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
"""

tinydict = {'Name': 'Runoob', 'Age': 7}
tinydict2 = {'Name': 'CCCC', 'Sex': 'female'}

tinydict.update(tinydict2)

print("更新字典 tinydict : ", tinydict)
