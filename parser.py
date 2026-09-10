from __future__ import annotations
import struct
from dataclasses import dataclass
from dataclass import *
from util import read_uint48, parse_price

# Constants
big_endian_2_byte_format_str: str = ">H"
big_endian_4_byte_format_str: str = ">I"
big_endian_8_byte_format_str: str = ">Q"
alpha_encoding = "ascii"

# Data Type Parsers
def parse_system_event_message(msg: bytes) -> SystemEventMessage:
    return SystemEventMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        event_code=chr(msg[11])
    )

def parse_stock_directory(msg: bytes) -> StockDirectory:
    return StockDirectory(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        stock=msg[11:19].decode("ascii").strip(),
        market_category=chr(msg[19]),
        financial_status_indicator=chr(msg[20]),
        round_lot_size=struct.unpack_from(big_endian_4_byte_format_str, msg, 21)[0],
        round_lots_only=chr(msg[25]),
        issue_classification=chr(msg[26]),
        issue_subtype=msg[27:29].decode(alpha_encoding).strip(),
        authenticity=chr(msg[29]),
        short_sale_threshold_indicator=chr(msg[30]),
        ipo_flag=chr(msg[31]),
        luld_ref_price_tier=chr(msg[32]),
        etp_flag=chr(msg[33]),
        etp_leverage_factor=struct.unpack_from(big_endian_4_byte_format_str, msg, 24)[0],
        inverse_indicator=chr(msg[38])
    )

def parse_stock_trading_action(msg: bytes) -> StockTradingAction:
    return StockTradingAction(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        stock=msg[11:19].decode(alpha_encoding).strip(),
        trading_state=chr(msg[19]),
        reserved=chr(msg[20]),
        reason=msg[21:25].decode(alpha_encoding).strip(),
    )

def parse_reg_sho_restriction(msg: bytes) -> RegSHORestriction:
    return RegSHORestriction(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        stock=msg[11:19].decode(alpha_encoding).strip(),
        reg_SHO_action=chr(msg[19])
    )

def parse_market_participation_position(msg: bytes) -> MarketParticipantPosition:
    return MarketParticipantPosition(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        mpid=msg[11:15].decode(alpha_encoding).strip(),
        stock=msg[15:23].decode(alpha_encoding).strip(),
        primary_market_maker=chr(msg[23]),
        market_maker_mode=chr(msg[24]),
        market_participant_state=chr(msg[25])
    )

def parse_mwcb_decline_level_message(msg: bytes) -> MWCBDeclineLevelMessage:
    return MWCBDeclineLevelMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        level_1=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
        level_2=struct.unpack_from(big_endian_8_byte_format_str, msg, 19)[0],
        level_3=struct.unpack_from(big_endian_8_byte_format_str, msg, 27)[0]
    )

def parse_mwcb_status_message(msg: bytes) -> MWCBStatusMessage:
    return MWCBStatusMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        breached_level=chr(msg[11])
    )

def parse_quoting_period_update(msg: bytes) -> QuotingPeriodUpdate:
    return QuotingPeriodUpdate(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        stock=msg[11:19].decode(alpha_encoding).strip(),
        ipo_quotation_release_time=struct.unpack_from(big_endian_4_byte_format_str, msg, 19)[0],
        ipo_quotation_release_qualifier=chr(msg[23]),
        ipo_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 24)[0])
    )

def parse_luld_auction_collar(msg: bytes) -> LULDAuctionCollar:
    return LULDAuctionCollar(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        stock=msg[11:19].decode(alpha_encoding).strip(),
        auction_collar_ref_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 19)[0]),
        upper_auction_collar_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 23)[0]),
        lower_auction_collar_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 27)[0]),
        auction_collar_extension=struct.unpack_from(big_endian_4_byte_format_str, msg, 31)[0]
    )

def parse_operational_halt(msg: bytes) -> OperationalHalt:
    return OperationalHalt(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        stock=msg[11:19].decode(alpha_encoding).strip(),
        market_code=chr(msg[19]),
        operational_halt_action=chr(msg[20])
    )

def parse_add_order_message(msg: bytes) -> AddOrderMessage:
    return AddOrderMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        order_ref=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
        buy_sell_indicator=chr(msg[19]),
        shares=struct.unpack_from(big_endian_4_byte_format_str, msg, 20)[0],
        stock=msg[24:32].decode(alpha_encoding).strip(),
        price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 32)[0])
    )

def parse_add_order_mpid_attribution_message(msg: bytes) -> AddOrderMPIDAttributionMessage:
    return AddOrderMPIDAttributionMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        order_ref=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
        buy_sell_indicator=chr(msg[19]),
        shares=struct.unpack_from(big_endian_4_byte_format_str, msg, 20)[0],
        stock=msg[24:32].decode(alpha_encoding).strip(),
        price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 32)[0]),
        attribution=msg[36:40].decode(alpha_encoding).strip()
    )

def parse_order_executed_message(msg: bytes) -> OrderExecutedMessage:
    return OrderExecutedMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        order_ref=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
        executed_shares=struct.unpack_from(big_endian_4_byte_format_str, msg, 19)[0],
        match_number=struct.unpack_from(big_endian_8_byte_format_str, msg, 23)[0]
    )

def parse_order_executed_with_price_message(msg: bytes) -> OrderExecutedWithPriceMessage:
    return OrderExecutedWithPriceMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        order_ref=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
        executed_shares=struct.unpack_from(big_endian_4_byte_format_str, msg, 19)[0],
        match_number=struct.unpack_from(big_endian_8_byte_format_str, msg, 23)[0],
        printable=chr(msg[31]),
        execution_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 32)[0])
    )

def parse_order_cancel_message(msg: bytes) -> OrderCancelMessage:
    return OrderCancelMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        order_ref=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
        cancelled_shares=struct.unpack_from(big_endian_4_byte_format_str, msg, 19)[0]
    )

def parse_order_delete_message(msg: bytes) -> OrderDeleteMessage:
    return OrderDeleteMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        order_ref=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0]
    )

def parse_order_replace_message(msg: bytes) -> OrderReplaceMessage:
    return OrderReplaceMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        original_order_ref=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
        new_order_ref=struct.unpack_from(big_endian_8_byte_format_str, msg, 19)[0],
        shares=struct.unpack_from(big_endian_4_byte_format_str, msg, 27)[0],
        price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 31)[0])
    )

def parse_trade_message(msg: bytes) -> TradeMessage:
    return TradeMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        order_ref=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
        buy_sell_indicator=chr(msg[19]),
        shares=struct.unpack_from(big_endian_4_byte_format_str, msg, 20)[0],
        stock=msg[24:32].decode(alpha_encoding).strip(),
        price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 32)[0]),
        match_number=struct.unpack_from(big_endian_8_byte_format_str, msg, 36)[0]
    )

def parse_cross_trade_message(msg: bytes) -> CrossTradeMessage:
    return CrossTradeMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        shares=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
        stock=msg[19:27].decode(alpha_encoding).strip(),
        cross_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 27)[0]),
        match_number=struct.unpack_from(big_endian_8_byte_format_str, msg, 31)[0],
        cross_type=chr(msg[39])
    )

def parse_broken_trade_message(msg: bytes) -> BrokenTradeMessage:
    return BrokenTradeMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        match_number=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
    )

def parse_noii_message(msg: bytes) -> NOIIMessage:
    return NOIIMessage(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        paired_shares=struct.unpack_from(big_endian_8_byte_format_str, msg, 11)[0],
        imbalance_shares=struct.unpack_from(big_endian_8_byte_format_str, msg, 19)[0],
        imbalance_direction=chr(msg[27]),
        stock=msg[28:36].decode(alpha_encoding).strip(),
        far_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 36)[0]),
        near_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 40)[0]),
        current_ref_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 44)[0]),
        cross_type=chr(msg[48]),
        price_variation_indicator=chr(msg[49])
    )

def parse_dlwcrpd(msg: bytes) -> DLWCRPD:
    return DLWCRPD(
        stock_locate=struct.unpack_from(big_endian_2_byte_format_str, msg, 1)[0],
        tracking_number=struct.unpack_from(big_endian_2_byte_format_str, msg, 3)[0],
        timestamp=read_uint48(msg[5:11]),
        stock=msg[11:19].decode(alpha_encoding).strip(),
        open_eligibility_status=chr(msg[19]),
        minimum_allowable_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 20)[0]),
        maximum_allowable_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 24)[0]),
        near_execution_price=parse_price(struct.unpack_from(big_endian_4_byte_format_str, msg, 28)[0]),
        near_execution_time=struct.unpack_from(big_endian_8_byte_format_str, msg, 32)[0],
        lower_price_range_collar=struct.unpack_from(big_endian_4_byte_format_str, msg, 40)[0],
        upper_price_range_collar=struct.unpack_from(big_endian_4_byte_format_str, msg, 44)[0]
    )
