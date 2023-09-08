from configparser import ConfigParser

config = ConfigParser()

config["DEFAULT"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername":"Player"
}
config["Bamba"] = {
    "numberdigits": 10,
    "numbertries": 6,
    "playername":"Bamba"
}
config["SUDO"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername":"Cheater",
    "cheats": "on"
}

with open("253_Config_Parser/number_guessing.ini","w") as f:
    config.write(f)