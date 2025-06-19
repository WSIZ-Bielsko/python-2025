from datetime import date
import calendar


def get_next_date(current_date: date, day_of_month: int) -> date:
    """
    Find next date >= current_date with day of month as specified by `day_of_month`.
    If `day_of_month` is positive, it should be such a day of this or next month, or the last
    day of that month if such a day doesn't exist.
    :param current_date: 
    :param day_of_month: 
    :return: 
    """
    year = current_date.year
    month = current_date.month
    day = current_date.day

    def last_day(y, m):
        return calendar.monthrange(y, m)[1]

    last_day_this_month = last_day(year, month)
    target_day_this_month = min(day_of_month, last_day_this_month)

    if day == target_day_this_month:
        return date(year, month, day)
    if day < target_day_this_month:
        return date(year, month, target_day_this_month)
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1

    last_day_next_month = last_day(year, month)
    target_day_next_month = min(day_of_month, last_day_next_month)
    return date(year, month, target_day_next_month)


def test_leap_year():
    # 29 in February (leap year)
    assert get_next_date(date(2024, 2, 27), 29) == date(2024, 2, 29)
    # 30 in February (leap year) should return last day of February
    assert get_next_date(date(2024, 2, 15), 30) == date(2024, 2, 29)
    # After 29th Feb in leap year, should roll to next month's 29 (March 29)
    assert get_next_date(date(2024, 2, 29), 29) == date(2024, 2, 29)
    # Requesting exact last day match
    assert get_next_date(date(2023, 2, 28), 28) == date(2023, 2, 28)

def test_end_of_year():
    # Looking for 31st in December on December 30
    assert get_next_date(date(2025, 12, 30), 31) == date(2025, 12, 31)
    # Looking for 1st in new year when today is December 31
    assert get_next_date(date(2025, 12, 31), 1) == date(2026, 1, 1)
    # Day larger than any in current month, on last day: Dec 31, 32 --> Dec 31
    assert get_next_date(date(2025, 12, 31), 32) == date(2025, 12, 31)
    # Looking for last day of year (31st Dec) from mid-year
    assert get_next_date(date(2025, 7, 9), 31) == date(2025, 7, 31)

def test_various_month_lengths():
    # April has only 30 days, looking for 31st
    assert get_next_date(date(2025, 4, 15), 31) == date(2025, 4, 30)
    # March has 31, looking for 31st, already past in April—should get May 31
    assert get_next_date(date(2025, 4, 30), 31) == date(2025, 4, 30)
    # Smallest possible day in month, from earlier day
    assert get_next_date(date(2025, 9, 10), 1) == date(2025, 10, 1)
    # Looking for 28th from February 1st, non-leap year
    assert get_next_date(date(2023, 2, 1), 28) == date(2023, 2, 28)


def test_simple():
    assert get_next_date(date(2025, 1, 1), 1) == date(2025, 1, 1)
    assert get_next_date(date(2025, 1, 10), day_of_month=1) == date(2025, 2, 1)
    assert get_next_date(date(2025, 1, 31), day_of_month=30) == date(2025, 2, 28)
    assert get_next_date(date(2025, 2, 28), day_of_month=31) == date(2025, 2, 28)
    assert get_next_date(date(2025, 3, 1), day_of_month=31) == date(2025, 3, 31)
    assert get_next_date(date(2025, 3, 31), day_of_month=30) == date(2025, 4, 30)