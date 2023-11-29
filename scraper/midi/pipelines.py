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

def update_html(html, midi_files):
    soup = BeautifulSoup(html, 'html.parser')

    # anchor_els = soup.find_all('a', href=True)
    # print(f"anchor_els: {anchor_els}")
    # midi_urls = [url for url in anchor_els if url.endswith('.mid')]

    # print(f"midi_urls: {midi_urls}")

    for url in midi_files:
        a = soup.find('a', href=url)
        print(f"a: {a}")
        print(f"url: {url}")
        filename = os.path.basename(urlparse(url).path)
        a['href'] = f'assets/midi/prariefrontier/{filename}'

    # for a, midi_file in zip(soup.find_all('a'), midi_files):
    #     print(f"a: {a}")
    #     print(f"midi_file: {midi_file}")
    #     a['href'] = f'assets/midi/prariefrontier/{midi_file}'

    return str(soup)

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

def download_midi_files(midi_urls, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for url in midi_urls:
        print(f"url: {url}")
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

class MidiPipeline:
    def process_item(self, item, spider):
        # print(f"item: {item}")
        html = item["html"]
        url = item["url"]

        # for midi_url in item["midi_urls"][:2]:
            # print(f"midi_url: {midi_url}")
        domain = getHostFromUrl(url)
        print(f"domain: {domain}")
        midi_urls = item["midi_urls"]
        midi_urls_with_domain = [domain+url for url in item["midi_urls"]]
        # midi_urls = midi_urls[:2] # test for now
        site_dir = 'prairiefrontier'
        download_midi_files(midi_urls_with_domain[:2], "../sites/assets/midi/prariefrontier")
            # yield scrapy.Request(midi_url, callback=self.parse_midi)

        # update html to point to midi files in assets/midi/prariefrontier
        new_html = update_html(item["html"], midi_urls[:2])
        # save html file to sites/prariefrontier/index.html

        # print(f"body: {body}")
        # need to save body to .html file
        # filename = url.split("/")[-1] + '.html'
        with open(f"../sites/{site_dir}/index.html", 'w') as f:
            f.write(new_html)

        return item
