# import tomlkit
# toml_data = """
# [nested]  # Not necessary
#     [nested.table]
#     string       = "Hello, TOML!"
#     weird_string = '''Literal
#         Multiline'''
# """

# print(tomlkit.dumps(tomlkit.loads(toml_data)))
# print(tomlkit.dumps(tomlkit.loads(toml_data)) == toml_data)

from tomlkit import comment, document, nl, table

toml = document()
toml.add(comment("Written by TOML kit"))
toml.add(nl())
toml.add("board_size",3)

# print(toml.as_string())

player_x = table()
player_x.add("symbol", "X")
player_x.add("color", "blue")
player_x.comment("Start player")
toml.add("player_x", player_x)

player_o = table()
player_o.update({"symbol": "O", "color": "green"})
toml["player_o"] = player_o

print(toml.as_string())