#import cctx
# Python
import ccxt
exchange = ccxt.okcoinusd () # default id
okcoin1 = ccxt.okcoinusd ({ 'id': 'okcoin1' })
okcoin2 = ccxt.okcoinusd ({ 'id': 'okcoin2' })
id = 'btcchina'
btcchina = eval ('ccxt.%s ()' % id)
coinbasepro = getattr (ccxt, 'coinbasepro') ()

# from variable id
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
})

# HTTP HEADERS AND SERVER CUSTOMIZATION
# Python
#The exchange.setSandboxMode (true) / exchange.set_sandbox_mode (True) has to be your first call immediately after creating the exchange (before any other calls)
# To obtain the API keys to the sandbox the user has to register with the sandbox website of the exchange in question and create a sandbox keypair
# Sandbox keys are not interchangeable with production keys!
exchange = ccxt.binance ({
    'rateLimit': 10000,  # unified exchange property
    'headers': {
        'YOUR_CUSTOM_HTTP_HEADER': 'YOUR_CUSTOM_VALUE',
    },
    'options': {
        'adjustForTimeDifference': True,  # exchange-specific option
    }
})
exchange.options['adjustForTimeDifference'] = False

#TESTNETS
# Python
exchange = ccxt.binance(config)
exchange.set_sandbox_mode(True)  # enable sandbox mode


