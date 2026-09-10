from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class SystemEventMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    event_code: str

@dataclass
class StockDirectory:
    stock_locate: int
    tracking_number: int
    timestamp: int
    stock: str
    market_category: str
    financial_status_indicator: str
    round_lot_size: int
    round_lots_only: str
    issue_classification: str
    issue_subtype: str
    authenticity: str
    short_sale_threshold_indicator: str
    ipo_flag: str
    luld_ref_price_tier: str
    etp_flag: str
    etp_leverage_factor: int
    inverse_indicator: str

@dataclass
class StockTradingAction:
    stock_locate: int
    tracking_number: int
    timestamp: int
    stock: str
    trading_state: str
    reserved: str
    reason: str

@dataclass
class RegSHORestriction:
    stock_locate: int
    tracking_number: int
    timestamp: int
    stock: str
    reg_SHO_action: str

@dataclass
class MarketParticipantPosition:
    stock_locate: int
    tracking_number: int
    timestamp: int
    mpid: str
    stock: str
    primary_market_maker: str
    market_maker_mode: str
    market_participant_state: str

@dataclass
class MWCBDeclineLevelMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    level_1: int
    level_2: int
    level_3: int

@dataclass
class MWCBStatusMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    breached_level: str

@dataclass
class QuotingPeriodUpdate:
    stock_locate: int
    tracking_number: int
    timestamp: int
    stock: str
    ipo_quotation_release_time: int
    ipo_quotation_release_qualifier: str
    ipo_price: float

@dataclass
class LULDAuctionCollar:
    stock_locate: int
    tracking_number: int
    timestamp: int
    stock: str
    auction_collar_ref_price: float
    upper_auction_collar_price: float
    lower_auction_collar_price: float
    auction_collar_extension: int

@dataclass
class OperationalHalt:
    stock_locate: int
    tracking_number: int
    timestamp: int
    stock: str
    market_code: str
    operational_halt_action: str

@dataclass
class AddOrderMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    order_ref: int
    buy_sell_indicator: str
    shares: int
    stock: str
    price: float

@dataclass
class AddOrderMPIDAttributionMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    order_ref: int
    buy_sell_indicator: str
    shares: int
    stock: str
    price: float
    attribution: str

@dataclass
class OrderExecutedMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    order_ref: int
    executed_shares: int
    match_number: int
    printable: Optional[str] = None
    execution_price: Optional[float] = None

@dataclass
class OrderExecutedWithPriceMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    order_ref: int
    executed_shares: int
    match_number: int
    printable: str
    execution_price: float

@dataclass
class OrderCancelMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    order_ref: int
    cancelled_shares: int

@dataclass
class OrderDeleteMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    order_ref: int

@dataclass
class OrderReplaceMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    original_order_ref: int
    new_order_ref: int
    shares: int
    price: float

@dataclass
class TradeMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    order_ref: int
    buy_sell_indicator: str
    shares: int
    stock: str
    price: float
    match_number: int

@dataclass
class CrossTradeMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    shares: int
    stock: str
    cross_price: float
    match_number: int
    cross_type: str

class BrokenTradeMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    match_number: int

class NOIIMessage:
    stock_locate: int
    tracking_number: int
    timestamp: int
    paired_shares: int
    imbalance_shares: int
    imbalance_direction: str
    stock: str
    far_price: float
    near_price: float
    current_ref_price: float
    cross_type: str
    price_variation_indicator: str

# DLWCRPD = Direst Listing with Capital Raise Price Discovery
class DLWCRPD:
    stock_locate: int
    tracking_number: int
    timestamp: int
    stock: str
    open_eligibility_status: str
    minimum_allowable_price: float
    maximum_allowable_price: float
    near_execution_price: float
    near_execution_time: int
    lower_price_range_collar: float
    upper_price_range_collar: float

Message = Union[
    SystemEventMessage, StockDirectory, StockTradingAction, RegSHORestriction, 
    MarketParticipantPosition, MWCBDeclineLevelMessage, MWCBStatusMessage, 
    QuotingPeriodUpdate, LULDAuctionCollar, OperationalHalt, AddOrderMessage, 
    AddOrderMPIDAttributionMessage, OrderExecutedMessage, OrderExecutedWithPriceMessage,
    OrderCancelMessage, OrderDeleteMessage, OrderReplaceMessage, TradeMessage, 
    CrossTradeMessage, BrokenTradeMessage, NOIIMessage, DLWCRPD
]