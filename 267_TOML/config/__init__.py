# __init__.py

import pathlib
import tomli

path = pathlib.Path(__file__).parent / "tic_tac_toe.toml"
with path.open(mode="rb") as fp:
    tic_tac_toe = tomli.load(fp)