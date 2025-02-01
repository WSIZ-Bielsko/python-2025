from datetime import time
from sys import thread_info

from python_2025.trains.importer import TrainInfo


def get_trains_from(city_prefix: str, all_trains: list[TrainInfo]) -> list[TrainInfo]:
    pass


def test_get_trains1():
    t1 = TrainInfo(id=1, train_name='a', train_number='01', source='Bielsko-Biała', destination='Warszawa', distance=250,
                   total_time_minutes=240, departure_time=time(12, 0, 0), arrival_time=time(15, 0, 0))
    t2 = TrainInfo(id=2, train_name='b', train_number='01', source='Wrocław', destination='Warszawa', distance=250,
                   total_time_minutes=240, departure_time=time(12, 0, 0), arrival_time=time(15, 0, 0))
    t3 = TrainInfo(id=3, train_name='c', train_number='01', source='Gdańsk', destination='Warszawa', distance=250,
                   total_time_minutes=240, departure_time=time(12, 0, 0), arrival_time=time(15, 0, 0))

    res = get_trains_from('Wro', [t1, t2, t3])
    print(res)
    assert res == [t2]


if __name__ == '__main__':
    pass
