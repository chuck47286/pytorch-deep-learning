"""
生成器
和函数区别
"""


def my_gen():
    yield 1
    yield 2
    yield 3
    return 4


def my_fun():
    return 5


# print(my_fun())
# print(my_gen()) # <generator object my_gen at 0x000002AFCB92BF20>
"""
1
2
3
"""
# for data in my_gen():
#     print(data)

"""
可以停止的函数
写法1 直接使用next()函数遍历，那么结果每次都是1
写法2 如果将生成器赋值给一个对象，那么next()遍历这个对象，则真正使用了生成器的方法，可以1,2,3,4遍历出来，而且会停止
"""
# 方法1 不合理
# print(next(my_gen())) # 1
# print(next(my_gen())) # 1
# print(next(my_gen())) # 1

# 方法2 合理
gen = my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # 报错， StopIteration: 4。第四次是return, 而不是yield实现
# print(next(gen))