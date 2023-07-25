import ccxt 
import logging
logging.basicConfig(level=logging.DEBUG)

# currencies: An associative array (a dict) of currencies by codes (usually 3 or 4 letters) available with an exchange. 
# Currencies are loaded and reloaded from markets.
# Python

# enable built-in rate limiting upon instantiation of the exchange
exchange = ccxt.bitfinex({
    # 'enableRateLimit': True,  # enabled by default
})

# or switch the built-in rate-limiter on or off later after instantiation
exchange.enableRateLimit = True  # enable
exchange.enableRateLimit = False  # disable

# markets_by_id: An associative array of arrays of markets indexed by exchange-specific ids. 
# Typically a length one array unless there are multiple markets with the same marketId. 
# Markets should be loaded prior to accessing this property.

# apiKey: This is your public API key string literal. Most exchanges require API keys setup.

# secret: Your private secret API key string literal. Most exchanges require this as well together with the apiKey.

# password: A string literal with your password/phrase. Some exchanges require this parameter for trading, but most of them don't.

# SECURITY MEASURES: f you encounter DDoS protection errors and cannot reach a particular exchange then:

# Use a proxy (this is less responsive, though)
# Ask the exchange support to add you to a whitelist
# try an alternative IP within a different geographic region
# run your software in a distributed network of servers
# run your software in close proximity to the exchange (same country, same city, same datacenter, same server rack, same server)
