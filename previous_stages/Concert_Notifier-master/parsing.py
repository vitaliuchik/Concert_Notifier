import requests
import bs4
import fake_useragent


ua = fake_useragent.UserAgent()
headers = {'User-Agent': ua.chrome}
def parser(artist_name):
    artist_name = artist_name.lower()
    site = requests.get('https://concert.ua/uk/event/' + artist_name, headers=headers)
    
    if str(site) != '<Response [200]>':
        return "There aren't any events for your search - " + artist_name
    
    site.encoding = 'cp1251'
    bs = bs4.BeautifulSoup(site.text, "html.parser")

    event_name = bs.select('.event-main-info__name-value')
    if event_name:
        event_name = event_name[0]
        return event_name.text.strip() + ' - https://concert.ua/uk/event/' + artist_name

    return "There aren't any events for your search - " + artist_name
    
    