# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.path_item import PathItem
from swagger_server.models.station import Station
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Path(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, departure_station: Station=None, departure_time: str=None, arrival_station: Station=None, arrival_time: str=None, travel_time: str=None, path_items: List[PathItem]=None):
        """
        Path - a model defined in Swagger

        :param departure_station: The departure_station of this Path.
        :type departure_station: Station
        :param departure_time: The departure_time of this Path.
        :type departure_time: str
        :param arrival_station: The arrival_station of this Path.
        :type arrival_station: Station
        :param arrival_time: The arrival_time of this Path.
        :type arrival_time: str
        :param travel_time: The travel_time of this Path.
        :type travel_time: str
        :param path_items: The path_items of this Path.
        :type path_items: List[PathItem]
        """
        self.swagger_types = {
            'departure_station': Station,
            'departure_time': str,
            'arrival_station': Station,
            'arrival_time': str,
            'travel_time': str,
            'path_items': List[PathItem]
        }

        self.attribute_map = {
            'departure_station': 'departure_station',
            'departure_time': 'departure_time',
            'arrival_station': 'arrival_station',
            'arrival_time': 'arrival_time',
            'travel_time': 'travel_time',
            'path_items': 'path_items'
        }

        self._departure_station = departure_station
        self._departure_time = departure_time
        self._arrival_station = arrival_station
        self._arrival_time = arrival_time
        self._travel_time = travel_time
        self._path_items = path_items

    @classmethod
    def from_dict(cls, dikt) -> 'Path':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Path of this Path.
        :rtype: Path
        """
        return deserialize_model(dikt, cls)

    @property
    def departure_station(self) -> Station:
        """
        Gets the departure_station of this Path.

        :return: The departure_station of this Path.
        :rtype: Station
        """
        return self._departure_station

    @departure_station.setter
    def departure_station(self, departure_station: Station):
        """
        Sets the departure_station of this Path.

        :param departure_station: The departure_station of this Path.
        :type departure_station: Station
        """

        self._departure_station = departure_station

    @property
    def departure_time(self) -> str:
        """
        Gets the departure_time of this Path.

        :return: The departure_time of this Path.
        :rtype: str
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time: str):
        """
        Sets the departure_time of this Path.

        :param departure_time: The departure_time of this Path.
        :type departure_time: str
        """

        self._departure_time = departure_time

    @property
    def arrival_station(self) -> Station:
        """
        Gets the arrival_station of this Path.

        :return: The arrival_station of this Path.
        :rtype: Station
        """
        return self._arrival_station

    @arrival_station.setter
    def arrival_station(self, arrival_station: Station):
        """
        Sets the arrival_station of this Path.

        :param arrival_station: The arrival_station of this Path.
        :type arrival_station: Station
        """

        self._arrival_station = arrival_station

    @property
    def arrival_time(self) -> str:
        """
        Gets the arrival_time of this Path.

        :return: The arrival_time of this Path.
        :rtype: str
        """
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, arrival_time: str):
        """
        Sets the arrival_time of this Path.

        :param arrival_time: The arrival_time of this Path.
        :type arrival_time: str
        """

        self._arrival_time = arrival_time

    @property
    def travel_time(self) -> str:
        """
        Gets the travel_time of this Path.

        :return: The travel_time of this Path.
        :rtype: str
        """
        return self._travel_time

    @travel_time.setter
    def travel_time(self, travel_time: str):
        """
        Sets the travel_time of this Path.

        :param travel_time: The travel_time of this Path.
        :type travel_time: str
        """

        self._travel_time = travel_time

    @property
    def path_items(self) -> List[PathItem]:
        """
        Gets the path_items of this Path.

        :return: The path_items of this Path.
        :rtype: List[PathItem]
        """
        return self._path_items

    @path_items.setter
    def path_items(self, path_items: List[PathItem]):
        """
        Sets the path_items of this Path.

        :param path_items: The path_items of this Path.
        :type path_items: List[PathItem]
        """

        self._path_items = path_items

