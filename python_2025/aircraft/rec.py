def traverse_mine(level: int) -> None:
    print(f'entering level= {level}')
    if level == -10:
        print('reached bottom')
        return
    traverse_mine(level - 1)
    print(f'exiting level= {level}')
    return


if __name__ == '__main__':
    traverse_mine(0)