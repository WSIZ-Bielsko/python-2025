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


def test_get_trains_case_insensitive():
    t1 = TrainInfo(id=1, train_name='IC', train_number='3101', source='Wrocław', destination='Kraków',
                   distance=270, total_time_minutes=180, departure_time=time(8, 0, 0), arrival_time=time(11, 0, 0))
    t2 = TrainInfo(id=2, train_name='TLK', train_number='3102', source='Warszawa', destination='Gdańsk',
                   distance=350, total_time_minutes=240, departure_time=time(9, 0, 0), arrival_time=time(13, 0, 0))
    assert get_trains_from('wro', [t1, t2]) == [t1]


def test_get_trains_multiple_matches():
    t1 = TrainInfo(id=1, train_name='IC', train_number='3101', source='Wrocław', destination='Kraków',
                   distance=270, total_time_minutes=180, departure_time=time(8, 0, 0), arrival_time=time(11, 0, 0))
    t2 = TrainInfo(id=2, train_name='TLK', train_number='3102', source='Wronki', destination='Poznań',
                   distance=150, total_time_minutes=120, departure_time=time(10, 0, 0), arrival_time=time(12, 0, 0))
    t3 = TrainInfo(id=3, train_name='IC', train_number='3103', source='Warszawa', destination='Gdańsk',
                   distance=350, total_time_minutes=240, departure_time=time(9, 0, 0), arrival_time=time(13, 0, 0))
    result = get_trains_from('Wro', [t1, t2, t3])
    assert len(result) == 2
    assert t1 in result and t2 in result


def test_get_trains_empty_input():
    t1 = TrainInfo(id=1, train_name='IC', train_number='3101', source='Wrocław', destination='Kraków',
                   distance=270, total_time_minutes=180, departure_time=time(8, 0, 0), arrival_time=time(11, 0, 0))
    assert get_trains_from('', [t1]) == []


def test_get_trains_special_characters():
    t1 = TrainInfo(id=1, train_name='IC', train_number='3101', source='Łódź', destination='Kraków',
                   distance=220, total_time_minutes=160, departure_time=time(8, 0, 0), arrival_time=time(10, 40, 0))
    t2 = TrainInfo(id=2, train_name='TLK', train_number='3102', source='Kraków', destination='Warszawa',
                   distance=300, total_time_minutes=200, departure_time=time(12, 0, 0), arrival_time=time(15, 20, 0))
    assert get_trains_from('Łó', [t1, t2]) == [t1]


def test_get_trains_no_matches():
    t1 = TrainInfo(id=1, train_name='IC', train_number='3101', source='Wrocław', destination='Kraków',
                   distance=270, total_time_minutes=180, departure_time=time(8, 0, 0), arrival_time=time(11, 0, 0))
    t2 = TrainInfo(id=2, train_name='TLK', train_number='3102', source='Warszawa', destination='Gdańsk',
                   distance=350, total_time_minutes=240, departure_time=time(9, 0, 0), arrival_time=time(13, 0, 0))
    assert get_trains_from('xyz', [t1, t2]) == []


if __name__ == '__main__':
    test_get_trains1()
