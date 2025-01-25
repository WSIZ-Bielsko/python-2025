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

    days = int(time[0])
    stripped: str = time.lstrip(str(days) + " days ")
    data = stripped.split(":")
    hours = int(data[0])
    minutes = int(data[1])
    seconds = int(data[2])


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


if __name__ == '__main__':
    with open('small.csv', 'r') as f:
        lines = f.readlines()
        for ln in lines[1:]:
            print(ln.strip())
            print(convert_line_to_traininfo(ln))

    # info1 = TrainInfo(train_name='kadabra')
    # print(info1)
