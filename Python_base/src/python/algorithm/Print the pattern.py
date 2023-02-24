s = int(input('请输入金字塔行数：\n'))

s = s + 1
m = 0

for i in range(s, 0, -1):
    m += 1
    print(' ' * m, end='')
    print('*' * (2 * i - 1))
