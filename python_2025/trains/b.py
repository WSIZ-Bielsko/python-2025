if __name__ == '__main__':
    s = '1 days 05:10:00'
    s = s.replace('days',':')
    print(s)
    print(s.split(':'))