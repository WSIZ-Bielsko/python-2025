import random
import string

from fastapi import FastAPI, HTTPException

from python_2025.prisoners_dilemma.game import Game

app = FastAPI(title="Prisonners dilemma API", description="API for prisonners dilemma game.")

# Global door instance
games: dict[str, Game] = {}
payoff = {'DD': (0, 0), 'CD': (0, 3), 'DC': (3, 0), 'CC': (2, 2)}


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {"message": "Prisonner's dilemma API", "version": "1.0.0"}


@app.get("/status")
async def get_door_status():
    return {'status': 'ok'}


@app.post("/game/move")
async def make_move(game_id: str, player: int, move: str) -> dict:
    if move not in ['C', 'D']:
        raise HTTPException(status_code=400, detail="Invalid move (must be C or D)")
    if player not in [1, 2]:
        raise HTTPException(status_code=400, detail="Invalid player (must be 1 or 2)")
    if not game_id:
        game_id = random.sample(string.ascii_letters, k=4)
    if game_id not in games:
        games[game_id] = Game(payoff=payoff)

    g = games[game_id]
    g.post_move(move, player)
    return {
        "game_id": game_id,
        "player": player,
        "move": move,
        "history": g.history,
        "scores": g.score,
        "status": "move received"
    }


@app.post("/game/status")
async def get_game_status(game_id: str) -> dict:
    if not game_id:
        return {'result': 'error: please provide game_id'}
    g = games[game_id]
    return {
        "game_id": game_id,
        "scores": g.score,
        "history": g.history,
        "turns:": len(g.history)
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5002)
