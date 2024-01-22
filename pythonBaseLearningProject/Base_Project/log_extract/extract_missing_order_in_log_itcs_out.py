"""
专门用于提取ITCS日志中，丢单的msgId
"""
import re
import os


def extract_order_from_log(log_line):
    """
    Extracts the order value from a log line if it contains the specified PBU.
    """
    order_match = re.search(r'execRpt (\d+)', log_line)
    if order_match:
        return order_match.group(1)
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
    order_msgId_map = {}  # 新增字典来映射 msgId 到 order

    with open(file_path, 'r', encoding='utf-8') as file:
        for log in file:
            if 'RECV type ' in log:
                order = extract_order_from_log(log)
                if order:
                    orders.add(order)
            elif 'ITCS-OUT send ServiceContext start!' in log:
                msgId = extract_msgId_from_log(log)
                if msgId:
                    # Extracting the order part of the msgId
                    msg_id_part = msgId[-len(order):]
                    msgIds.add(msg_id_part)
                    order_msgId_map[msg_id_part] = msgId


    # Finding orders that are not part of any msgId
    missing_orders = orders - msgIds

    return missing_orders, msgIds, orders, order_msgId_map


def print_sorted_set(s, description="Set", numeric_sort=False):
    """
    打印集合中的元素，每行一个，按升序排序，并打印集合的描述和大小。

    :param s: 要排序和打印的集合。
    :param description: 集合的描述（例如对象名）。
    :param numeric_sort: 如果为True，则按数值排序，否则按字典序排序。
    """
    # 获取集合的大小
    size = len(s)

    # 打印集合的描述和大小
    print(f"{description} (Size: {size}):")

    if numeric_sort:
        # 按数值排序
        sorted_list = sorted(s, key=int)
    else:
        # 按字典序排序
        sorted_list = sorted(s)

    # 遍历排序后的列表并打印每个元素
    for item in sorted_list:
        print(item)

def print_sorted_map(map_dict, description="Map"):
    """
    打印字典中的键值对，每行一个，按键的数值升序排序，并打印字典的描述和大小。

    :param map_dict: 要排序和打印的字典。
    :param description: 字典的描述（例如对象名）。
    """
    # 获取字典的大小
    size = len(map_dict)

    # 打印字典的描述和大小
    print(f"{description} (Size: {size}):")
    # 按键的数值升序排序字典，并遍历打印
    for key in sorted(map_dict, key=int):
        print(f"{key}: {map_dict[key]}")


dir_path = r'C:\Users\Chuck\Desktop'
file_name = 'b.805'
file_path = os.path.join(dir_path, file_name)
# print(file_path)# 替换为你的日志文件路径
missing_orders, _, orders, order_msgId_map = process_logs_from_file(file_path)
# print(f"common elements {missing_orders & msgIds}")
# print(f"differences elements {msgIds - orders}")

print_sorted_set(missing_orders, description="missing_orders", numeric_sort=True)
# print_sorted_set(msgIds, description="msgIds", numeric_sort=True)
print_sorted_map(order_msgId_map, description="order_msgId_map")
print_sorted_set(orders, description="orders", numeric_sort=True)
