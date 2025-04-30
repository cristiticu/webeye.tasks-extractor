from datetime import datetime

import settings


def get_divisible_frequencies(selected_datetime: datetime):
    minutes = selected_datetime.minute
    matching_intervals = [
        f"{frequency}m" for frequency in settings.AVAILABLE_FREQUENCIES if minutes % frequency == 0]

    return matching_intervals


def get_day_filters(selected_datetime: datetime):
    weekday = selected_datetime.weekday()

    if weekday < 5:
        return ["all", "weekdays"]
    else:
        return ["all", "weekend"]
