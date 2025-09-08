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


def test_enter_door():
    door = Door()
    door.enter_airlock('Joe', origin='lobby')
    door.leave_airlock('Joe', destination='room')
    # teraz opuszczamy space (Mike musialby byc wczesniej w room)

    door.current_room_occupants.append('Mike')
    door.enter_airlock('Mike', origin='room')
    door.leave_airlock('Mike', destination='lobby')


# todo: write more tests....


if __name__ == '__main__':
    door = Door()
