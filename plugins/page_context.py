#coding:utf-8

import re
from math import floor


def preBuildPage(page, context, data):
    """
    Updates the context of the page to include: the page itself
    as {{ CURRENT_PAGE }}
    """

    extra = {
        "CURRENT_PAGE": page,
        "READ_TIME": read_time(data)
    }

    context.update(extra)
    return context, data


def read_time(data):
    stripped_data = re.sub('<[^<]+?>', '', data)
    time = len(re.findall("(\S+)", stripped_data)) / 275.0

    time += len(re.findall('(<img)', data)) * 0.2

    hours_part = int(floor(time / 60))
    minutes_part = int(floor(time % 60))
    seconds_part = int(floor(time * 60 % 60))

    read_str = 'Read time: {m} minutes {s} seconds'

    if hours_part is not 0:
        read_str = 'Read time: {h} hours {m} minutes {s} seconds'
        return read_str.format(h=hours_part, m=minutes_part, s=seconds_part)

    return read_str.format(m=minutes_part, s=seconds_part)
