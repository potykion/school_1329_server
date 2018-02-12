from datetime import datetime, time
from typing import Tuple, Dict, Union

from django.test.client import encode_multipart


def datetime_to_drf(datetime_: datetime) -> Union[str, datetime]:
    """
    Convert datetime to DRF format.
    :param datetime_: Datetime in UTC.
    :return: Datetime string in DRF-format.

    >>> datetime_to_drf(datetime(2017, 12, 18, 16, 00))
    '2017-12-18T16:00:00Z'
    """
    if datetime_:
        return f'{datetime_.date()}T{datetime_.time()}Z'
    else:
        return datetime_


def format_time(time_: time) -> str:
    """
    Convert time to string with hours and minutes.
    :param time_: Time.
    :return: String with hours and minutes.
    """
    return f'{time_.hour}:{time_.minute}'


def encode_data(data) -> Tuple[Dict, str]:
    """
    Encode data for PUT requests.
    :param data: Dict.
    :return: Encoded data and content type with boundary string.
    """
    boundary_string = 'BoUnDaRyStRiNg'
    encoded_data = encode_multipart(boundary_string, data)
    content_type = f'multipart/form-data; boundary={boundary_string}'
    return encoded_data, content_type
