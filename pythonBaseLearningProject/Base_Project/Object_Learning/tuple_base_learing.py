# tuple 元祖
# 和list的区别在于元素不可以修改
# 类似于str 不可以修改元素，但是可以取元素

tuple = ('abcd', 784, 2.23, 'runboo')
print(tuple)
print(tuple[0])
print(tuple[0:])
print(tuple[:2])
print()

# 操作非法
tuple[1] = 'three' # TypeError: 'tuple' object does not support item assignment 抛出异常
print(tuple)