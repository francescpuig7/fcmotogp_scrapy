import scrapy
from time import sleep

class UsersSpider(scrapy.Spider):
    name = "users_spider"

    def start_requests(self):
        self.u = []
        urls = [
            'https://www.forocoches.com/foro/showthread.php?t=6813735&highlight=porra+motogp&page=2',
            'https://www.forocoches.com/foro/showthread.php?t=6813735&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6793940&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6793940&highlight=porra+motogp&page=2',
            'https://www.forocoches.com/foro/showthread.php?t=6782720&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6782720&highlight=porra+motogp&page=2',
            'https://www.forocoches.com/foro/showthread.php?t=6617603&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6617603&highlight=porra+motogp&page=2',
            'https://www.forocoches.com/foro/showthread.php?t=5996795',
            'https://www.forocoches.com/foro/showthread.php?t=5503534',
            'https://www.forocoches.com/foro/showthread.php?t=5536379'
            'https://www.forocoches.com/foro/showthread.php?t=5564543'
            'https://www.forocoches.com/foro/showthread.php?t=5597114',
            'https://www.forocoches.com/foro/showthread.php?t=5629376',
            'https://www.forocoches.com/foro/showthread.php?t=5663002',
            'https://www.forocoches.com/foro/showthread.php?t=5680470',
            'https://www.forocoches.com/foro/showthread.php?t=5710851#post274886359',
            'https://www.forocoches.com/foro/showthread.php?p=285891394',
            'https://www.forocoches.com/foro/showthread.php?t=5842918',
            'https://www.forocoches.com/foro/showthread.php?t=5842918&page=0#post286058849',
            'https://www.forocoches.com/foro/showthread.php?t=5874563',
            'https://www.forocoches.com/foro/showthread.php?t=5907147',
            'https://www.forocoches.com/foro/showthread.php?t=5963177',
            'https://www.forocoches.com/foro/showthread.php?t=5978471',
            'https://www.forocoches.com/foro/showthread.php?t=6026894',
            'https://www.forocoches.com/foro/showthread.php?t=6570113&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6570113&highlight=porra+motogp&page=2',
            'https://www.forocoches.com/foro/showthread.php?t=6538296&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6538296&highlight=porra+motogp&page=2',
            'https://www.forocoches.com/foro/showthread.php?t=6509988&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6509988&highlight=porra+motogp&page=2',
            'https://www.forocoches.com/foro/showthread.php?t=6472261&highlight=porra+motogp'
            'https://www.forocoches.com/foro/showthread.php?t=6472261&highlight=porra+motogp&page=2',
            'https://www.forocoches.com/foro/showthread.php?t=6441072&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6441072&highlight=porra+motogp&page=2',
            'https://www.forocoches.com/foro/showthread.php?t=6392957&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6376247&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6333815&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6286211&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=6286211&highlight=porra+motogp&page=2',
            'https://www.forocoches.com/foro/showthread.php?t=6027536&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=5998288&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=5982291&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=5967101&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=5906700&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=5873555&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=5812129&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=5842240&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=5800134&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=5710348&highlight=porra+motogp',
            'https://www.forocoches.com/foro/showthread.php?t=5495539&highlight=porra+motogp'
        ]
        urls = []
        for i in range(2, 5):
           urls.append('https://www.forocoches.com/foro/showthread.php?t=7289319&highlight=motogp&page={}'.format(str(i)))
        print(urls)
        for url in urls:
            sleep(3)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        users = []
        page = response.url.split("/")[-2]
        print('RESPONSE.URL: {}'.format(response.url))
        for selector_ in response.xpath('.//a[@class="bigusername"]/text()').getall():
            if selector_ and selector_ not in self.u:
                users.append(selector_)
                self.u.append(selector_)
        users = list(set(users))
         
        with open('authors.txt', 'a+') as writer:
            # Write the dog breeds to the file in reversed order
            for x in users:
                writer.write('[MENTION]{}[\MENTION] '.format(x))
        for x in users:
            print('[MENTION]{}[\MENTION]'.format(x))
