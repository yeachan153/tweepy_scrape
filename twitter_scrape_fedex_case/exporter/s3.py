from twitter_scrape_fedex_case.exporter.exporter import Exporter
from twitter_scrape_fedex_case.utils.json_encoder import DateTimeEncoder


class S3Exporter(Exporter):
    """Class to upload files
    to AWS
    """

    def __init__(self, s3, bucket: str):
        """Initializes uploader class. Needs to

        Args:
            s3_obj (boto3 s3 resource): boto3 s3 resource object, e.g. boto3.resource('s3')
            Should be authenticated. If you don't have aws configure, put your
            authentication in the boto3 object.
            bucket (str): Name of bucket in S3.
        """
        self.s3 = s3
        self.bucket = bucket
        self.json_encoder = DateTimeEncoder()

    def export_json(self, data: dict, key: str) -> None:
        """Uploads JSON to S3

        Args:
            data (dict): dictionary to upload as json
            key (str): s3 key, excluding bucket
        """
        s3object = self.s3.Object(self.bucket, key)
        s3object.put(Body=(bytes(self.json_encoder.encode(data).encode("UTF-8"))))
