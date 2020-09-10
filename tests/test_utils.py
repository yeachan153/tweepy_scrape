from twitter_scrape_fedex_case.utils.json_encoder import DateTimeEncoder
import datetime
import json


def test_datetime_encode_1():
    """Check encoding works"""
    test_dict = {"a": 2, "b": datetime.datetime.now()}
    encoded = DateTimeEncoder().encode(test_dict)
    assert isinstance(encoded, str)


def test_datetime_encode_2():
    """Check encoded date is the same"""
    test_dict = {"a": 2, "b": datetime.date(2020, 6, 14)}
    encoded = DateTimeEncoder().encode(test_dict)
    loaded = json.loads(encoded)
    decoded = datetime.datetime.fromisoformat(loaded["b"])
    assert test_dict["b"] == decoded.date()
