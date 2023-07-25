# install CCTX via pip
# pip install cctx
# TRADING ECOSYSTEMS /BITCOIN/ETHEREUM/TRANSACTIONS
>>> import ccxt
>>> print(ccxt.exchanges)
['ace', 'alpaca', 'ascendex', 'bequant', 'bigone', 'binance', 'binancecoinm', 'binanceus', 'binanceusdm', 'bingx', 'bit2c', 'bitbank',
 'bitbay', 'bitbns', 'bitcoincom', 'bitfinex', 'bitfinex2', 'bitflyer', 'bitforex', 'bitget', 'bithumb', 'bitmart', 'bitmex',
 'bitopro', 'bitpanda', 'bitrue', 'bitso', 'bitstamp', 'bitstamp1', 'bittrex', 'bitvavo', 'bkex', 'bl3p', 'blockchaincom', 
 'btcalpha', 'btcbox', 'btcmarkets', 'btctradeua', 'btcturk', 'bybit', 'cex', 'coinbase', 'coinbaseprime', 'coinbasepro',
 'coincheck', 'coinex', 'coinfalcon', 'coinmate', 'coinone', 'coinsph', 'coinspot', 'cryptocom', 'currencycom', 'delta', 'deribit',
 'digifinex', 'exmo', 'fmfwio', 'gate', 'gateio', 'gemini', 'hitbtc', 'hitbtc3', 'hollaex', 'huobi', 'huobijp', 'huobipro', 'idex',
 'independentreserve', 'indodax', 'kraken', 'krakenfutures', 'kucoin', 'kucoinfutures', 'kuna', 'latoken', 'lbank', 'lbank2', 
 'luno', 'lykke', 'mercado', 'mexc', 'mexc3', 'ndax', 'novadax', 'oceanex', 'okcoin', 'okex', 'okex5', 'okx', 'paymium', 'phemex', 
 'poloniex', 'poloniexfutures', 'probit', 'tidex', 'timex', 'tokocrypto', 'upbit', 'wavesexchange', 'wazirx', 'whitebit', 'woo', 'yobit', 'zaif', 'zonda']

# The library supports concurrent asynchronous mode with asyncio and async/await in Python 3.5.3+
>>> import ccxt.async_support as ccxt

# DOCS
# market data
# instruments/trading pairs
# price feeds (exchange rates)
# order books
# trade history
# tickers
# OHLC(V) for charting
# other public endpoints
