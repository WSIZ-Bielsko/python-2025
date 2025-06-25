from loguru import logger


class DoorError(RuntimeError):
    pass


class Door:

    def __init__(self):
        self.air_lock_occupant: str = '(empty)'
        self.current_room_occupants: list[str] = []
        # design: only one person can be in the airlock at a time

    def enter_airlock(self, occupant: str, origin: str):
        logger.info(f'{occupant} attempts to the airlock from: {origin}')

        if origin == 'room':
            # a person enters the airlock from the room
            if occupant not in self.current_room_occupants:
                raise DoorError(f'{occupant} is not in the room -- cannot enter the airlock')
            if self.air_lock_occupant != '(empty)':
                raise DoorError(f'Airlock is occupied')

            self.current_room_occupants.remove(occupant)
            self.air_lock_occupant = occupant

            logger.info(f'{occupant} entered the airlock')
        elif origin == 'lobby':
            # a person enters the airlock from the room
            if occupant in self.current_room_occupants:
                raise DoorError(f'{occupant} is in the room -- cannot reenter the airlock')
            if self.air_lock_occupant != '(empty)':
                raise DoorError(f'Airlock is occupied')

            self.air_lock_occupant = occupant
        else:
            raise DoorError(f'Invalid direction: {origin}')
        logger.info(f'{occupant} entered the airlock')

    def leave_airlock(self, occupant, destination: str):
        logger.info(f'{occupant} attempts to leave the airlock in the direction: {destination}')
        # todo: implement
        if self.air_lock_occupant != occupant:
            raise DoorError(f'Airlock occupied by {self.air_lock_occupant}, not {occupant}')
        if self.air_lock_occupant == '(empty)':
            raise DoorError(f'Airlock is not occupied')

        if destination=='room':
            # a person leaves the airlock to the room
            if occupant in self.current_room_occupants:
                raise DoorError(f'{occupant} already in room')

            self.air_lock_occupant = '(empty)'
            self.current_room_occupants.append(occupant)
        elif destination=='lobby':
            # a person leaves the airlock to the lobby
            self.air_lock_occupant = '(empty)'
        else:
            raise DoorError(f'Invalid destination: {destination}')
        logger.info(f'{occupant} left the airlock')


def test_enter_door():
    door = Door()
    door.enter_airlock('Joe', origin='lobby')
    door.leave_airlock('Joe', destination='room')
    # teraz opuszczamy space (Mike musialby byc wczesniej w room)

    door.current_room_occupants.append('Mike')
    door.enter_airlock('Mike', origin='room')
    door.leave_airlock('Mike', destination='lobby')


# todo: write more tests....
def test_enter_airlock_from_room_success():
    door = Door()
    door.current_room_occupants = ['Alice', 'Bob']
    door.enter_airlock('Alice', 'room')
    assert door.air_lock_occupant == 'Alice'
    assert 'Alice' not in door.current_room_occupants

def test_enter_airlock_from_room_fail_not_in_room():
    door = Door()
    door.current_room_occupants = ['Bob']
    try:
        door.enter_airlock('Alice', 'room')
        assert False, "DoorError not raised"
    except DoorError:
        pass

def test_enter_airlock_from_lobby_success():
    door = Door()
    door.current_room_occupants = ['Bob']
    door.enter_airlock('Charlie', 'lobby')
    assert door.air_lock_occupant == 'Charlie'

def test_enter_airlock_from_lobby_fail_already_in_room():
    door = Door()
    door.current_room_occupants = ['Alice']
    try:
        door.enter_airlock('Alice', 'lobby')
        assert False, "DoorError not raised"
    except DoorError:
        pass

def test_leave_airlock_to_room_success():
    door = Door()
    door.current_room_occupants = ['Bob']
    door.air_lock_occupant = 'Alice'
    door.leave_airlock('Alice', 'room')
    assert door.air_lock_occupant == '(empty)'
    assert 'Alice' in door.current_room_occupants

def test_leave_airlock_to_room_fail_already_in_room():
    door = Door()
    door.current_room_occupants = ['Alice']
    door.air_lock_occupant = 'Alice'
    try:
        door.leave_airlock('Alice', 'room')
        assert False, "DoorError not raised"
    except DoorError:
        pass

def test_leave_airlock_to_lobby_success():
    door = Door()
    door.air_lock_occupant = 'Alice'
    door.leave_airlock('Alice', 'lobby')
    assert door.air_lock_occupant == '(empty)'

def test_leave_airlock_fail_airlock_empty():
    door = Door()
    try:
        door.leave_airlock('Alice', 'room')
        assert False, "DoorError not raised"
    except DoorError:
        pass

def test_leave_airlock_fail_wrong_occupant():
    door = Door()
    door.air_lock_occupant = 'Bob'
    try:
        door.leave_airlock('Alice', 'room')
        assert False, "DoorError not raised"
    except DoorError:
        pass

def test_leave_airlock_fail_invalid_destination():
    door = Door()
    door.air_lock_occupant = 'Alice'
    try:
        door.leave_airlock('Alice', 'garage')
        assert False, "DoorError not raised"
    except DoorError:
        pass

if __name__ == '__main__':
    door = Door()
