from dataclasses import dataclass


@dataclass
class TrainInfo:
    # pola....
    id: int
    train_name: str
    train_number: str


def convert_line_to_traininfo(ln: str) -> TrainInfo:
    data = ln.split(',')
    return TrainInfo(id=int(data[0]), train_name=data[1], train_number=data[2])


if __name__ == '__main__':
    with open('small.csv', 'r') as f:
        lines = f.readlines()
        for ln in lines[1:]:
            print(ln.strip())
            print(convert_line_to_traininfo(ln))

    # info1 = TrainInfo(train_name='kadabra')
    # print(info1)

