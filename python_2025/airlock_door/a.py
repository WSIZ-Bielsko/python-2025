from dataclasses import dataclass


# klasa
@dataclass
class User:
    # pola
    name: str
    pin: int

    # metody
    def check_pin(self, pin: int) -> bool:
        return self.pin == pin


if __name__ == '__main__':
    print('ok')

    # tworzenie instancji
    u1 = User('john', 1122)

    u2 = User('alice', 3333)

    print(u1)
    print(u2)

    print(u1.name)
    print(u1.pin)

    print(u2.name)
    print(u2.pin)
    print(u1.check_pin(1122))
    print(u1.check_pin(1132))

    while True:
        name = input('Enter your name: ')
        pin = int(input('Enter your PIN: '))
