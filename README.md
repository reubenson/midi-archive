# midi-archive

An archive of music on the web before the age of MP3s

## Web scraping tool for building the archive

- Each archived site to be hosted will preserve HTML, CSS, and MIDI
- MIDI files will be archived within the assets directory, and scoped by path to the site
    - e.g. /assets/midi/prairiefrontier/*
- CSS will similarly be archived within the assets directory
    - e.g. /assets/css/prairiefrontier/*
- HTML will be transformed to have CSS and MIDI links point to the self-hosted assets
    - e.g. sites/prairiefrontier/midi.html
    - TO DO: determine if `/sites` is the directory I want to serve static from
    - when restoring a site from Internet Archive, need to strip out IA's template
- JavaScript usage is generally pretty limited on these site, so just gonna ignore that
- The entirety of each site won't necessarily be scraped, since their source now exists on Internet Archive
- Replatformed sites will be faithful to their original look and feel
- Everything will serve static from github pages (for now anyway)

### Installation / Development
After setting up venv, install Scrapy
`python3 -m pip install Scrapy`

and 

`scrapy crawl prairiefrontier -s LOG_LEVEL=WARNING`

To create a new spider: `scrapy genspider example example.com`

## Miscellaneous Notes to Myself
- Ideally, each website in the archive would have its own subdomain, but for now just using paths off my primary personal domain
- probably makes sense to group assets by site, not under a midi dir
- need script to zip all MIDI files together
- safe to assume all midi filenames are unique on a given site? (probably holds ... generally)
- Scraper To Dos
    - Start by just grabbing the entire main HTML document
    - Download CSS files to assets
    - Munge HTML to point to self-hosted assets
        - And remove Internet Archive markup
        - Need to update links to other site pages
    - Download MIDI files and do the same as CSS
    - Also need to download any image assets
- Need to add appropriate head tags
- Consider building with 11ty framework, to help with local dev and CMS overhead for dealing with repeated elements and layouts
    - Each site could be distilled into components
        - HTML body
        - assets
        - title and keywords (and other metadata)
        - IA url
    - 11ty to provide common head, and other shared modules like blogring UI
    - 11ty to compose pages from scraped data