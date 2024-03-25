package com.sse.iitp.protocol.converter.bo;

import com.sse.iitp.protocol.converter.enums.impl.StepMsgEnum;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.math.BigDecimal;
import java.util.List;

@Data
public class StepTradeCaptureReport extends StepOrderBase {

    public StepTradeCaptureReport() {
        super(StepMsgEnum.TRADE_CAPTURE_REPORT);
    }

    @ApiModelProperty(value = "业务类型，见附表|String", required = true)
    private String ApplID;

    @ApiModelProperty(value = "会员内部编号|String", required = true)
    private String TradeReportID;

    @ApiModelProperty(value = "业务子类型，见附表|String", required = false)
    private String TrdType;

    @ApiModelProperty(value = "成交申报类型
0=Submit，提交成交申报
2=Accept，确认成交申报
3=Decline，拒绝成交申报|String", required = true)
    private String TradeReportType;

    @ApiModelProperty(value = "成交申报事务类别
0=New，新申报
1=Cancel，撤销申报
2=Replace，响应|String", required = true)
    private String TradeReportTransType;

    @ApiModelProperty(value = "订单所有者类型
1=个人投资者
103=机构投资者
104=自营交易|Integer", required = true)
    private Integer OwnerType;

    @ApiModelProperty(value = "原始交易会员内部编号，表示被撤消订单的会员内部编号|String", required = false)
    private String TradeReportRefID;

    @ApiModelProperty(value = "买卖方向：1=买，2=卖
对于回购：1=正回购，2=逆回购
对于合并申报且TradeReportType为0时：填0|String", required = true)
    private String Side;

    @ApiModelProperty(value = "申报价格（元）或回购利率（%）
合并申报时代表买入价格|Object", required = false)
    private Object Price1;

    @ApiModelProperty(value = "申报价格2
合并申报时代表卖出价格（元）|Object", required = false)
    private Object Price2;

    @ApiModelProperty(value = "期限（天），可填[1,365]|Integer", required = false)
    private Integer ExpirationDays;

    @ApiModelProperty(value = "首次结算日|Object", required = false)
    private Object SettlDate;

    @ApiModelProperty(value = "到期日|Object", required = false)
    private Object MaturityDate;

    @ApiModelProperty(value = "到期结算日|Object", required = false)
    private Object SettlDate2;

    @ApiModelProperty(value = "实际占款天数（天），可填[1,365]|Integer", required = false)
    private Integer UAInterestAccrualDays;

    @ApiModelProperty(value = "业务发生时间|Object", required = true)
    private Object TransactTime;

    @ApiModelProperty(value = "总成交金额，四舍五入
预留，暂不启用|Object", required = false)
    private Object TotalValueTraded;

    @ApiModelProperty(value = "总回购利息，四舍五入
预留，暂不启用|Object", required = false)
    private Object TotalAccruedInterestAmt;

    @ApiModelProperty(value = "总到期结算金额，四舍五入
预留，暂不启用|Object", required = false)
    private Object TotalSettlCurrAmt;

    @ApiModelProperty(value = "违约宽限期（天），[0,365]。|Integer", required = false)
    private Integer NoDates;

    @ApiModelProperty(value = "订单限制
对于协议回购表示“是否同意在违约情形下由质权方对该违约交易项下的质押券直接以拍卖、变卖等方式进行处置”。
Y = 是
N = 否|String", required = false)
    private String ;

    @ApiModelProperty(value = "结算场所：1=中国结算，2=中央结算
双边托管券，可填1或2，单边托管券只能填其实际托管方。预留，暂不启用。|String", required = false)
    private String SecurityExchange;

    @ApiModelProperty(value = "结算周期：
0 = T+0
1 = T+1
2 = T+2
3 = T+3
预留，暂不启用|String", required = false)
    private String SettlPeriod;

    @ApiModelProperty(value = "结算方式：1=净额结算，2=RTGS结算。
担保券可填1或2；非担保券只能为2。|String", required = false)
    private String SettlType;

    @ApiModelProperty(value = "证券个数|Integer", required = false)
    private Integer NoUnderlyings;

    @ApiModelProperty(value = "证券代码|String", required = false)
    private String SecurityID;

    @ApiModelProperty(value = "证券数量|Object", required = false)
    private Object OrderQty;

    @ApiModelProperty(value = "份额类型
0 = 限售
1 = 非限售|String", required = false)
    private String ShareProperty;

    @ApiModelProperty(value = "限售期（月），可选：
0006、0012、0018、0024。|String", required = false)
    private String RestrictedMonth;

    @ApiModelProperty(value = "折算比例（%）|Integer", required = false)
    private Integer ContractMultiplier;

    @ApiModelProperty(value = "质押券面值总额|Object", required = false)
    private Object CashOrderQty;

    @ApiModelProperty(value = "成交金额|Object", required = false)
    private Object GrossTradeAmt;

    @ApiModelProperty(value = "回购利息|Object", required = false)
    private Object AccruedInterestAmt;

    @ApiModelProperty(value = "到期结算金额|Object", required = false)
    private Object SettlCurrAmt;

    @ApiModelProperty(value = "本期回购结算利息|Object", required = false)
    private Object OrderQty2;

    @ApiModelProperty(value = "到期续做类型
N = 非第三方续做
Y = 第三方续做|String", required = false)
    private String TrdSubType;

    @ApiModelProperty(value = "当TradeReportType为0时，原成交编号；
当TradeReportType为2或3时，表示待确认（拒绝）的申报的交易所订单编号。|String", required = false)
    private String ExecRefID;

    @ApiModelProperty(value = "发起方重复组，依次包含发起方的交易参与人代码、发起方交易员一债通账户、发起方业务单元、发起方营业务代码、投资者账户、账户名称、对手方交易员一债通账户1、对手方交易员一债通账户2。取值为8|Integer", required = true)
    private Integer NoPartyIDs;

    @ApiModelProperty(value = "发起方交易参与人机构代码|String", required = true)
    private String PartyID;

    @ApiModelProperty(value = "取12，表示当前PartyID的取值为发起方的交易参与人代码|Integer", required = true)
    private Integer PartyRole;

    @ApiModelProperty(value = "发起方交易员一债通账户|String", required = true)
    private String PartyID;

    @ApiModelProperty(value = "取101，表示当前PartyID的取值为发起方的交易员一债通账户|Integer", required = true)
    private Integer PartyRole;

    @ApiModelProperty(value = "发起方业务交易单元代码|String", required = true)
    private String PartyID;

    @ApiModelProperty(value = "取1，表示当前PartyID的取值为发起方业务交易单元号。|Integer", required = true)
    private Integer PartyRole;

    @ApiModelProperty(value = "发起方营业部代码|String", required = true)
    private String PartyID;

    @ApiModelProperty(value = "取4001，表示当前PartyID的取值为发起方的营业部代码。|Integer", required = true)
    private Integer PartyRole;

    @ApiModelProperty(value = "发起方投资者帐户，TradeReportType为0或2时必填。|String", required = false)
    private String PartyID;

    @ApiModelProperty(value = "取5，表示当前PartyID的取值为发起方投资者帐户|Integer", required = false)
    private Integer PartyRole;

    @ApiModelProperty(value = "仅对协议回购有效，协商成交、到期续做申报发起时为发起方投资者账户名称，确认时（TradeReportType=2）填写逆回购方证券账户名称。其他申报无意义。|String", required = false)
    private String PartyID;

    @ApiModelProperty(value = "取38，表示当前PartyID的取值为发起方投资者账户名称|Integer", required = false)
    private Integer PartyRole;

    @ApiModelProperty(value = "对手方交易员一债通账户1，当合并申报时表示买方交易员代码|String", required = true)
    private String PartyID;

    @ApiModelProperty(value = "取102，表示当前PartyID的取值为对手方的交易员一债通账户|Integer", required = true)
    private Integer PartyRole;

    @ApiModelProperty(value = "对手方交易员一债通账户2，仅合并申报时有效表示卖方交易员。其他申报无意义。|String", required = false)
    private String PartyID;

    @ApiModelProperty(value = "取57，表示当前的PartyID的取值为合并申报卖方|Integer", required = false)
    private Integer PartyRole;

    @ApiModelProperty(value = "约定号，TradeReportType=0时可以填写，用于对手方定位订单信息。仅可填大小写英文字母或数字。|String", required = false)
    private String ConfirmID;

    @ApiModelProperty(value = "备注，可填写补充约定或补充条款|String", required = false)
    private String Memo;

}
