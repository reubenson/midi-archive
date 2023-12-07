import scrapy
from urllib.parse import urlparse
import os

PRAIRIEFRONTIER_URLS = [
    "https://web.archive.org/web/19990220173318/http://www.prairiefrontier.com/pfcards/Xtrapgs/a-e.html",
    # "https://web.archive.org/web/19990220173318/http://www.prairiefrontier.com/pfcards/Xtrapgs/f-j.html",
    # "https://web.archive.org/web/19990220173318/http://www.prairiefrontier.com/pfcards/Xtrapgs/k-o.html",
    # "https://web.archive.org/web/19990220173318/http://www.prairiefrontier.com/pfcards/Xtrapgs/p-s.html",
    # "https://web.archive.org/web/19990220173318/http://www.prairiefrontier.com/pfcards/Xtrapgs/t-v.html"
]

PERSO_URLS = [
    
]

SITES = {
    "prairiefrontier": {},
    "perso": {
        "urls": [
            # "https://web.archive.org/web/20041010183445/http://perso.club-internet.fr/brassy/PartMed/Machaut/Machaut.html",
            # "https://web.archive.org/web/20040911094212/http://perso.club-internet.fr/brassy/PartMed/motet/Motets.html",
            # "https://web.archive.org/web/20041013001542/http://perso.club-internet.fr/brassy/PartMed/Adam/Adam.html",
            # "https://web.archive.org/web/20041103004027/http://perso.club-internet.fr/brassy/PartMed/Carmbur/CarmBur.html",
            # "https://web.archive.org/web/20041013013556/http://perso.club-internet.fr/brassy/PartMed/Minnesang/Minnesang.html",
            # "https://web.archive.org/web/20040901101624/http://perso.club-internet.fr/brassy/PartMed/Amigo/amigo.html",
            # "https://web.archive.org/web/20041013090228/http://perso.club-internet.fr/brassy/PartMed/Cantigas/CSMIDI.html",
            # "https://web.archive.org/web/20040808164445/http://perso.club-internet.fr/brassy/PartMed/Coincy/COINCY.html",
            # "https://web.archive.org/web/20040903012724/http://perso.club-internet.fr/brassy/PartMed/estampit/estampit.html",
            # "https://web.archive.org/web/20040903213121/http://perso.club-internet.fr/brassy/PartMed/Chans15/ChansXV.html",
            # "https://web.archive.org/web/20040813151011/http://perso.club-internet.fr/brassy/PartMed/Inst15/inst15.html",
            # "https://web.archive.org/web/20041205092511/http://perso.club-internet.fr/brassy/PartMed/Bayeux/Bay.html",
            # "https://web.archive.org/web/20040911094822/http://perso.club-internet.fr/brassy/PartMed/Trecento/trecento.html",
            # "https://web.archive.org/web/20040903213903/http://perso.club-internet.fr/brassy/PartMed/Flandres/musflam.html",
            # "https://web.archive.org/web/20041105171205/http://perso.club-internet.fr/brassy/PartMed/LiVerm/LiVerm.html"
        ]
    },
    "vietvet": {
        "urls": [
            "http://www.vietvet.org/audio/playlist.htm"
        ]
    },
    "irishmidifiles": {
        "urls": [
            "http://www.irishmidifiles.ie/midifiles.htm"
        ]
    },
    "aol_israelmidi": {
        "urls": [
            "https://web.archive.org/web/20011211192009/http://members.aol.com/israelmidi/index.html"
        ]
    },
    "laurasmidiheaven": {
        "urls": [
            "https://web.archive.org/web/19990417070447/http://www.laurasmidiheaven.simplenet.com/VideoGms.htm",
            "https://web.archive.org/web/19990417070447/http://www.laurasmidiheaven.simplenet.com/VideoGms2.htm",
            "https://web.archive.org/web/19990417070447/http://www.laurasmidiheaven.simplenet.com/VideoGms3.htm",
            "https://web.archive.org/web/19990417070447/http://www.laurasmidiheaven.simplenet.com/VideoGms4.htm",
            "https://web.archive.org/web/19990417070447/http://www.laurasmidiheaven.simplenet.com/VideoGms5.htm",
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5cd.htm"
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5ef.htm",
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5gh.htm",
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5ij.htm",
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5kl.htm",
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5mn.htm",
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5op.htm",
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5qr.htm",
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5st.htm",
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5uvw.htm",
            "https://web.archive.org/web/19990503120959/http://www.laurasmidiheaven.simplenet.com/VideoGms5xyz.htm",
            "https://web.archive.org/web/19990417070447/http://www.laurasmidiheaven.simplenet.com/VideoGms6.htm",
            "https://web.archive.org/web/19990417070447/http://www.laurasmidiheaven.simplenet.com/VideoGms7.htm",
        ]
    }
}

def waybackify(url):
    print(f"url (waybackify): {url}")
    # return early if we're not dealing with a wayback machine snapshot
    # print(f"url: {url}")
    if not 'web.archive.org' in url:
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
        yield scrapy.Request(
            waybackify(response.urljoin(urls[i]))
        )
        i+=1

class PrairiefrontierSpider(scrapy.Spider):
    name = 'archive'
    target = 'laurasmidiheaven'

    # allowed_domains = ["web.archive.org"]
    start_urls = SITES[target]["urls"]

    def parse(self, response):
        # print(f"response.url: {response.url}")
        # some responses for .mid are ending up here ?
        # To Do: refactor this to be more generalized, or keep requests from cycling back in
        if '.mid' in response.url.lower() or '.jpg' in response.url.lower() or '.png' in response.url.lower():
            return

        anchor_els = response.css("a::attr(href)").getall()
        midi_urls = list(set([url for url in anchor_els if url.lower().endswith('.mid')]))
        img_els = list(set([url for url in response.css("img::attr(src)").getall() if url.startswith('/web')]))#this is maybe a bit specific to wayback machine scraping
        
        # lil hacky for now
        background_els = [url for url in response.css("body::attr(background)").getall() if url.startswith('/web')]

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
            "background_urls": background_els
        }

        pass

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
