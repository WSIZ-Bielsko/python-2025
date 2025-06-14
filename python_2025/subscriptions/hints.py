from datetime import date
from calendar import monthrange

if __name__ == '__main__':
    d = date(2025, 2, 15)
    print(d.day)  # 15
    print(d.month)  # 2

    print(monthrange(2025, 2))  # (5,28); [1] gives max number of days in month
    print(monthrange(2024, 2))  # (3,29); leap year
