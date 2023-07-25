# Python-Trading
A python trading algorithms with CCXT libraries to support crypto research and algorithmic performance

id: Each exchange has a default id. The id is not used for anything, it's a string literal for user-land exchange instance identification purposes. You can have multiple links to the same exchange and differentiate them by ids. Default ids are all lowercase and correspond to exchange names.

name: This is a string literal containing the human-readable exchange name.

countries: An array of string literals of 2-symbol ISO country codes, where the exchange is operating from.

urls['api']: The single string literal base URL for API calls or an associative array of separate URLs for private and public APIs.

urls['www']: The main HTTP website URL.

urls['doc']: A single string URL link to original documentation for exchange API on their website or an array of links to docs.

version: A string literal containing version identifier for current exchange API. The ccxt library will append this version string to the API Base URL upon each request. You don't have to modify it, unless you are implementing a new exchange API. The version identifier is a usually a numeric string starting with a letter 'v' in some cases, like v1.1. Do not override it unless you are implementing your own new crypto exchange class.

api: An associative array containing a definition of all API endpoints exposed by a crypto exchange. The API definition is used by ccxt to automatically construct callable instance methods for each available endpoint.

has: This is an associative array of exchange capabilities (e.g fetchTickers, fetchOHLCV or CORS).

timeframes: An associative array of timeframes, supported by the fetchOHLCV method of the exchange. This is only populated when has['fetchOHLCV'] property is true.


