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

    @ApiModelProperty(value = "平台内分区号|Integer", required = true)
    private Integer PartitionNo;

    @ApiModelProperty(value = "执行报告编号|Long", required = true)
    private Long ReportIndex;

    @ApiModelProperty(value = "会员内部编号|String(10)")
    private String TradeReportID;

    @ApiModelProperty(value = "交易所订单编号|String(16)")
    private String TradeID;

    @ApiModelProperty(value = "证券代码|String(12)")
    private String SecurityID;

    @ApiModelProperty(value = "成交申报类型\n" +
            "0=Submit，提交成交申报")
    private String TradeReportType;

    @ApiModelProperty(value = "成交申报事务类别\n" +
            "0=New，新申报\n" +
            "2=Replace，响应 ")
    private String TradeReportTransType;

    @ApiModelProperty(value = "执行报告类型，取值有：\n" +
            "F=Trade，成交")
    private String TrdAckStatus;

    @ApiModelProperty(value = "当前申报的状态，取值有：\n" +
            "2=Matched，已成交")
    private String TrdRptStatus;

    @ApiModelProperty(value = "被撤销订单的交易所订单编号|String(10)")
    private String OrigTradeID;

    @ApiModelProperty(value = "原始交易会员内部编号|String(10)")
    private String TradeReportRefID;

    @ApiModelProperty(value = "回购到期日|String(8)")
    private String MaturityDate;

    @ApiModelProperty(value = "实际占款天数|Integer(3)")
    private Integer UAInterestAccrualDays;

    @ApiModelProperty(value = "违约宽限天数|Integer(3)")
    private Integer NoDates;

    @ApiModelProperty(value = "总回购利息|BigDecimal")
    private BigDecimal TotalAccruedInterestAmt;

    @ApiModelProperty(value = "总到期结算金额|BigDecimal")
    private BigDecimal TotalSettlCurrAmt;

    @ApiModelProperty(value = "份额类型|String(1)")
    private String ShareProperty;

    @ApiModelProperty(value = "限售月|String(4)")
    private String RestrictedMonth;

    @ApiModelProperty(value = "是否同意进行处置|String(1)")
    private String OrderRestrictions;

    @ApiModelProperty(value = "结算场所|String(1)")
    private String SecurityExchange;

    @ApiModelProperty(value = "结算速度：1=T+0，2=T+1。仅对中央结算托管券有效。预留，暂不启用")
    private String SettlPeriod;

    @ApiModelProperty(value = "结算速度|String(1)")
    private String SettlType;

    @ApiModelProperty(value = "结算方式|String(1)")
    private String SettlementType;

    @ApiModelProperty(value = "成交价格|BigDecimal")
    private BigDecimal LastPx;

    @ApiModelProperty(value = "成交数量")
    private BigDecimal LastQty;

    @ApiModelProperty(value = "成交金额（元）\n" +
            "对债券现券交易，成交金额=成交价格*成交数量*10；对于基金，成交金额=成交价格*成交数量。\n" +
            "对协议回购成交申报和到期续作申报合约新开，填写回购成交金额；其他无效。")
    private BigDecimal GrossTradeAmt;

    @ApiModelProperty(value = "成交编号|String(8)")
    private String ExecID;

    @ApiModelProperty(value = "本期回购结算利息|BigDecimal(12,2)")
    private BigDecimal OrderQty2;

    @ApiModelProperty(value = "到期续做类型|String(1)")
    private String TrdSubType;

    @ApiModelProperty(value = "原成交日期或当前交易日|String(8)")
    private String OrigTradeDate;

    @ApiModelProperty(value = "原成交编号或待确认(拒绝)申报的交易所订单编号|String(16)")
    private String ExecRefID;

    @ApiModelProperty(value = "约定号|String(12)")
    private String ConfirmID;

    @ApiModelProperty(value = "订单所有者类型|Integer", required = true)
    private Integer OwnerType;

    @ApiModelProperty(value = "买卖方向|String(1)", required = true)
    private String Side;

    @ApiModelProperty(value = "申报价格或回购利率|BigDecimal(13,5)", required = true)
    private BigDecimal Price1;

    @ApiModelProperty(value = "合并申报时代表卖出价格|BigDecimal(13,5)", required = true)
    private BigDecimal Price2;

    @ApiModelProperty(value = "期限（天），可填[1,365]")
    private Integer ExpirationDays;

    @ApiModelProperty(value = "首次结算日|String(8)")
    private String SettlDate;

    @ApiModelProperty(value = "到期结算日|String(8)")
    private String SettlDate2;

    @ApiModelProperty(value = "折算比例")
    private Integer ContractMultiplier;

    @ApiModelProperty(value = "总成交金额|BigDecimal(16|2)")
    private BigDecimal TotalValueTraded;

    @ApiModelProperty(value = "业务发生时间|String(21)", required = true)
    private String TransactTime;

    @ApiModelProperty(value = "订单申报时间")
    private String OrderEntryTime;

    /**
     * TODO 证券集合
     * 有关该tag 实现以及命名，需要持续关注
     */
    @ApiModelProperty(value = "质押券个数|Integer(2)")
    private List<StepUndInstrmtGrp> NoUnderlyings;

    //以下字段非STEP标准协议所定义
    //实际使用中需要根据STEP规定的<Parties>组件定义中的PartyID和PartyRole解析
    @ApiModelProperty(value = "发起方交易参与人代码|String(12)")
    private String TradeParticipantsCode;

    @ApiModelProperty(value = "发起方交易员一债通账户|String(10)")
    private String TraderBntAccount;


    @ApiModelProperty(value = "发起方营业部代码|String(8)", required = true)
    private String BranchID;

    @ApiModelProperty(value = "发起方投资者账户|String(13)", required = true)
    private String Account;

    @ApiModelProperty(value = "发起方投资者账户名称|String(13)", required = true)
    private String AccountName;

    @ApiModelProperty(value = "对手方交易参与人机构代码|String(12)", required = true)
    private String CounterTraderOrgCode;

    @ApiModelProperty(value = "对手方交易员一债通账户(合并申报时表示买方交易员代码)|String(10)")
    private String CounterTraderBntAccount1;

    @ApiModelProperty(value = "对手方交易员一债通账户(合并申报时表示卖方交易员代码)|String(10)")
    private String CounterTraderBntAccount2;

    @ApiModelProperty(value = "质权人名称|String(120)")
    private String PledgeeName;

    @ApiModelProperty(value = "备注|String(900)")
    private String Memo;

    @ApiModelProperty(value = "补充条款|String(900)")
    private String Text;
}
