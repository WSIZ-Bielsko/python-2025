class DoorError(RuntimeError):
    pass


class Door:

    def __init__(self):
        self.air_lock_occupant: str = None
        self.current_occupants: list[str] = []
        # design: only one person can be in the airlock at a time

    def enter(self, occupant: str, direction: str):
        # direction: 'in' or 'out'

        # 1) if sb. in airlock --> raise DoorError
        # raise DoorError('person already in airlock')
        # 2) cannot enter if already in current occupants

        print(f'{occupant} entered the airlock')

    def leave(self, occupant, direction: str):
        # direction: 'in' or 'out'
        # 1) cant levae if not in airlock
        print(f'{occupant} left the airlock')


def test_enter_door():
    door = Door()
    door.enter('Joe', 'in')
    door.leave('Joe', 'in')
    # teraz opuszczamy space
    door.enter('Mike', 'out')
    door.leave('Mike', 'out')

# todo: write more tests....


if __name__ == '__main__':
    door = Door()
    door.enter('Joe')
    door.enter('Joe')
    door.enter('Mike')
    door.leave('Mike')
    door.enter('Sarah')
