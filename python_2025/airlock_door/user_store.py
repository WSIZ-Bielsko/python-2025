from dataclasses import dataclass


# klasa
@dataclass
class User:
    # pola
    name: str
    pin: int

    # metody
    def check_pin(self, pin: int) -> bool:
        print('checking pin...')
        return self.pin == pin


if __name__ == '__main__':
    print('ok')

    # tworzenie instancji
    u1 = User('john', 1122)
    u2 = User('alice', 3333)
    u3 = User('bob', 4455)
    u4 = User('emma', 6677)
    u5 = User('sarah', 8899)
    u6 = User('mike', 1234)
    u7 = User('lisa', 5678)
    u8 = User('tom', 9012)

    users = [u1, u2, u3, u4, u5, u6, u7, u8]

    # print(u1)
    # print(u2)
    #
    # print(u1.name)
    # print(u1.pin)
    #
    # print(u2.name)
    # print(u2.pin)
    # print(u1.check_pin(1122))
    # print(u1.check_pin(1132))

    while True:
        name = input('Enter your name: ')
        pin = int(input('Enter your PIN: '))
        # przeszukać listę "users" poszukując usera o podanym `name`;
        # jeśli znajdziemy takiego, to sprawdzić PIN,
        # jeśli jest poprawny, to witamy go, i wychodzimy z pętli
        # jeśli nie, to wypisujemy komunikat (albo o niepoprawnym PIN, albo o braku usera, odpowiednio)

        x = User(name, pin)
        if x in users:
            print(f'Welcome {x.name}!')
            break


        # correct = False
        # for u in users:
        #     if u.name == name and u.check_pin(pin):
        #         print(f'Welcome {u.name}!')
        #         correct = True
        #         break
        # if correct:
        #     break
