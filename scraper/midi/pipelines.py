# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from urllib.parse import urlparse
import os
import requests
from bs4 import BeautifulSoup

def update_html(html, midi_files, img_files, background_files, sitename=""):
    soup = BeautifulSoup(html, 'html.parser')

    if not sitename:
        print("No sitename provided")
        return
    # TO DO: remove Internet Archive boilerplate, but maybe note on which snapshot this was pulled from

    # anchor_els = soup.find_all('a', href=True)
    # print(f"anchor_els: {anchor_els}")
    # midi_urls = [url for url in anchor_els if url.endswith('.mid')]

    # print(f"midi_urls: {midi_urls}")

    for url in midi_files:
        a = soup.find('a', href=url)
        # print(f"a: {a}")
        # print(f"url: {url}")
        filename = os.path.basename(urlparse(url).path)
        a['href'] = f'/assets/{sitename}/midi/{filename}'

    for url in img_files:
        el = soup.find('img', src=url)
        # print(f"url: {url}")
        filename = os.path.basename(urlparse(url).path.split("/")[-1]) # need to standardize this across (helper fn)
        # print(f"filename: {filename}")
        el['src'] = f'/assets/{sitename}/images/{filename}'
        # print(f"el: {el}")

    for url in background_files:
        el = soup.find('body', background=url) # TO DO generalize to any element
        # print(f"url: {url}")
        filename = os.path.basename(urlparse(url).path.split("/")[-1]) # need to standardize this across (helper fn)
        print(f"filename: {filename}")
        el['background'] = f'/assets/{sitename}/images/{filename}'
        # print(f"el: {el}")

    # for a, midi_file in zip(soup.find_all('a'), midi_files):
    #     print(f"a: {a}")
    #     print(f"midi_file: {midi_file}")
    #     a['href'] = f'assets/midi/prariefrontier/{midi_file}'

    return str(soup.find('body'))

# Usage
# html = '<html><body><a href="old_link1.midi"></a><a href="old_link2.midi"></a></body></html>'
# midi_files = ['file1.midi', 'file2.midi']
# new_html = update_html(html, midi_files)
# print(new_html) 

def getHostFromUrl(url):
    parsed = urlparse(url)
    print(f"parsed: {parsed}")
    scheme, netloc, path = parsed.scheme, parsed.netloc, parsed.path
    # print(f"parsed.path: {parsed.path}")
    return scheme + "://" + netloc
    # return url.split("/")[0]

def download_files(asset_urls, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for url in asset_urls:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_name = os.path.basename(urlparse(url).path)
            print(f"file_name: {file_name}")
            with open(os.path.join(save_dir, file_name), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {file_name}")
        else:
            # TO DO: handle these by marking up html
            print(f"Failed to download {url}")

def generate11tyHead():
    # TO DO: update placeholder values
    description = "Prairie Frontier Cards"
    keywords = "Prairie Frontier Cards, midi, music, 90s"
    layout: "layout.njk" # fine to hard-code this for now

    return f"""---
description: {description}
keywords: {keywords}
layout: layout.njk
---
"""


# class MidiPipeline:
#     def process_item(self, item, spider):
#         # print(f"item: {item}")
#         html = item["html"]
#         url = item["url"]
#         img_urls = item["img_urls"]
#         background_urls = item["background_urls"]

#         # print(f"background_urls: {background_urls}")

#         # for midi_url in item["midi_urls"][:2]:
#             # print(f"midi_url: {midi_url}")
#         domain = getHostFromUrl(url)
#         path = urlparse(url).path.split("/")[-1]
#         print(f"domain: {domain}")
#         print(f"path: {path}")
#         midi_urls = item["midi_urls"]

#         # TO DO: wrapper function for this
#         midi_urls_with_domain = [domain+url for url in item["midi_urls"]]
#         img_urls_with_domain = [domain+url for url in item["img_urls"]]
#         background_urls_with_domain = [domain+url for url in item["background_urls"]]

#         site_dir = 'prairiefrontier'

#         # download_files(midi_urls_with_domain[:], "../src/assets/prairiefrontier/midi")
#         # download_files(img_urls_with_domain[:], "../src/assets/prairiefrontier/images")
#         # download_files(background_urls_with_domain[:], "../src/assets/prairiefrontier/images")
#             # yield scrapy.Request(midi_url, callback=self.parse_midi)

#         # update html to point to midi files in assets/midi/prariefrontier
#         new_html = update_html(item["html"], midi_urls[:], img_urls[:], background_urls[:])
#         # save html file to sites/prariefrontier/index.html

#         # add 11ty variables on top of html
#         md_head = generate11tyHead()
#         print(f"md_head: {md_head}")

#         # print(f"body: {body}")
#         # need to save body to .html file
#         # filename = url.split("/")[-1] + '.html'
#         save_dir = f"../src/{site_dir}"
#         if not os.path.exists(save_dir):
#             os.makedirs(save_dir)
#         with open(f"{save_dir}/{path.replace('.html', '.md')}", 'w') as f:
#             f.write(md_head + new_html)

#         return item

# this pipeline is responsible for downloading and processing the scraped html
class HtmlPipeline:
    def process_item(self, item, spider):
        html = item["html"]
        url = item["url"]
        midi_urls = item["midi_urls"]
        img_urls = item["img_urls"]
        background_urls = item["background_urls"]    
        
        new_html = update_html(html, midi_urls[:], img_urls[:], background_urls[:], sitename=spider.target)
        
        # add 11ty variables on top of html
        md_head = generate11tyHead()

        # print(f"body: {body}")
        # need to save body to .html file
        # filename = url.split("/")[-1] + '.html'
        path = urlparse(url).path.split("/")[-1]

        # site_dir = 'prairiefrontier'
        site_dir = spider.target
        save_dir = f"../src/{site_dir}"

        print(f"save_dir: {save_dir}")
        print(f"path: {path}")
        print(f"site_dir: {site_dir}")

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        with open(f"{save_dir}/{path.replace('.html', '.md')}", 'w') as f:
            f.write(md_head + new_html)

        return item


# class DownloadItemPipeline:
#     def process_item(self, item, spider):
#         # response = item["response"]
#         # print(f"response.status: {response.status}")
#         # print(f"response.content: {response.content}")
#         # url = response.url
#         # print(f"response in DownloadItemPipeline: {response}")
#         # print('url: ', url)
#         # save_dir = '/assets/prairiefrontier/midi'
#         # if response.status_code == 200:
#         #     file_name = os.path.basename(urlparse(url).path)
#         #     print(f"file_name: {file_name}")
#         #     # with open(os.path.join(save_dir, file_name), 'wb') as f:
#         #     #     f.write(response.content)
#         #     print(f"Downloaded {file_name}")
#         return item