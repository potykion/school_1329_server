from datetime import timedelta, time, datetime

LESSON_DURATION = 45


def compute_end_time(start_time: time) -> time:
    """
    Add lesson duration to start time.
    :param start_time: Start time.
    :return: End time.

    >>> compute_end_time(time(10, 30))
    datetime.time(11, 15)
    """
    start_datetime = datetime.combine(datetime.today(), start_time)
    end_datetime = start_datetime + timedelta(minutes=LESSON_DURATION)
    return end_datetime.time()
