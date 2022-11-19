import pickle

"""
pickle模块实现了基本的数据序列和反序列化。
    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
    
pickle.dump(obj, file, protocol)：
    obj——序列化对象，将对象obj保存到文件file中去；
    file——file表示保存到的类文件对象，file必须有write()接口，file可以是一个以’w’打开的文件或者是一个StringIO对象，也可以是任何可以实现write()接口的对象；
    protocol——序列化模式，默认是 0（ASCII协议，表示以文本的形式进行序列化），protocol的值还可以是1和2（1和2表示以二进制的形式进行序列化。其中，1是老式的二进制协议；2是新二进制协议）。

pickle.load(file)：反序列化对象，将文件中的数据解析为一个python对象。
"""
print("------------------  dump  --------------------")

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('str_class', u'Unicode str_class'),
         'c': None}

selfref_list = [1, 2, 3]

output = open('D:\\IDE_pycharm\\project1\\Python_base\\src\\resources\\file\\folder1\\pickle.txt', 'wb')

pickle.dump(data1, output)

pickle.dump(selfref_list, output, -1)

output.close()
print("序列化成功")

print("------------------  load  --------------------")

pkl_file = open('D:\\IDE_pycharm\\project1\\Python_base\\src\\resources\\file\\folder1\\pickle.txt', 'rb')

data1 = pickle.load(pkl_file)
print(data1)

data2 = pickle.load(pkl_file)
print(data2)

pkl_file.close()
