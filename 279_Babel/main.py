"""
Babel is an integrated collection of utilities that assist in internationalizing and localizing Python applications, with an 
emphasis on web-based applications.

pip install Babel
"""
from babel import Locale

locale = Locale('en', 'US')
print(locale.territories['US'])
# print(locale)
locale = Locale('es', 'MX')
print(locale.territories['US'])
# print(locale)

"""
given a locale object you can ask it for its canonical display name, the name of the language and other things.
"""
l = locale.parse('en_US')
print(l.get_language_name('de_DE'))
print(l.get_language_name('it_IT'))
print(l.get_territory_name('it_IT'))
print(l.get_territory_name('pt_PT'))

# Calendar Display
locale = Locale('es')
month_names = locale.months['format']['wide'].items()
for idx, name in sorted(month_names):
    print(name)

from datetime import date, datetime, time
from babel.dates import format_date, format_datetime, format_time

d = date(2007, 4, 1)
print(format_date(d, locale='en'))
print(format_date(d, locale='en_IN'))
print(format_date(d, format='short', locale='en'))
print(format_date(d, format='long', locale='en'))
print(format_date(d, format='full', locale='en'))

d = date(2007, 4, 1)
print(format_date(d, "EEE, MMM d, ''yy", locale='en'))
print(format_date(d, "EEEE, d.M.yyyy", locale='de'))
print(format_date(d, "EEEE, d.M.yyyy", locale='en_IN'))

