

def try_join():
    w = ['ab', 'c', 'dd', 'e']
    print(','.join(w))

import json

def x_json_load() -> dict[str, list[str]]:
    file_name = 'poland.json'

    d = json.load(open(file_name))

    # print(d)
    # print(type(d))
    return d


if __name__ == '__main__':
    d = x_json_load()
    print(sorted(list(d.keys())))
    s = set()
    for v in d.values():
        for m in v:
            s.add(m)
    print(sorted(list(s)))
