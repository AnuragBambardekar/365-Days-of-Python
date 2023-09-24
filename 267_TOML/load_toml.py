import tomli
from pathlib import Path

with open("267_TOML/tic_tac_toe.toml", "rb") as fp:
    config = tomli.load(fp)

print(config)
print(config["user"]["player_o"])
print(config["server"]["url"])


toml_str = """
offset_date-time_utc = 2021-01-12 00:23:45Z
potpourri = ["flower", 1749, { symbol = "X", color = "blue" }, 1994-02-14]
"""

config2 = tomli.loads(toml_str)

print(config2)


config3 = tomli.loads(Path("267_TOML/tic_tac_toe.toml").read_text(encoding="utf-8"))
print(config3)