import scrapy
from proposal import *
from dictnames import DICTNAMES
from magic_regex import magic_regex
import pandas as pd

winners = {
    '1': Proposal('Marquez', '1'), '2': Proposal('Quartanaro', '2'),
    '3': Proposal('Viñales', '3'), 'vr': Proposal('Marquez', 'vr'),
    'pole': Proposal('Viñales', 'pole'), 'pi': Proposal('Quartanaro', 'pi')
}

class FCSpider(scrapy.Spider):
    name = "fc_spider"

    def start_requests(self):
        urls = [
            'https://www.forocoches.com/foro/showthread.php?p=345081693#post345081693'
        ]
        print(urls)
        self.load_winner()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('RESPONSE.URL: {}'.format(response.url))
        selector = response.css("table.tborder")
        for s in selector:
            username = s.css('a.bigusername::text').getall()
            if username:
                post_id = s.css('td.alt1::attr(id)').extract()
                sel = 'td#{}::text'.format(post_id[0])
                message = s.css(sel).getall()
                self.parse_message(username[0], message, post_id[0])
                print('\n')
        print(self.results)

    def parse_message(self, username, message, post_id=None):
        if post_id:
            print(post_id)
        message = [x for x in message if x != '\r\n\t\r\n\t\t\r\n\t\t\r\n\r\n\r\n']
        print('{}: {}'.format(username, message))
        results = magic_regex(message, username)
        for result in results:
            p = ProposalUser(**result)
            if result['position']:
                try:
                    test = winners[result['position'][0].lower()]
                    print('{} vs {}'.format(test, p))
                    if test == p:
                        points = p.get_points()
                        print('{}!!!!!!!!!!! and get {} POINTS'.format(p, points))
                        if username in self.results:
                            self.results[username] += points
                        else:
                            self.results[username] = points
                except:
                    continue

    def load_winner(self):
        self.results = {}
        self.winners = {}
        df = pd.read_csv('winners', sep=';', names=['pilot_name', 'position'])
        for elem in df.T.to_dict().values():
            self.winners[elem['position']] = elem['pilot_name']
        return True

    def write_results(self):
        with open('results.txt', 'w') as f_:
            for k, v in self.results.items():
                f_.writelines('{}: {}\n'.format(k, v))

