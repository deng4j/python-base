from typing import Any, Optional, Dict, List, Tuple, Sequence, TypeVar, Union, NamedTuple

"""
typing模块：用于参数提示。
"""


class People:
    name = '李敏'


def send_request(request_data: Any,
                 headers: Optional[Dict[str, str]],
                 people: Optional[People] = None,
                 as_json: bool = True):
    """
    :param request_data:提示可以是任何数据
    :param headers:提示内容是一个可选的字符串字典
    :param people:提示是可选的（默认为None），或者是符合编码People的任何数据
    :param as_json:提示需要始终是一个布尔值（本质上是一个flag，即使名称可能没有提供这种提示）
    :return:
    """
    print("request_data：{}\n"
          "headers:{}\n"
          "people:{}\n"
          "as_json:{}\n".format(request_data, headers, people, as_json))


# 实际上
send_request('随便', 12, People(), True)

print("---------------------类型标注提示1---------------------")


def fun1(a: int) -> str:
    """
    :param a: a:int #指定了输入参数a为int类型
    :return: -> str #返回值为srt类型
    """
    print(a)
    return '返回一个str'


print(fun1(12))

print("---------------------类型标注提示2---------------------")

Vector = List[float]


def scale(vector: Vector) -> Vector:
    return [num * 2 for num in vector]


# 传递float元素的list不会警告
print(scale([1.0, -4.2, 5.4]))
print(scale({1, 2}))

print("---------------------类型标注提示3---------------------")

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]


def broadcast_message(servers: Server):
    print(servers)


broadcast_message((('str', 10), {'a': '1'}))
broadcast_message((('str', '10'), {'a': '1'}))

print("---------------------泛型指定提示---------------------")

T = TypeVar('T')  # 可以是任意类型
A = TypeVar('A', str, bytes)  # 必须是str或bytes
C = Union[str, None]  # 必须是str或None


def ft(l: Sequence[T]) -> T:
    """传递任意类型元素的list"""
    return l


# 传递str类型
print(ft((1, 2)))

print("---------------------创建变量时的类型指定---------------------")


class Employee(NamedTuple):
    name: str
    id: int = 3


employee = Employee('张三')
assert employee.id == 3

employee.id == 'strxxxx'  # 不生效
print(employee.id)

try:
    assert employee.id == 'strbbb', 'id只能是int类型'
except Exception as e:
    print(e)

print("-------------------------变量-------------------------")

a: int = 1
b: int = 'xx'
print(a, b)
