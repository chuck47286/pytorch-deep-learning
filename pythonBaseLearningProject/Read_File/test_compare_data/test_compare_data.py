# # 假定structured_data是之前的结构化数据列表
# structured_data = [
#     # 示例数据
#     {'D': [{'1180': ['ApplID', '业务类型', 'Y', 'C6']}, {'11': ['ClOrdID', '会员内部订单编号', 'Y', 'C10']}]},
#     {'F': [{'1180': ['ApplID', '业务类型', 'Y', 'C7']}, {'11': ['ClOrdID', '会员内部订单编号', 'Y', 'C10']}]}
# ]
#
# # 平铺所有tag和其最后一列值
# tags_with_values = [(tag, values[-1]) for table_data in structured_data for entries in table_data.values() for entry in
#                     entries for tag, values in entry.items()]
#
# # 使用字典收集每个tag的最后一列值
# tag_values_dict = {}
# for tag, value in tags_with_values:
#     tag_values_dict.setdefault(tag, set()).add(value)
#
# # 检查并打印出存在不一致的tag
# for tag, values in tag_values_dict.items():
#     if len(values) > 1:
#         print(f"Tag '{tag}' 有不一致的最后一列值: {values}")

# 假定structured_data是之前的结构化数据列表
structured_data = [
    {'D': [{'1180': ['ApplID', '业务类型', 'Y', 'C6']}, {'11': ['ClOrdID', '会员内部订单编号', 'Y', 'C10']}, {'13': ['test', '测试数据集', 'Y', 'C100']}]},
    {'F': [{'1180': ['ApplID', '业务类型', 'Y', 'C7']}, {'11': ['ClOrdID', '会员内部订单编号', 'Y', 'C10']}]}
]

# 使用字典收集每个tag的最后一列值，同时记录消息类型
tag_values_dict = {}

for table_data in structured_data:
    for msg_type, entries in table_data.items():
        for entry in entries:
            for tag, values in entry.items():
                if tag not in tag_values_dict:
                    tag_values_dict[tag] = {}
                tag_values_dict[tag].setdefault(msg_type, set()).add(values[-1])

# 检查并打印出存在不一致的tag
# for tag, msg_types in tag_values_dict.items():
#     if any(len(values) > 1 for values in msg_types.values()) or len(msg_types) > 1:
#         diff_values = {msg_type: values for msg_type, values in msg_types.items()}
#         print(f"Tag '{tag}' 在不同消息类型中有不一致的最后一列值: {diff_values}")

for tag, msg_types in tag_values_dict.items():
    combined_values = {v for values in msg_types.values() for v in values}
    msg_types_join = ','.join(msg_types.keys())
    if len(combined_values) > 1:
        print(f"Tag '{tag}' 在不同消息类型中有不一致的最后一列值: {msg_types}")
    elif len(msg_types) > 1:
        print(f"Tag '{tag}' 出现在多个消息类型({msg_types_join})中，但其值一致。")
    else:
        # 如果只有一个消息类型包含这个tag,且想展示这种情况
        print(f"Tag '{tag}' 仅出现在消息类型({msg_types_join})")
