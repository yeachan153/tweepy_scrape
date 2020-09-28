# Overview

This repo takes the [twitter-scraper](https://github.com/bisguzar/twitter-scraper) and adds some additional exporting functionality. At the moment the only export that is supported to AWS S3.

## Installation

### Dependencies
1. Poetry - To install, you should have poetry installed. Follow the guide [here](https://python-poetry.org/docs/#installation).
2. Python 3.7+ - You can use pyenv to install on 3.7+
3. Pip `>=20.0.0`.
4. Create S3 bucket: ```aws s3api create-bucket --bucket fedex-case --region eu-central-1 --create-bucket-configuration LocationConstraint=eu-central-1```

### Process
After that, clone this repository and install it:
```
git clone https://github.com/yeachan153/twitter_scrape_export.git
cd twitter_scrape_export
poetry install
```

## Use Case
At the moment, I simulate a twitter stream by writing to S3.

```
from twitter_scrape_fedex_case.tweets.get_tweets import TweetPipeline
from twitter_scrape_fedex_case.exporter.s3 import S3Exporter
import boto3


bucket = "fedex-case"  # Name of bucket to write to
s3 = boto3.resource("s3")  # Auth handled here

exporter = S3Exporter(s3=s3, bucket=bucket)
pipeline = TweetPipeline(exporter)

pipeline.execute(query='#amsterdam', pages=2)  # Scrape 2 pages of this hashtag.
```
