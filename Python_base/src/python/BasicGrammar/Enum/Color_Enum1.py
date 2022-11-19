from enum import Enum


# 创建枚举1
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print("------------------调用枚举成员的 3 种方式------------------")

print(Color.RED)
print(Color['RED'])
print(Color(1))

print("------------------调取枚举成员中的 value 和 name------------------")

print(Color.RED.value)
print(Color.RED.name)

print("------------------遍历枚举类中所有成员的 2 种方式------------------")

for color in Color:
    print(color)

print("------------------外部修改枚举的值------------------")

try:
    Color.RED = 5
except:
    print('枚举类中各个成员的值，不能在类的外部做任何修改')

print("--------- 枚举类还提供了一个 __members__ 属性，该属性是一个包含枚举类中所有成员的字典 -------")

for name, member in Color.__members__.items():
    print(name, "->", member)
