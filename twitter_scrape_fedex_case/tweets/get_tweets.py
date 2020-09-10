from twitter_scraper import get_tweets
from twitter_scrape_fedex_case.user.user_data import get_user_data
from twitter_scrape_fedex_case.exporter.exporter import Exporter
from datetime import datetime


class TweetPipeline:
    """Class to scrape twitter posts
    and export them.
    """

    YM = datetime.now().strftime("%Y%m")

    def __init__(self, export_pipeline: Exporter):
        """Initialises class and sets
        the export pipeline. Currently only
        S3Exporter is supported

        Args:
            export_pipeline (Exporter): instance of exporter pipeline
            to be used.
        """
        self.export_pipeline = export_pipeline

    def execute(self, query: str, pages: int):
        """
        Fetches tweets and exports them through
        export pipeline.

        Args:
            query (str): the tweet or hashtag you want to scrape
            pages (int): the number of pages you want in terms
            of responses
        """
        tweets = get_tweets(query=query, pages=pages)
        for tweet in tweets:
            username = tweet["username"]
            tweet_id = tweet["tweetId"]
            user_data = get_user_data(username)
            full_data = {**tweet, **user_data}
            self.export_pipeline.export_json(full_data, f"{self.YM}/{tweet_id}.json")
