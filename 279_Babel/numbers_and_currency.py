from babel.numbers import format_currency, format_compact_currency, format_percent, format_scientific, parse_number
from babel import Locale

from babel.numbers import get_currency_symbol

# user_locale = Locale('en_US')
user_locale = Locale('en_IN')

currency_amount = 1234.56

formatted_currency = format_currency(currency_amount, 'USD', locale=user_locale)

print(formatted_currency)

print(format_currency(1099.98, 'EUR', u'¤¤ #,##0.00', locale='en_US'))
print(format_compact_currency(12345, 'USD', locale='en_US'))

print(format_percent(0.34, locale='en_US'))

print(format_scientific(10000, locale='en_US'))
print(format_scientific(1234567, u'##0.##E00', locale='en_US'))

# Parsing numbers
print(parse_number('1,099', locale='en_US'))

# Get currency notation
print(get_currency_symbol('USD', locale='en_US'))