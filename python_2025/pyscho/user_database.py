import json


def create_user(db: dict, username: str, password: str):
    """
    raise ValueError jeśli username zajęty w bazie
    :param db:
    :param username:
    :param password:
    :return:
    """
    pass


def login(db: dict, username: str, password: str) -> bool:
    """

    :param db:
    :param username:
    :param password:
    :return: True if username exists, and db[username] == password
    """
    pass


def update_password(db: dict, username: str, old_password: str, new_password: str):
    """
    Check if old password is correct (and username exists); if so -- update the password
    :param db:
    :param username:
    :param old_password:
    :param new_password:
    :return:
    """




def save_db(db, file_name):
    with open(file_name, 'w') as f:
        json.dump(db, f)


def load_db(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return dict()


if __name__ == '__main__':
    db = dict()
    # db = load_db('users.json')
    db['abra'] = 'kadabra'
    save_db(db, 'users.json')
