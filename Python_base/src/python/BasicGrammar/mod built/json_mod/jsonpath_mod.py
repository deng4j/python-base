import json

from jsonpath import jsonpath

"""
JsonPath为Json文档提供了解析能力，通过使用JsonPath，你可以方便的查找节点、获取想要的数据，JsonPath是Json版的XPath。

JsonPath语法要点：
    $ 表示文档的根元素
    @ 表示文档的当前元素
    .node_name 或 ['node_name'] 匹配下级节点
    [index] 检索数组中的元素
    [start:end:step] 支持数组切片语法
    * 作为通配符，匹配所有成员
    .. 子递归通配符，匹配成员的所有子元素
    (<expr>) 使用表达式
    ?(<boolean expr>)进行数据筛选
    
注意：
    JsonPath的索引从0开始计数
    JsonPath中字符串使用单引号表示，例如:$.store.book[?(@.category=='reference')]中的'reference'
"""

json1 = """
    {
	"store": {
		"book": [{
				"category": "武侠",
				"author": "金庸",
				"title": "《连城诀》",
				"price": 59
			}, {
				"category": "武侠",
				"author": "金庸",
				"title": "《笑傲江湖》",
				"price": 100
			}, {
				"category": "科幻",
				"author": "刘慈欣",
				"title": "《三体》",
				"isbn": "0-312-31-4123",
				"price": 38
			}, {
				"category": "言情",
				"author": "紫百合",
				"title": "《花落燕云梦》",
				"isbn": "0-395-1933125-8",
				"price": 22.99
			}
		],
		"bicycle": {
			"color": "red",
			"price": 3123
		}
	}
}
"""

json_obj = json.loads(json1)

print(jsonpath(json_obj, '$.store.book[*].author'))  # 所有book的author节点

print(jsonpath(json_obj, '$..author'))  # 所有author节点

print(jsonpath(json_obj, '$.store.*'))  # store下的所有节点，book数组和bicycle节点

print(jsonpath(json_obj, '$.store..price'))  # store下的所有price节点

print(jsonpath(json_obj, '$..book[2]'))  # 匹配第3个book节点

print(jsonpath(json_obj, '$..book[0,1]'))  # 匹配前两个book节点

print(jsonpath(json_obj, '$..book[?(@.isbn)]'))  # 过滤含isbn字段的节点

print(jsonpath(json_obj, '$..book[?(@.price<50)]'))  # 过滤price<50的节点
