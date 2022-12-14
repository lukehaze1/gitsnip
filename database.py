from peewee import *

db = MySQLDatabase('fitalgo', host='127.0.0.1', port=0, user='root', password='COCOMOMO987')
class BaseModel(Model):
    class Meta:
        database = db

class Token(BaseModel):
    name = FloatField()
    token = CharField(primary_key=True)
    base_pair = CharField()
    symbol = CharField()
    dex = CharField()
    liquidity = IntegerField()
    buy_tax = FloatField()
    sell_tax = FloatField()
    buy_gas = IntegerField()
    sell_gas = IntegerField()
    pair_address = CharField()
    approved = IntegerField()
    limit = IntegerField()
    algo = CharField()

class Position(BaseModel):
    token = CharField(primary_key=True)
    name = CharField()
    base_pair = CharField()
    buy_price = FloatField()
    sell_price = FloatField()
    stop_price = FloatField()
    take_price = FloatField()
    trailing_stop = IntegerField()
    trailing_stop_price = FloatField()
    position = CharField()
    amount = IntegerField()
    buy_timestamp = DateTimeField()
    timeframe = IntegerField()
    algon = IntegerField()
    loss_count = IntegerField()

class Report(BaseModel):
    token = CharField(primary_key=True)
    name = CharField()
    buy_timestamp = DateTimeField()
    sell_timestamp = DateTimeField()
    amount = IntegerField()
    win_loss = FloatField()
    profit_percent = FloatField()
    profit_amount = FloatField()
    balance = FloatField()

class Candle(BaseModel):
    id = IntegerField(primary_key=True)
    token_id = ForeignKeyField(Token, backref='candles')
    signal = IntegerField()
    timestamp = DateTimeField()
    open = FloatField()
    high = FloatField()
    low = FloatField()
    close = FloatField()
    volume = FloatField()
    signal = IntegerField()

class Snapshot(BaseModel):
    id = IntegerField(primary_key=True)
    h24_buys = IntegerField()
    h24_sells = IntegerField()
    h6_buys = IntegerField()
    h6_sells = IntegerField()
    h1_buys = IntegerField()
    h1_sells = IntegerField()
    m5_buys = IntegerField()
    m5_sells = IntegerField()
    h24_volume = FloatField()
    h6_volume = FloatField()
    h1_volume = FloatField()
    m5_volume = FloatField()
    h24_price_change = FloatField()
    h6_price_change = FloatField()
    h1_price_change = FloatField()
    m5_price_change = FloatField()
    liquidity = CharField()
    chain_id = CharField()
    dex_id = CharField()
    url = CharField()
    pair_address = CharField()
    address = CharField()
    name = CharField()
    symbol = CharField()
    quote_symbol = CharField()
    price_native = FloatField()
    price_usd = FloatField()
    token_id = ForeignKeyField(Token, backref='snapshots')
    pair_created = IntegerField()
    datetime = DateTimeField()

class Buystop(BaseModel):
    token = CharField(primary_key=True)
    price = FloatField()
    stop_loss = FloatField()
    done = FloatField()
    name = CharField()

class Limit(BaseModel):
    token = CharField(primary_key=True)
    price = FloatField()
    stop_loss = FloatField()
    done = FloatField()
    name = CharField()

class Price(BaseModel):
    token = CharField(primary_key=True)
    price = FloatField()
    name = CharField()
    timestamp = DateTimeField()

class TestData(BaseModel):
    id = IntegerField(primary_key=True)
    timeframe = IntegerField()
    timestamp = DateTimeField()
    signal = IntegerField()
    open = FloatField()
    high = FloatField()
    low = FloatField()
    close = FloatField()
    volume = FloatField()
    token_id = ForeignKeyField(Token, backref='charts')

class TestData2(BaseModel):
    id = IntegerField(primary_key=True)
    timeframe = IntegerField()
    timestamp = DateTimeField()
    signal = IntegerField()
    open = FloatField()
    high = FloatField()
    low = FloatField()
    close = FloatField()
    volume = FloatField()
    token_id = ForeignKeyField(Token, backref='charts2')

class TestData3(BaseModel):
    id = IntegerField(primary_key=True)
    timeframe = IntegerField()
    timestamp = DateTimeField()
    signal = IntegerField()
    open = FloatField()
    high = FloatField()
    low = FloatField()
    close = FloatField()
    volume = FloatField()
    token_id = ForeignKeyField(Token, backref='charts3')


class TestData4(BaseModel):
    id = IntegerField(primary_key=True)
    timeframe = IntegerField()
    timestamp = DateTimeField()
    signal = IntegerField()
    open = FloatField()
    high = FloatField()
    low = FloatField()
    close = FloatField()
    volume = FloatField()
    token_id = ForeignKeyField(Token, backref='charts4')


db.connect()
