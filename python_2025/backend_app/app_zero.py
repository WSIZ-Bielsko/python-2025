from random import randint

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from python_2025.backend_app.engine import solve
from python_2025.backend_app.ship_fight import shot

app = FastAPI()

# In-memory storage for users
users: dict[int, dict] = {}
user_id_counter = 1
moves: dict[int, str] = {}
state = {'board': '.' * 20}


class User(BaseModel):
    name: str
    email: str


class UserUpdate(BaseModel):
    name: str = None
    email: str = None


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}


@app.get("/add/{num1}/{num2}")
def add_numbers(num1: float, num2: float):
    return {"result": num1 + num2}


@app.get("/get_winner/{board}")
def solve(board: str):
    return {"result": solve(board)}


@app.get("/ships_reset")
def reset():
    n_board = ['.' for _ in range(20)]
    pos = randint(0, 18)
    n_board[pos] = 'o'
    n_board[pos + 1] = 'o'
    state['board'] = ''.join(n_board)
    return {"result": 'new board created'}


@app.get("/ships/shot/{position}")
def shotz(position: int):
    board = state['board']
    res, n_board = shot(board, position)
    state['board'] = n_board
    return {"result": res}


@app.get("/get_winner/{board}")
def solve(board: str):
    return {"result": solve(board)}


@app.get("/largest")
def add_numbers(numbers: str):
    nn = [int(n) for n in numbers.split(",")]
    return {"result": max(nn)}


def get_winner(move_dict: dict[int, str]) -> str:
    return 'draw'


@app.get("/RPS/{player}/{move}")
def add_numbers(player: int, move: str):
    if player not in [1, 2]:
        return {"error": "Player must be 1 or 2"}
    other = 1
    if player == 1:
        other = 2
    if other in moves:
        other_move = moves[other]
        moves[other] = move

        winner = get_winner(moves)
        moves.pop(other)
        moves.pop(player)
        return {"result": "somebody won"}
    else:
        moves[player] = move
    return {"result": f'thanks; now waiting for player {other}'}


@app.post("/users", status_code=201)
def create_user(user: User):
    global user_id_counter
    user_id = user_id_counter
    users[user_id] = user.model_dump()
    user_id_counter += 1
    return {"id": user_id, **users[user_id]}


@app.put("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    current_user = users[user_id]
    update_data = user_update.model_dump(exclude_unset=True)
    updated_user = {**current_user, **update_data}
    users[user_id] = updated_user
    return {"id": user_id, **updated_user}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **users[user_id]}


if __name__ == "__main__":
    uvicorn.run("app_zero:app", host="0.0.0.0", port=8000)
