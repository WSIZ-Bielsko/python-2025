def my_sqrt(x: float) -> float | None:
    if x >= 0:
        return x**0.5
    else:
        return None


if __name__ == '__main__':
    print(my_sqrt(1))
    print(my_sqrt(0.25))
    print(my_sqrt(0))
    print(my_sqrt(-4))


    z = my_sqrt(-2)
    if z is not None:
        print(f'rozwiazanie: {z}')
