from dataclasses import dataclass
from datetime import time, datetime


@dataclass
class TrainInfo:
    # pola....
    id: int
    train_name: str
    train_number: str
    source: str
    destination: str
    distance: int
    total_time_minutes: int
    departure_time: time
    arrival_time: time


def convert_duration_info_to_minutes(day_info: str) -> int:
    """
    Example input:
    '1 days 05:10:00'
    '0 days 11:45:00'
    :param day_info:
    :return:
    """
    day_info = day_info.replace('days', ':')
    data = day_info.split(":")
    days = int(data[0])
    hours = int(data[1])
    minutes = int(data[2])
    return (days * 24 + hours) * 60 + minutes


def convert_line_to_traininfo(ln: str) -> TrainInfo:
    data = ln.split(',')

    #  datetime.strptime(s, '%H:%M:%S').time()
    id = int(data[0])
    train_name = data[1]
    train_number = data[2]
    source = data[3]
    destination = data[4]
    distance = int(data[5])
    total_time_minutes = convert_duration_info_to_minutes(data[6])
    departure_time = datetime.strptime(data[7], '%H:%M:%S').time()
    arrival_time = datetime.strptime(data[7], '%H:%M:%S').time()
    return TrainInfo(id, train_name, train_number, source, destination, distance, total_time_minutes,
                     departure_time, arrival_time)


def load_file(file_name: str) -> list[TrainInfo]:
    res = []
    with open('small.csv', 'r') as f:
        lines = f.readlines()
        for ln in lines[1:]:
            res.append(convert_line_to_traininfo(ln))
    return res


if __name__ == '__main__':
    # info1 = TrainInfo(train_name='kadabra')
    # print(info1)

    # mins = convert_duration_info_to_minutes('12 days    05:10:00')
    # mins = convert_duration_info_to_minutes('1 days    00:00:00')
    # print(mins)

    x = load_file('small.csv')
    x.sort(key=lambda x: x.total_time_minutes)

    for ti in x:
        if ti.source.startswith('MUM'):
            print(ti)
