import requests
import bs4
import fake_useragent


class Parser:
    """Parser for events on concert.ua"""

    def parse(self, artist_name):
        """Parses concert.ua checking availability performance of this artist

        :param artist_name:
        :return: event_name, event_link: tuple
        """

        ua = fake_useragent.UserAgent()
        headers = {'User-Agent': ua.chrome}
        artist_name = artist_name.lower()
        site = requests.get('https://concert.ua/uk/event/' + artist_name,
                            headers=headers)

        if str(site) != '<Response [200]>':
            return False

        site.encoding = 'utf-8'
        bs = bs4.BeautifulSoup(site.text, "html.parser")

        event_name = bs.select('.event-main-info__name-value')
        if event_name:
            event_name = event_name[0]
            return event_name.text.strip(), \
                   'https://concert.ua/uk/event/' + artist_name

        return False
