# midi-archive

An archive of music on the web before the age of MP3s. This is not intended to be an extensive collection, but is instead an archive that exists alongside a [machine learning model](https://github.com/reubenson/midi-archive-lambda) that uses the archive as its corpus.

## Workflow
The current process for updating the archive is a bit manual:
- Run the scraper tool, located in `/scraper`
- Run the script for tokenizing all the MIDI files, at `/scripts/apply_tokenizer.py`
- Zip up token json and upload to S3 with `/scripts/deploy_assets.sh`
- MIDI Archive assets are now ready to be ingested by ML model

## Repository Directory Structure
- I want to store MIDI data in the repo, but keep the filesize of the repo from ballooning too much, so there should be no repetition. 
- I want to store HTML data in the repo as well. And images too?

## Web scraping tool for building the archive

- Each archived site to be hosted will preserve HTML, CSS, and MIDI
- MIDI files will be archived within the assets directory, and scoped by path to the site
    - e.g. /assets/midi/prairiefrontier/*
- CSS will similarly be archived within the assets directory
    - e.g. /assets/css/prairiefrontier/*
- HTML will be transformed to have CSS and MIDI links point to the self-hosted assets
    - e.g. sites/prairiefrontier/midi.html
    - when restoring a site from Internet Archive, need to strip out IA's template
- JavaScript usage is generally pretty limited on these site, so just gonna ignore that
- The entirety of each site won't necessarily be scraped, since their source now exists on Internet Archive
- Replatformed sites will be faithful to their original look and feel
- Everything will serve static from github pages (for now anyway)

### Architecture / Flow
- The spider crawls pages, and then sends additional requests for assets like MIDI files
    - These requests get passed through response middleware, where the response payload is then saved to disk in the assets directory
- Each page is also saved to disk, which is handled in a Pipeline
    - Before getting saved to disk, the HTML needs to be updated, such that references to the assets (MIDI, CSS, images) are updated to point to the self-hosted paths
        - In order to do this, the spider will keep track of every successful request and provide the asset path transformations needed to update HTML in the Pipeline
    - HTML will be saved in a .md file with some additional heading data
- Each page the spider crawls will result in a markdown file, which will then be processed by 11ty to result in HTML pages served via the _sites directory
    - Currently, the site is hosted on GitHub Pages, and will point to the _sites directory to serve all static pages and assets



### Installation / Development
- initialize venv `source /Users/reubenson/Projects/midi-archive/.venv/bin/activate`
- After setting up venv, install Scrapy
`python3 -m pip install Scrapy`
- `cd scraper` (need to be in the same directory as scrapy.cfg)
- run scraper with `scrapy crawl archive -s LOG_LEVEL=WARNING`
    - before running that command, update the target in the script

### Lambda
- [Reference for setting up Websockets API in AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-chat-app.html#websocket-api-chat-app-create-api)

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

- should have read architecture docs for Scrapy first https://docs.scrapy.org/en/latest/topics/architecture.html
- Tipping point somewhere around how much I want to host via GitHub, vs pushing assets up to S3

## S3 Directory Structure
- assets
- assets/midi
- assets/tokens

## Deploying assets
`cd scripts`
`./deploy_assets.sh`

## Requirements
- Each MIDI file should be traceable back to the website it came from
- Each MIDI file should hold onto its title and its original filename
    - Difficult to normalize this at scale, esp with how variable sites are
- Metadata during scraping to be saved as .csv?
- Images and HTML also to be saved, for potential future use