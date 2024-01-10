# dic 字典

dict = {}
dict['one'] = '1 - 工程'
dict[2] = '2 - 工具'

print(dict)
print(dict['one'])
print(dict[2])
# print(dict[4]) # 出错，抛出异常 KeyError: 4
print(dict.keys())
print(dict.values())