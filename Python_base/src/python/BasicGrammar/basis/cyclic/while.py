# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b

print("\n------------------------while 循环使用 else 语句-------------------------")

count = 8
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

print("------------------------简单语句组-------------------------")

while count > 5: count -= 1
print(count)
