import scrapy


class PrairiefrontierSpider(scrapy.Spider):
    name = "prairiefrontier"
    allowed_domains = ["web.archive.org"]
    # start_urls = ["https://web.archive.org/web/19990221054316/http://www.prairiefrontier.com/pfcards/Xtrapgs/midi.html"]
    start_urls = [
        # "https://quotes.toscrape.com/tag/humor/",
        "https://web.archive.org/web/19990220173318/http://www.prairiefrontier.com/pfcards/Xtrapgs/a-e.html"
    ]

    def parse(self, response):
        anchor_els = response.css("a::attr(href)").getall()
        midi_urls = [url for url in anchor_els if url.endswith('.mid')]
        # print(f"midi_urls: {midi_urls}")  

        yield {
            "url": response.url,
            "html": response.body,
            "midi_urls": midi_urls
        }
        # filename = response.url.split("/")[-1] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # for body in response.css("body"):
        #     yield {
        #         "body": body
        #     }
        pass
