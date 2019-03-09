# Наведено лише приклад роботи з 2ою частиною проекту, так як для реалізації першої (Google Play Music API)
# на даному етапі мені потрібно надавати свої персональні дані

# Парсинг concert.ua по заданому виконавцю

import requests
import bs4

artist_name = 'markul'
site = requests.get('https://concert.ua/uk/search-result?query=' + artist_name)

bs = bs4.BeautifulSoup(site.text, "html.parser")

events = bs.select('.event')
if events:
    event = events[0]
    event_name = event.select('.event__name')[0]
    print(event_name.string)
else:
    print("There aren't any events for your search")
