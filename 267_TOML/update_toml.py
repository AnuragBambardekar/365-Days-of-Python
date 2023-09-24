import tomlkit

# opening in text mode
with open("267_TOML/editMe.toml", mode="rt", encoding="utf-8") as fp:
    config = tomlkit.load(fp)

print(config)
print(type(config))
print(config["user"]["player_o"]["color"])
print(config["user"]["player_o"]["color"].upper())

# can also access comments
print(config["user"]["ai_skill"].trivia.comment)

config.add("app_name", "Tic-Tac-Toe")

print("New Config: ",config)

config["user"]["ai_skill"] = 0.6 # change value of ai_skill

print("New Config: ", config)