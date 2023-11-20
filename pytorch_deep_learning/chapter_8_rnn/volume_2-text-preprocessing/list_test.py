import collections
# list1 = ['a']
# list2 = ['b']
# print(list2)
# print(list1)
# print(list1 + list2)

tokens = [['hello', 'world'], ['python', 'programming'], ['python'], ['test','test','test']]

token_list = [token for line in tokens for token in line]
print(token_list)
print(f'{collections.Counter(token_list)}')