import tomli_w

config = {
    "user": {
        "player_x": {"symbol": "X", "color": "blue", "ai": True},
        "player_o": {"symbol": "O", "color": "green", "ai": False},
        "ai_skill": 0.85,
    },
    "board_size": 3,
    "server": {"url": "https://tictactoe.example.com"},
}

print(tomli_w.dumps(config))

with open("267_TOML/tic_tac_toe_config_2.toml", mode="wb") as fp:
    tomli_w.dump(config, fp)