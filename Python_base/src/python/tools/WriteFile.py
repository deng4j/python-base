def writeFile(path='/Users/deng4j/Desktop/temp/writeFile.txt', model='w', content=None):
    if content is None:
        raise Exception("path is None!!!")

    f = open(path, model, encoding='utf-8')
    num = f.write(content)
    print('写入成功：{}  字节：{}'.format(path, num))
    f.close()


if __name__ == '__main__':
    writeFile(content='你好👋')
