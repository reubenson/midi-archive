# midi-archive

An informal archive of music on the web before the age of MP3s. This is not intended to be comprehensive, but is instead an archive that exists alongside a companion [machine learning model](https://github.com/reubenson/midi-archive-lambda) that uses the archive as its corpus.

This repository implements [Scrapy](https://docs.scrapy.org/en/latest/) to collect MIDI files from websites before Y2K, and [Eleventy](https://www.11ty.dev/) as a static site generator for serving what is currently a very bare bones webpage.

### Workflow
The current process for updating the archive is a bit manual:
- Run the scraper tool, located in `/scraper`
- Run the script for tokenizing all the MIDI files, at `/scripts/apply_tokenizer.py`
- Zip up token json and upload to S3 with `/scripts/deploy_assets.sh`
- MIDI Archive assets are now ready to be ingested by ML model

### Installation / Development
- initialize venv `source /Users/reubenson/Projects/midi-archive/.venv/bin/activate`
- After setting up venv, install Scrapy
`python3 -m pip install Scrapy`
- `cd scraper` (need to be in the same directory as scrapy.cfg)
- run scraper with `scrapy crawl archive -s LOG_LEVEL=WARNING`
    - before running that command, update the target in the script

### Scraper
- The spider crawls pages, and then sends additional requests for assets like MIDI files
    - These requests get passed through response middleware, where the response payload is then saved to disk in the assets directory
- Each page is also saved to disk, which is handled in a Pipeline
    - Before getting saved to disk, the HTML needs to be updated, such that references to the assets (MIDI, CSS, images) are updated to point to the self-hosted paths
        - In order to do this, the spider will keep track of every successful request and provide the asset path transformations needed to update HTML in the Pipeline
    - HTML will be saved in a .md file with some additional heading data
- Each page the spider crawls will result in a markdown file, which will then be processed by 11ty to result in HTML pages served via the _sites directory
    - Currently, the site is hosted on GitHub Pages, and will point to the docs directory to serve all static pages and assets

### Deploying assets
`cd scripts`
`./deploy_assets.sh`

### References
- [Scrapy architecture](https://docs.scrapy.org/en/latest/topics/architecture.html)

### Remaining Tasks
- Serve MIDI assets via S3 instead of GitHub, depending on anticipated site traffic