# Python
import ccxt
exchange.load_markets()
symbol = 'BTC/USDT'
amount = 1.2345678  # amount in base currency BTC
price = 87654.321  # price in quote currency USDT
formatted_amount = exchange.amount_to_precision(symbol, amount)
formatted_price = exchange.price_to_precision(symbol, price)
print(formatted_amount, formatted_price)

# Python
okcoin = ccxt.okcoinusd()
markets = okcoin.load_markets()
print(okcoin.id, markets)

# Pytho- MARKET-STRUCTURE
print(exchange.load_markets())

etheur1 = exchange.markets['ETH/EUR']         # get market structure by symbol
etheur2 = exchange.market('ETH/EUR')          # same result in a slightly different way

etheurId = exchange.market_id('ETH/EUR')      # get market id by symbol

symbols = exchange.symbols                    # get a list of symbols
symbols2 = list(exchange.markets.keys())      # same as previous line

print(exchange.id, symbols)                   # print all symbols

currencies = exchange.currencies              # a dictionary of currencies

kraken = ccxt.kraken()
kraken.load_markets()

kraken.markets['BTC/USD']                     # symbol → market (get market by symbol)
kraken.markets_by_id['XXRPZUSD'][0]           # id → market (get market by id)

kraken.markets['BTC/USD']['id']               # symbol → id (get id by symbol)

# base currency ↓
            # BTC / USDT
            # ETH / BTC
            # DASH / ETH
                    #↑ quote currency

kraken.markets_by_id['XXRPZUSD'][0]['symbol'] # id → symbol (get symbol by id)
# Python
poloniex = ccxt.poloniex({'verbose': True}) # log HTTP requests
poloniex.load_markets() # request markets
print(poloniex.id, poloniex.markets)   # output a full list of all loaded markets
print(list(poloniex.markets.keys())) # output a short list of market symbols
print(poloniex.markets['BTC/ETH'])     # output single market details
poloniex.load_markets() # return a locally cached version, no reload
reloadedMarkets = poloniex.load_markets(True) # force HTTP reload = True
print(reloadedMarkets['ETH/ZEC'])

