"""
专门用于提取ITCS日志中，丢单的msgId
"""
import re
import os
import time
from datetime import datetime


def extract_enqueue_info(log_line):
    """
    Extracts enqueue information form a log line.
    Returns module_pbu. msgId, and originalMsgId.
    """
    match = re.search(r'module_pbu=(\w+).*msgId=(\w+).*originalMsgId=(\d+)', log_line)
    if match:
        return match.groups()
    return None, None, None


def extract_dequeue_info(log_line):
    """
    Extracts dequeue information form a log line.
    Returns module_pbu and msgId.
    """
    match = re.search(r'module_pbu=(\w+).*msgId=(\w+)', log_line)
    if match:
        return match.groups()
    return None, None, None


def process_logs_from_file(file_path):
    """
    Processes log lines from a file, extracting and comparing order and msgId values based on the specified PBU.
    """
    enqueue_orders = {}  # key: module_pbu, value: set of (msgId, originalMsgId)
    dequeue_orders = {}  # key: module_pbu, value: set of msgId
    still_in_queue = {}  # key: module_pbu, value: list of originalMsgId

    # with open(file_path, 'r', encoding='gbk') as file:
    with open(file_path, 'r', encoding='utf-8') as file:
        for log in file:
            if 'OrderQueuePreProperties [createBizTypeKey] done, pbuKey is created!' in log:
                module_pbu, msgId, originalMsgId = extract_enqueue_info(log)
                if module_pbu:
                    enqueue_orders.setdefault(module_pbu, {}).update({msgId: originalMsgId})
            elif 'ITCS send start!' in log:
                module_pbu, msgId = extract_dequeue_info(log)
                if module_pbu:
                    dequeue_orders.setdefault(module_pbu, set()).add(msgId)

    # filtering orders still in the queue
    for module_pbu, msgId_to_original in enqueue_orders.items():
        still_in_queue[module_pbu] = [original for msgId, original in msgId_to_original.items()
                                                      if msgId not in dequeue_orders.get(module_pbu, set())]
    # count enqueued_orders 中所有的元素的总数
    total_enqueued = sum(len(msgId_to_original) for msgId_to_original in enqueue_orders.values())
    # count dequeued_orders 中所有的元素的总数
    total_dequeued = sum(len(msgIds) for msgIds in dequeue_orders.values())

    return total_enqueued, total_dequeued, still_in_queue


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
    total_enqueued, total_dequeued, still_in_queue = process_logs_from_file(
        os.path.join(dir_path, file_name))

    # 打印结果
    print(f"missing_orders (Size:{total_enqueued - total_dequeued})")
    print(f"orders (Size:{total_enqueued})")
    for key in sorted(still_in_queue.keys()):
        print(f"Key: {key}, value: {still_in_queue[key]}")
    print(f'-----------------------')


if __name__ == "__main__":
    # 设置默认间隔时间（单位：秒）
    interval = 5  # 300s == 5min

    # 日志文件路径
    # dir_path = r'C:\Users\yucheng\Downloads' # 测试日志路径
    # file_name = "stdout - 2024-01-17T111257.805"  # 测试日志文件名

    dir_path = r'./log_folder/' # 测试日志路径
    file_name = "stdout (50)"  # 测试日志文件名
    # print(os.path.join(dir_path, file_name))
    file_path = os.path.join(dir_path, file_name)

    while True:
        process_and_print_logs(file_path)
        # 等待指定的间隔时间
        time.sleep(interval)
