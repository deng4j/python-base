def do_format(column, separator):
    data = ''
    print('输入文字，按ok结束输入')
    for i in iter(input, 'ok'):
        data += i
    data = ''.join(set(data.replace('\n', '').replace(' ', '')))
    count = 0
    new_data = ''
    for c in data:
        new_data = new_data + c + separator
        count += 1
        if count == column:
            new_data = new_data + '\n'
            count = 0
    print(new_data)


"""
将文本以格式输出
"""
if __name__ == '__main__':
    while True:
        do_format(20, ' ')
