import re

"""
匹配一个URL
"""
url = '![在这里插入图片描述](https://img-blog.csdnimg.cn/33632133fe77430793d5aa3ab3a0af6a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5oSb5rKi44GL44KK44KT,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)'
results = re.finditer(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', url)
for result in results:
    print(result.group())
