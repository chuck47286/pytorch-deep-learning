import random

my_seq = list(range(35))
print(my_seq)
corpus = my_seq[random.randint(0, 5 - 1):]
print(corpus)
num_subseqs = (len(corpus) - 1) // 5
print(num_subseqs)
initial_indices = list(range(0, num_subseqs * 5, 5))
print(initial_indices)
random.shuffle(initial_indices)
print(initial_indices)