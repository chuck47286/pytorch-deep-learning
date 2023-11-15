conv_arch = ((1, 64), (1, 128), (2, 256), (2, 512), (2, 512))

arch_ = [(pair[0], pair[1] // 4) for pair in conv_arch]
# print(arch_)

