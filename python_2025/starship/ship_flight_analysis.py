from dataclasses import dataclass

from matplotlib import pyplot as plt


def convert_to_numbers(line: str) -> tuple[int, int, int]:
    x = line.split(',')
    return int(x[0]), int(x[1]), int(x[2])


@dataclass
class Telemetry:
    # ↓↓ pola
    time: float
    alt: float
    velocity: float


@dataclass
class FullTelemetry:
    time: float
    alt: float
    velocity: float
    vertical_velocity: float
    horizontal_velocity: float
    acceleration: float
    pitch_angle: float


def compute_full_telemetry(basic_data: list[Telemetry]) -> list[FullTelemetry]:
    result = []
    for i in range(1, len(basic_data)):
        current = basic_data[i]
        previous = basic_data[i - 1]
        vertical_velocity_kmh = (current.alt - previous.alt) * 3600 / (current.time - previous.time)
        horizontal_velocity = (current.velocity ** 2 - vertical_velocity_kmh ** 2) ** 0.5
        acceleration = (current.velocity - previous.velocity) * 1000 / 3600 / (current.time - previous.time)

        pitch = 0
        full = FullTelemetry(current.time, current.alt, current.velocity, vertical_velocity_kmh,
                             horizontal_velocity, acceleration, pitch)
        result.append(full)

    return result


def plot_acceleration(data: list[FullTelemetry]) -> None:
    times = []
    accelerations = []
    for d in data:
        times.append(d.time)
        accelerations.append(d.acceleration)

    plt.plot(times, accelerations)
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (m/s)')
    plt.title('Acceleration of starship on IFT 7')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':

    flight_data: list[Telemetry] = []

    with open('ship_data.csv', 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            # print(f'[{line.strip()}]')
            print(convert_to_numbers(line))
            nums = convert_to_numbers(line)

            flight_data.append(Telemetry(velocity=nums[0], alt=nums[1], time=nums[2]))

    # ↓↓ to są instancje klasy Telemetry
    t1 = Telemetry(time=5, alt=30, velocity=112)
    t2 = Telemetry(time=10, alt=35, velocity=120)
    print(t1)
    print(t2)
    print(t1.velocity)
    print(t2.velocity)
    t2.velocity += 10

    full = compute_full_telemetry(flight_data)
    for d in full:
        print(d)

    plot_acceleration(full)
