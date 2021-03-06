import scrapy
from proposal import *
from user import User
from magic_regex import magic_regex
import pandas as pd

class FCSpider(scrapy.Spider):
    name = "fc_spider"

    def start_requests(self):
        urls = [
"https://www.forocoches.com/foro/showthread.php?t=7456282&highlight="
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
        self.write_results()

    def parse_message(self, username, message, post_id=None):
        if post_id:
            print(post_id)
        message = [x for x in message if x != '\r\n\t\r\n\t\t\r\n\t\t\r\n\r\n\r\n']
        print('{}: {}'.format(username, message))
        results = magic_regex(message, username)
        user_ = User(username, n_proposals=0)
        for result in results:
            p = ProposalUser(**result)
            if result['position']:
                try:
                    test = self.winners[result['position'].lower()]
                    print('{} vs {}'.format(test, p))
                    if username not in self.results:
                        self.results[username] = 1
                    if test == p:
                        points = p.points
                        print('{}!!!!!!!!!!! and get {} POINTS'.format(p, points))
                        self.results[username] += points
                    user_.update_proposals()
                except Exception as err:
                    continue
        if user_.n_proposals != 8:
            self.results[user_.name] = 'manual?'
            print('NO - Manual? #Votes: {}'.format(user_.n_proposals))
        else:
            print('ok #Votes: {}'.format(user_.n_proposals))

    def load_winner(self):
        self.results = {}
        self.winners = {}
        df = pd.read_csv('winners', sep=';', names=['pilot_name', 'position'])
        for elem in df.T.to_dict().values():
            self.winners[elem['position']] = Proposal(elem['pilot_name'], elem['position'])
        return True

    def write_results(self):
        with open('results.txt', 'w') as f_:
            for k, v in self.results.items():
                f_.writelines('{}: {}\n'.format(k, v))

