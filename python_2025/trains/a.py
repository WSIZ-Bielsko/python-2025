from datetime import datetime

if __name__ == '__main__':
    s = '21:55:00'
    s_as_time = datetime.strptime(s, '%H:%M:%S').time()
    print(s_as_time)
    print(type(s_as_time))

    now = datetime.now().time()
    print(now)
    print(type(now))
