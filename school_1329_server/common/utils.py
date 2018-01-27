from datetime import datetime


def datetime_to_drf(datetime_: datetime):
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
        datetime_
