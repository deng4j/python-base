import json

"""
处理的是字符串

json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
    allow_nan=True, cls=None, indent=None, separators=None, 
    encoding="utf-8", default=None, sort_keys=False, **kw)：将 Python 对象编码成 JSON 字符串。

json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int
    [, parse_constant[, object_pairs_hook[, **kw]]]]]]]])：用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
"""

data = {
    'name': '张三',
    'age': 18,
    'card': 1684351245312645
}

data2 = "{'name': '张三','age': 18,'card': 1684351245312645}"

json_obj = json.dumps(data, ensure_ascii=False)
print(type(json_obj))
print(json_obj)

json_obj2 = json.dumps(data2, ensure_ascii=False)
print(type(json_obj2))
print(json_obj2)

# 将 JSON 对象转换为 Python 字典
py_obj = json.loads(json_obj)
print(type(py_obj))
print(py_obj)
print(py_obj['name'])
