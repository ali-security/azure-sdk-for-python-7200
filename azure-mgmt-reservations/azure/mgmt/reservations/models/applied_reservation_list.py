# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.2.2.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AppliedReservationList(Model):
    """AppliedReservationList.

    :param value:
    :type value: list of str
    :param next_link: Url to get the next page of reservations
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[str]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, value=None, next_link=None):
        self.value = value
        self.next_link = next_link
