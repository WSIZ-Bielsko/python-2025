from pydantic import BaseModel


class Figure(BaseModel):
    side: int
    height: int


class AircraftPart(BaseModel):
    id: int
    name: str
    # constraints
    flights_since_overhaul: int
    hours_since_overhaul: int

    # max values
    max_flights: int
    max_hours: int

    # subparts
    subparts: list[int]





if __name__ == '__main__':
    f1 = Figure(side=10, height=2)  # instancja klasy

    print(f1.height, f1.side)
    print(f1)

    f2 = Figure(side=8, height=22)
    print(f2)
