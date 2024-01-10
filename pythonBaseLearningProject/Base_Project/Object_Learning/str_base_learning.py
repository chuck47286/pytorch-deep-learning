# string 字符串
# 属于sequence,这点同list, tuple

str = 'Runoob'
print(str)
print(str[0])
print(str[0:])
print(str[:2])
print()

# 操作非法
str[1] = 'm' # 抛出异常，TypeError: 'str' object does not support item assignment， 这点同tuple
print(str)