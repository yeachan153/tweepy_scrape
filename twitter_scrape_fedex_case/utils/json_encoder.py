from json import JSONEncoder
import datetime


class DateTimeEncoder(JSONEncoder):
    """Automatically encode dates when JSON
    encoding to YYYY-MM-DDTHH:MM:SS.
    """

    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
