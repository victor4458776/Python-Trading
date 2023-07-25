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

timeout: A timeout in milliseconds for a request-response roundtrip (default timeout is 10000 ms = 10 seconds). If the response is not received in that time, the library will throw an RequestTimeout exception. You can leave the default timeout value or set it to a reasonable value. Hanging forever with no timeout is not your option, for sure. You don't have to override this option in general case.

rateLimit: A request rate limit in milliseconds. Specifies the required minimal delay between two consequent HTTP requests to the same exchange. The built-in rate-limiter is enabled by default and can be turned off by setting the enableRateLimit property to false.

enableRateLimit: A boolean (true/false) value that enables the built-in rate limiter and throttles consecutive requests. This setting is true (enabled) by default. The user is required to implement own rate limiting or leave the built-in rate limiter enabled to avoid being banned from the exchange.

userAgent: An object to set HTTP User-Agent header to. The ccxt library will set its User-Agent by default. Some exchanges may not like it. If you are having difficulties getting a reply from an exchange and want to turn User-Agent off or use the default one, set this value to false, undefined, or an empty string. The value of userAgent may be overrided by HTTP headers property below.

headers: An associative array of HTTP headers and their values. Default value is empty {}. All headers will be prepended to all requests. If the User-Agent header is set within headers, it will override whatever value is set in the userAgent property above.
