import json


def print_routes(routes: dict[str, list[str]]):
    """
    display route info in the format
        city1 -> city2,city3,city4
        city2 -> city4,city5
        city3 -> city1
    """
    # routes.

    for start in routes:
        print(f'{start} -> {",".join(routes[start])}')


def x_json_load() -> dict[str, list[str]]:
    file_name = 'poland.json'

    d = json.load(open(file_name))

    # print(d)
    # print(type(d))
    return d


if __name__ == '__main__':
    # Adjacency list representation of the map as a directed graph
    # routes: dict[str, list[str]] = {
    #     "Bielsko": ["Jaworzno", "Tychy"],
    #     "Jaworzno": ["Kraków"],
    #     "Tychy": ["Jaworzno"],
    #     "Kraków": ["Kielce"],
    #     "Kielce": []
    # }
    routes = x_json_load()
    print_routes(routes)
