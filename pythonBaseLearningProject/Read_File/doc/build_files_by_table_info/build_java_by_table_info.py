# 根据更新的要求，我们将生成的Java代码调整为仅包含属性字段，并使用Lombok注解简化代码
# 同时，将代码输出到一个文本文件中而不是打印到控制台
json_data = {'AE': [{'1180': ['ApplID', '业务类型，见附表', 'Y', 'C6']},
                    {'571': ['TradeReportID', '会员内部编号', 'Y', 'C10']},
                    {'828': ['TrdType', '业务子类型，见附表', 'N', 'C3']},
                    {'856': ['TradeReportType', '成交申报类型\n0=Submit，提交成交申报\n2=Accept，确认成交申报\n3=Decline，拒绝成交申报', 'Y',
                                'C1']},
                    {'487': ['TradeReportTransType', '成交申报事务类别\n0=New，新申报\n1=Cancel，撤销申报\n2=Replace，响应', 'Y', 'C1']},
                    {'522': ['OwnerType', '订单所有者类型\n1=个人投资者\n103=机构投资者\n104=自营交易', 'Y', 'N3']},
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
                    {'580': ['NoDates', '违约宽限期（天），[0,365]。', 'N', 'N3']},
                    {'529': ['', '订单限制\n对于协议回购表示“是否同意在违约情形下由质权方对该违约交易项下的质押券直接以拍卖、变卖等方式进行处置”。\nY = 是\nN = 否', 'N',
                                'C1']},
                    {'207': ['SecurityExchange', '结算场所：1=中国结算，2=中央结算\n双边托管券，可填1或2，单边托管券只能填其实际托管方。预留，暂不启用。', 'N', 'C1']},
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
                    {'829': ['TrdSubType', '到期续做类型\nN = 非第三方续做\nY = 第三方续做', 'N', 'C1']},
                    {'19': ['ExecRefID', '当TradeReportType为0时，原成交编号；\n当TradeReportType为2或3时，表示待确认（拒绝）的申报的交易所订单编号。', 'N', 'C16']},
                    {'453': ['NoPartyIDs','发起方重复组，依次包含发起方的交易参与人代码、发起方交易员一债通账户、发起方业务单元、发起方营业务代码、投资者账户、账户名称、对手方交易员一债通账户1、对手方交易员一债通账户2。取值为8',
                                                      'Y', 'N2']},
                    {'448': ['PartyID', '发起方交易参与人机构代码', 'Y', 'C12']},
                    {'452': ['PartyRole', '取12，表示当前PartyID的取值为发起方的交易参与人代码', 'Y', 'N4']},
                    {'448': ['PartyID', '发起方交易员一债通账户', 'Y', 'C10']},
                    {'452': ['PartyRole', '取101，表示当前PartyID的取值为发起方的交易员一债通账户', 'Y', 'N4']},
                    {'448': ['PartyID', '发起方业务交易单元代码', 'Y', 'C8']},
                    {'452': ['PartyRole', '取1，表示当前PartyID的取值为发起方业务交易单元号。', 'Y', 'N4']},
                    {'448': ['PartyID', '发起方营业部代码', 'Y', 'C8']},
                    {'452': ['PartyRole', '取4001，表示当前PartyID的取值为发起方的营业部代码。', 'Y', 'N4']},
                    {'448': ['PartyID', '发起方投资者帐户，TradeReportType为0或2时必填。', 'N', 'C13']},
                    {'452': ['PartyRole', '取5，表示当前PartyID的取值为发起方投资者帐户', 'N', 'N4']},
                    {'448': ['PartyID', '仅对协议回购有效，协商成交、到期续做申报发起时为发起方投资者账户名称，确认时（TradeReportType=2）填写逆回购方证券账户名称。其他申报无意义。', 'N', 'C120']},
                    {'452': ['PartyRole', '取38，表示当前PartyID的取值为发起方投资者账户名称', 'N', 'N4']},
                    {'448': ['PartyID', '对手方交易员一债通账户1，当合并申报时表示买方交易员代码', 'Y', 'C10']},
                    {'452': ['PartyRole', '取102，表示当前PartyID的取值为对手方的交易员一债通账户', 'Y', 'N4']},
                    {'448': ['PartyID', '对手方交易员一债通账户2，仅合并申报时有效表示卖方交易员。其他申报无意义。', 'N', 'C10']},
                    {'452': ['PartyRole', '取57，表示当前的PartyID的取值为合并申报卖方', 'N', 'N4']},
                    {'664': ['ConfirmID', '约定号，TradeReportType=0时可以填写，用于对手方定位订单信息。仅可填大小写英文字母或数字。', 'N', 'C12']},
                    {'10198': ['Memo', '备注，可填写补充约定或补充条款', 'N', 'C900']}]}

# 更新Java类的基本结构，包括Lombok注解
class_name = "TradeOrder"
java_code = "import lombok.Data;\n\n@Data\n"
java_code += f"public class {class_name} {{\n"

# 为每个字段添加Java属性，不再添加getter和setter方法
for item in json_data['AE']:
    for key, value in item.items():
        field_name = value[0]  # 字段名称
        java_type = "String"  # 假设默认使用String，具体类型根据value[3]进行调整
        if value[3] == 'price' or value[3] == 'quantity':
            java_type = "double"
        elif value[3] == 'N2' or value[3] == 'N3' or value[3] == 'N4':
            java_type = "int"

        # 添加私有属性
        java_code += f"    private {java_type} {field_name};\n"

java_code += "}"

# 将生成的Java代码写入到一个文本文件中
file_path = './StepTestOrder.java'
with open(file_path, 'w') as file:
    file.write(java_code)
