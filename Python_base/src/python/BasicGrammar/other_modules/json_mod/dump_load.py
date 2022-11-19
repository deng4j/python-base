import json

"""
处理的是文件
"""

data = {
    'name': '张三',
    'age': 18,
    'card': 1684351245312645
}

# 写入 JSON 数据
with open('D:\\IDE_pycharm\\project1\\Python_base\\src\\resources\\json\\data.json', 'w', encoding='utf-8') as f:
    json.dump(data, fp=f, ensure_ascii=False)

# 读取数据
with open('D:\\IDE_pycharm\\project1\\Python_base\\src\\resources\\json\\data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
