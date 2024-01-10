# set 无序，元素唯一的集合

set = {'sf', 'ab', 'c', 'd', 1}
print(set)
# print(set[0]) # 报错，set' object is not subscriptable
print()


def recursive_set(set_collection):  # 遍历
    print("开始遍历set")
    for val in set_collection:
        print(val)


# 操作
set.add(123)
set.add(123)
set.add(123)
recursive_set(set)
