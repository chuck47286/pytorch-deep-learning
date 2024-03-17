"""
专门用于提取ITCS-OUT日志中，丢单的msgId
"""
import re
import os
import time
from datetime import datetime


def extract_order_from_log(log_line):
    """
    Extracts the order value from a log line if it contains the specified PBU.
    """
    order_match = re.search(r'execRpt (\w+)', log_line)
    pbu_match = re.search(r'pbu (\w+)', log_line)
    if order_match and pbu_match:
        return order_match.group(1), pbu_match.group(1)
    return None


def extract_msgId_from_log(log_line):
    """
    Extracts the msgId value from a log line if it contains the specified PBU.
    """
    msgId_match = re.search(r'msgId=(\S+)', log_line)
    if msgId_match:
        return msgId_match.group(1)
    return None


def process_logs_from_file(file_path):
    """
    Processes log lines from a file, extracting and comparing order and msgId values based on the specified PBU.
    """
    orders = set()
    msgIds = set()
    order_pbu_dict = {}
    msgId_dict = {}

    # with open(file_path, 'r', encoding='gbk') as file:
    with open(file_path, 'r', encoding='utf-8') as file:
        for log in file:
            if 'RECV type ' in log:
                order, pbu = extract_order_from_log(log)
                if order and pbu:
                    orders.add(order)
                    order_pbu_dict[order] = pbu
            elif 'ITCS-OUT send ServiceContext start!' in log:
                msgId = extract_msgId_from_log(log)
                if msgId:
                    # Extracting the order part of the msgId
                    msgId_part = msgId[-len(order):]
                    msgIds.add(msgId_part)
                    msgId_dict[msgId_part] = msgId

    # Finding orders that are not part of any msgId
    missing_orders = orders - msgIds

    return missing_orders, msgIds, orders, msgId_dict, order_pbu_dict


def print_sorted_set(s, desc="Set", numeric_sort=False, traversal=False):
    """
    打印集合中的元素，每行一个，按升序排序。

    :param s: 要排序和打印的集合。
    :param desc: 集合的描述
    :param numeric_sort: 如果为True，则按数值排序，否则按字典序排序。
    :return:
    """
    # 获取集合的大小
    size = len(s)

    # 打印集合的描述和大小
    print(f"{desc} (Size:{size})")

    if traversal:
        if numeric_sort:
            # 按数值排序
            sorted_list = sorted(s, key=int)
        else:
            # 按字典序排序
            sorted_list = sorted(s)

        # 遍历排序后的列表并打印每个元素
        for item in sorted_list:
            print(item)


def print_sorted_map(dict, desc="Dict", traversal=False):
    """
    打印集合中的元素，每行一个，按升序排序。

    :param s: 要排序和打印的集合。
    :param desc: 集合的描述
    :param numeric_sort: 如果为True，则按数值排序，否则按字典序排序。
    :return:
    """
    # 获取集合的大小
    size = len(dict)

    # 打印集合的描述和大小
    print(f"{desc} (Size:{size})")
    if traversal:
        # 按键的数值升序排序字典，并遍历打印
        for key in sorted(dict, key=int):
            print(f"{key}: {dict[key]}")


def find_pbu_for_missing_orders(mis_orders, order_pbu_map):
    """
    找出 missing orders 集合中每个 order 对应的 pbu,并统计每个 pbu的mis 个数
    :param mis_orders:  丢失order的集合
    :param order_pbu_map: order --> pbu 的映射关系
    :return:
    """
    pbu_missing_order_count = {}
    for order in mis_orders:
        pbu = order_pbu_map.get(order)
        if pbu:
            if pbu not in pbu_missing_order_count:
                pbu_missing_order_count[pbu] = {'count': 0, 'orders': set()}
            pbu_missing_order_count[pbu]['count'] += 1
            pbu_missing_order_count[pbu]['orders'].add(order)

    return pbu_missing_order_count


def process_and_print_logs(file_path):
    """
    处理日志文件并打印结果，每次执行前打印时间戳。
    :param file_path: 文件绝对路径
    :return:
    """
    # 获取当前时间戳并打印
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Current Timestamp:{current_time}')

    # 执行日志处理函数
    missing_orders, msgIds, orders, order_msgId_dict, order_pbu_dict = process_logs_from_file(
        os.path.join(dir_path, file_name))

    # 打印结果
    print_sorted_set(missing_orders, desc="missing_orders", numeric_sort=True)
    # print_sorted_set(msgIds, desc="msgIds", numeric_sort=True)
    print_sorted_set(orders, desc="orders", numeric_sort=True)
    # print_sorted_map(order_msgId_dict, desc="msgIds")
    # print_sorted_map(order_pbu_dict, desc="order_pbu_dict")
    for_missing_orders = find_pbu_for_missing_orders(missing_orders, order_pbu_dict)
    for key in sorted(for_missing_orders.keys()):
        print(f"Key: {key}, value: {for_missing_orders[key]}")
    print(f'-----------------------')


if __name__ == "__main__":
    # 设置默认间隔时间（单位：秒）
    interval = 5  # 300s == 5min

    # 日志文件路径
    dir_path = r'./log_folder/' # 测试日志路径
    file_name = "test_3.txt"  # 测试日志文件名

    # dir_path = r'C:\Users\yucheng\Downloads'  # 本地日志路径
    # file_name = "itcs_out.txt"  # 替换为你的日志文件路径
    # print(os.path.join(dir_path, file_name))
    file_path = os.path.join(dir_path, file_name)

    while True:
        process_and_print_logs(file_path)
        # 等待指定的间隔时间
        time.sleep(interval)
