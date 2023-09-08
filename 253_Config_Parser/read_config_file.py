from configparser import ConfigParser, ExtendedInterpolation

config = ConfigParser(
    interpolation=ExtendedInterpolation()
) # allow to read values which reference other values

try:
    config.read("253_Config_Parser/config.ini")
except:
    print("Format Error!")
    raise SystemExit()

print(config["Log"]["log_filename"])
print(config["Database"]["server"])

if "username" in config["Database"]:
    print("Username exists!")

print(config.get("Database","password"))

print(config.sections())

print(config.options("Database"))

# print(type(config["Database"]["port"]))

# port = int(config["Database"]["port"])
# print(port, type(port))

port = config.getint("Database","port",fallback=7) # if port is not defined then use fallback
print(port, type(port))

if (config.getboolean("Log", "logging_on")):
    print("Logging On")
else:
    print("Logging off")


print(config["Log"]["log_dir"])
print(config["Database"]["archive_dir"])