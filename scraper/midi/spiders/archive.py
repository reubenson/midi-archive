import scrapy
from urllib.parse import urlparse
import os
import json

with open("../sites.json", "r") as file:
    SITES = json.load(file)


def waybackify(url):
    print(f"url (waybackify): {url}")
    if not "web.archive.org" in url:
        return url
    if url.lower().endswith(".mid"):
        split = url.split("/http")
        joined = f"{split[0]}if_/http{split[1]}"
        return joined
    else:
        return url


def initiate_download_assets(response, urls):
    i = 0
    while i < len(urls):
        yield scrapy.Request(waybackify(response.urljoin(urls[i])))
        i += 1


class ArchiveSpider(scrapy.Spider):
    name = "archive"
    target = "laurasmidiheaven"

    # allowed_domains = ["web.archive.org"]
    start_urls = SITES[target]["urls"]
    # uncomment to scrape manually defined
    # start_urls = [
    #     "https://web.archive.org/web/19981205192725/http://laurasmidiheaven.simplenet.com/rockm-p.htm"
    # ]

    def parse(self, response):
        # print(f"response.url: {response.url}")
        # some responses for .mid are ending up here ?
        # To Do: refactor this to be more generalized, or keep requests from cycling back in
        if (
            ".mid" in response.url.lower()
            or ".jpg" in response.url.lower()
            or ".png" in response.url.lower()
        ):
            return

        # anchor_els = response.css('a').getall()
        anchor_hrefs = response.css("a::attr(href)").getall()
        midi_urls = list(
            set([url for url in anchor_hrefs if url.lower().endswith(".mid")])
        )
        # this is maybe a bit specific to wayback machine scraping
        # img_els = list(set([url for url in response.css("img::attr(src)").getall() if url.startswith('/web')]))#this is maybe a bit specific to wayback machine scraping
        img_els = list(
            set([url for url in response.css("img::attr(src)").getall()])
        ) 

        # lil hacky for now
        background_els = [
            url
            for url in response.css("body::attr(background)").getall()
            if url.startswith("/web")
        ]

        # download midi files
        for req in initiate_download_assets(response, midi_urls[:]):
            yield req

        # download images
        # for req in initiate_download_assets(response, img_els):
        #     yield req

        yield {
            "url": response.url,
            "html": response.body,
            "midi_urls": midi_urls,
            "img_urls": img_els,
            "background_urls": background_els,
        }

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
        # filename = response.url.split("/")[-1] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # for body in response.css("body"):
        #     yield {
        #         "body": body
        #     }
        pass
