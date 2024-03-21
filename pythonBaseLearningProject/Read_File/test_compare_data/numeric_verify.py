import re


def adjust_row_data(row_data):
    """
    调整数据行：从列表开头开始，删除不是数字的元素，直到找到第一个是数字的元素为止
    :param row_data: 原始行数据列表
    :return: 调整后的行数据列表
    """
    tag_pattern = re.compile(r'^\d+$')

    # 找到第一个符合纯数字模式的元素的索引
    start_index = 0
    for i, item in enumerate(row_data):
        if tag_pattern.match(item):
            start_index = i  # 找到符合纯数字模式的元素，记录索引并停止循环
            break

    # 删除前面不是数字的元素
    adjusted_data = row_data[start_index:]

    return adjusted_data


def swap_elements_if_condition_met(row_data):
    """
    如果第一个元素是数字类型且第二个元素不是，则交换列表中的第一个和第二个元素
    :param row_data: 原始行数据列表
    :return: 调整后的行数据列表
    """
    # 使用正则表达式来检查是否为数字
    is_digit = re.compile(r'^\d+$')

    # 确保列表至少有两个元素
    if len(row_data) >= 2:
        first_is_digit = is_digit.match(row_data[0])
        second_is_digit = is_digit.match(row_data[1])

        # 如果第一个元素是数字且第二个元素不是数字，则交换这两个元素
        if first_is_digit and not second_is_digit:
            row_data[0], row_data[1] = row_data[1], row_data[0]

    return row_data


# 示例数据
# example_1 = ['8560', '→', 'GateWayPBU', '登录或订阅PBU', 'Y', 'C8']
# example_1 = swap_elements_if_condition_met(example_1)
example_2 = ['→', '8560', 'GateWayPBU', '登录或订阅PBU', 'Y', 'C8']
example_2 = swap_elements_if_condition_met(example_2)

# 应用调整函数并打印结果
# adjusted_example_1 = adjust_row_data(example_1)
adjusted_example_2 = adjust_row_data(example_2)

# print(adjusted_example_1)  # 期望输出: ['8560', 'GateWayPBU', '登录或订阅PBU', 'Y', 'C8']
# original ['8560', '→', 'GateWayPBU', '登录或订阅PBU', 'Y', 'C8']
print(adjusted_example_2)  # 期望输出: ['8560', 'GateWayPBU', '登录或订阅PBU', 'Y', 'C8']
