from abc import ABC
from abc import abstractmethod


class Exporter(ABC):
    """Abstract implementation of exporter
    class
    """

    @abstractmethod
    def export_json(self):
        """Exports dictionary as JSONs"""
        raise NotImplementedError()
