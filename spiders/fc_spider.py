import scrapy
from proposal import *
from dictnames import DICTNAMES

class FCSpider(scrapy.Spider):
    name = "fc_spider"

    def start_requests(self):
        urls = [
            'https://www.forocoches.com/foro/showthread.php?t=7382028&highlight=',
        ]
        print(urls)
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
                print(ProposalUser(username[0], 'Rossi', '1'))
                print(self.parse_message(username[0], message, post_id[0]))
                print('\n\n')

    @staticmethod
    def parse_message(username, message, post_id=None):
        if post_id:
            print(post_id)
        message = [x for x in message if x != '\r\n\t\r\n\t\t\r\n\t\t\r\n\r\n\r\n']
        for m in message:
            print(m.lower())
            if m.lower() in DICTNAMES:
                print(m)

    def load_winner(self):
        pass

