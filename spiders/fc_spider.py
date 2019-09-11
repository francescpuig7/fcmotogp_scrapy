import scrapy


class FCSpider(scrapy.Spider):
    name = "fc_spider"

    def start_requests(self):
        urls = [
            'https://www.forocoches.com/foro/showthread.php?t=6813735&highlight=porra+motogp&page=2',
        ]
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        print('RESPONSE.URL: {}'.format(response.url))
        selector = response.css("table.tborder")
        for s in selector:
            username = s.css('a.bigusername::text').getall()
            if username:
                post_id = s.css('td.alt1::attr(id)').extract()
                # message = s.xpath('//td[@class="alt1"]')
                sel = 'td#{}::text'.format(post_id[0])
                message = s.css(sel).getall()
                self.parse_message(username[0], message, post_id[0])

    @staticmethod
    def parse_message(username, message, post_id=None):
        print(username)
        if post_id:
            print(post_id)
        print([x for x in message if x != '\r\n\t\r\n\t\t\r\n\t\t\r\n\r\n\r\n'])

