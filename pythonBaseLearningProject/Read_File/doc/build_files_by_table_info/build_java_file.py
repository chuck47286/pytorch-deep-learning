# 定义消息类型到Java类名和StepMsgEnum值的映射
message_type_mapping = {
    'AE': {'class_name': 'StepTradeCaptureReport', 'enum': 'TRADE_CAPTURE_REPORT'},
    # 添加更多的映射关系
}

def get_java_type(type_identifier):
    """
    根据JAVA
    :param type_identifier:
    :return:
    """
    # 检查首字母
    if type_identifier.startswith('C'):
        return 'String'
    elif type_identifier.startswith('N'):
        # 提取数字部分
        number_part = type_identifier[1:].split('(')[0]  # 移除可能的小数定义，例如"N6(2)"
        number = int(number_part)  # 转换为整数

        # 根据数字部分的值判断具体类型
        if number < 10:
            return 'Integer'
        elif number >= 10:
            return 'Long'
        # 如果有小数部分，使用BigDecimal
        if '(' in type_identifier:
            return 'BigDecimal'
    elif type_identifier == 'date' or type_identifier == 'ntime' or type_identifier == 'Boolean':
        return 'String'
    elif type_identifier == 'price' or type_identifier == 'quantity' or type_identifier == 'amount':
        return 'BigDecimal'
    # 如果无法识别，返回Object作为默认类型
    return 'Object'


def build_java_file(json_data):
    # 根据json_data的键来确定类名和枚举值
    message_type = list(json_data.keys())[0]  # 假设json_data只有一个主要的键
    mapping = message_type_mapping.get(message_type, None)

    if mapping is None:
        raise ValueError(f"Unsupported message type: {message_type}")

    class_name = mapping['class_name']
    step_msg_enum = mapping['enum']


    # Initialize parts of the Java class
    package_declaration = "package com.sse.iitp.protocol.converter.bo;\n\n"
    imports = "import com.sse.iitp.protocol.converter.enums.impl.StepMsgEnum;\n" \
              "import io.swagger.annotations.ApiModelProperty;\n" \
              "import lombok.Data;\n\n" \
              "import java.math.BigDecimal;\n" \
              "import java.util.List;\n\n"
    class_declaration = f"@Data\npublic class {class_name} extends StepOrderBase {{\n\n" \
                        f"    public {class_name}() {{\n" \
                        f"        super(StepMsgEnum.{step_msg_enum});\n" \
                        "    }\n\n"
    class_fields = ""
    field_template = "    @ApiModelProperty(value = \"{description}|{type}\", required = {is_required})\n" \
                     "    private {java_type} {field_name};\n\n"

    # Generate fields
    for item in json_data['AE']:
        for key, value in item.items():
            field_name, description, required, data_type = value
            is_required = "true" if required == 'Y' else "false"
            java_type = get_java_type(data_type)  # Default to Object if mapping not found
            class_fields += field_template.format(description=description, type=java_type, is_required=is_required,
                                                  java_type=java_type, field_name=field_name)

    # Assemble the complete class
    java_class = package_declaration + imports + class_declaration + class_fields + "}\n"
    return java_class


if __name__ == "__main__":
    json_data = {'AE': [{'1180': ['ApplID', '业务类型，见附表', 'Y', 'C6']}, {'571': ['TradeReportID', '会员内部编号', 'Y', 'C10']},
                        {'828': ['TrdType', '业务子类型，见附表', 'N', 'C3']}, {
                            '856': ['TradeReportType', '成交申报类型\n0=Submit，提交成交申报\n2=Accept，确认成交申报\n3=Decline，拒绝成交申报',
                                    'Y', 'C1']}, {
                            '487': ['TradeReportTransType', '成交申报事务类别\n0=New，新申报\n1=Cancel，撤销申报\n2=Replace，响应', 'Y',
                                    'C1']}, {'522': ['OwnerType', '订单所有者类型\n1=个人投资者\n103=机构投资者\n104=自营交易', 'Y', 'N3']},
                        {'572': ['TradeReportRefID', '原始交易会员内部编号，表示被撤消订单的会员内部编号', 'N', 'C10']},
                        {'54': ['Side', '买卖方向：1=买，2=卖\n对于回购：1=正回购，2=逆回购\n对于合并申报且TradeReportType为0时：填0', 'Y', 'C1']},
                        {'44': ['Price1', '申报价格（元）或回购利率（%）\n合并申报时代表买入价格', 'N', 'price']},
                        {'640': ['Price2', '申报价格2\n合并申报时代表卖出价格（元）', 'N', 'price']},
                        {'8911': ['ExpirationDays', '期限（天），可填[1,365]', 'N', 'N4']},
                        {'64': ['SettlDate', '首次结算日', 'N', 'date']}, {'541': ['MaturityDate', '到期日', 'N', 'date']},
                        {'193': ['SettlDate2', '到期结算日', 'N', 'date']},
                        {'8847': ['UAInterestAccrualDays', '实际占款天数（天），可填[1,365]', 'N', 'N3']},
                        {'60': ['TransactTime', '业务发生时间', 'Y', 'ntime']},
                        {'8504': ['TotalValueTraded', '总成交金额，四舍五入\n预留，暂不启用', 'N', 'amount']},
                        {'540': ['TotalAccruedInterestAmt', '总回购利息，四舍五入\n预留，暂不启用', 'N', 'amount']},
                        {'10330': ['TotalSettlCurrAmt', '总到期结算金额，四舍五入\n预留，暂不启用', 'N', 'amount']},
                        {'580': ['NoDates', '违约宽限期（天），[0,365]。', 'N', 'N3']}, {
                            '529': ['', '订单限制\n对于协议回购表示“是否同意在违约情形下由质权方对该违约交易项下的质押券直接以拍卖、变卖等方式进行处置”。\nY = 是\nN = 否', 'N',
                                    'C1']}, {
                            '207': ['SecurityExchange', '结算场所：1=中国结算，2=中央结算\n双边托管券，可填1或2，单边托管券只能填其实际托管方。预留，暂不启用。', 'N',
                                    'C1']},
                        {'10216': ['SettlPeriod', '结算周期：\n0 = T+0\n1 = T+1\n2 = T+2\n3 = T+3\n预留，暂不启用', 'N', 'C1']},
                        {'63': ['SettlType', '结算方式：1=净额结算，2=RTGS结算。\n担保券可填1或2；非担保券只能为2。', 'N', 'C1']},
                        {'711': ['NoUnderlyings', '证券个数', 'N', 'N2']}, {'48': ['SecurityID', '证券代码', 'N', 'C12']},
                        {'38': ['OrderQty', '证券数量', 'N', 'quantity']},
                        {'10331': ['ShareProperty', '份额类型\n0 = 限售\n1 = 非限售', 'N', 'C1']},
                        {'10332': ['RestrictedMonth', '限售期（月），可选：\n0006、0012、0018、0024。', 'N', 'C4']},
                        {'231': ['ContractMultiplier', '折算比例（%）', 'N', 'N6(2)']},
                        {'152': ['CashOrderQty', '质押券面值总额', 'N', 'amount']},
                        {'381': ['GrossTradeAmt', '成交金额', 'N', 'amount']},
                        {'159': ['AccruedInterestAmt', '回购利息', 'N', 'amount']},
                        {'119': ['SettlCurrAmt', '到期结算金额', 'N', 'amount']},
                        {'192': ['OrderQty2', '本期回购结算利息', 'N', 'amount']},
                        {'829': ['TrdSubType', '到期续做类型\nN = 非第三方续做\nY = 第三方续做', 'N', 'C1']}, {'19': ['ExecRefID',
                                                                                                     '当TradeReportType为0时，原成交编号；\n当TradeReportType为2或3时，表示待确认（拒绝）的申报的交易所订单编号。',
                                                                                                     'N', 'C16']}, {
                            '453': ['NoPartyIDs',
                                    '发起方重复组，依次包含发起方的交易参与人代码、发起方交易员一债通账户、发起方业务单元、发起方营业务代码、投资者账户、账户名称、对手方交易员一债通账户1、对手方交易员一债通账户2。取值为8',
                                    'Y', 'N2']}, {'448': ['PartyID', '发起方交易参与人机构代码', 'Y', 'C12']},
                        {'452': ['PartyRole', '取12，表示当前PartyID的取值为发起方的交易参与人代码', 'Y', 'N4']},
                        {'664': ['ConfirmID', '约定号，TradeReportType=0时可以填写，用于对手方定位订单信息。仅可填大小写英文字母或数字。', 'N', 'C12']},
                        {'10198': ['Memo', '备注，可填写补充约定或补充条款', 'N', 'C900']},
                        {'10197': ['PartitionNo', '平台内分区号', 'Y', 'N4']},
                        {'10179': ['ReportIndex', '执行报告编号，从1开始连续递增编号', 'Y', 'N16']},
                        {'1003': ['TradeID', '交易所订单编号', 'Y', 'C16']},
                        {'1126': ['OrigTradeID', '被撤消订单的交易所订单编号，撤销申报必填', 'N', 'C16']},
                        {'8912': ['TrdAckStatus', '执行报告类型，取值有：\nF=Trade，成交', 'Y', 'C1']},
                        {'939': ['TrdRptStatus', '当前申报的状态，取值有：\n2=Matched，已成交', 'Y', 'C1']},
                        {'31': ['LastPx', '成交价格', 'Y', 'price']}, {'17': ['ExecID', '成交编号', 'Y', 'C16']},
                        {'32': ['LastQty', '成交数量', 'Y', 'quantity']},
                        {'8500': ['OrderEntryTime', '订单申报时间', 'N', 'ntime']}]
                 }
    java_code = build_java_file(json_data)
    # 将生成的Java代码写入到一个文本文件中
    file_path = './StepTestAE.java'
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(java_code)
