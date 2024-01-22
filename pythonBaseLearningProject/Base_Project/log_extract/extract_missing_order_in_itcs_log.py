"""
专门用于提取ITCS日志中，丢单的msgId
"""
import re


def extract_order_from_log(log_line, pbu):
    """
    Extracts the order value from a log line if it contains the specified PBU.
    """
    if f"pbu {pbu} " in log_line or f"pbu={pbu}" in log_line:
        order_match = re.search(r'order (\d+)', log_line)
        if order_match:
            return order_match.group(1)
    return None


def extract_msgId_from_log(log_line, pbu):
    """
    Extracts the msgId value from a log line if it contains the specified PBU.
    """
    if f"techPBU={pbu}" in log_line:
        msgId_match = re.search(r'msgId=(\d+)', log_line)
        if msgId_match:
            return msgId_match.group(1)
    return None


def process_logs_from_file(file_path, pbu):
    """
    Processes log lines from a file, extracting and comparing order and msgId values based on the specified PBU.
    """
    orders = set()
    msgIds = set()

    with open(file_path, 'r') as file:
        for log in file:
            if 'RECV type [D]' in log:
                order = extract_order_from_log(log, pbu)
                if order:
                    orders.add(order)
            elif 'send start,' in log:
                msgId = extract_msgId_from_log(log, pbu)
                if msgId:
                    # Extracting the order part of the msgId
                    msgIds.add(msgId[-len(order):])

    # Finding orders that are not part of any msgId
    missing_orders = orders - msgIds

    return missing_orders


file_path = "./log_folder/a.txt"  # 替换为你的日志文件路径
pbu = "00179"  # 替换为你想要过滤的PBU值
missing_orders = process_logs_from_file(file_path, pbu)
print(missing_orders)