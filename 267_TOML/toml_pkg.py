# import config
# print(config.path)
# print(config.tic_tac_toe)
# print(config.tic_tac_toe["server"]["url"])
# print(config.tic_tac_toe["constant"]["board_size"])
# print(config.tic_tac_toe["user"]["player_o"])
# print(config.tic_tac_toe["user"]["player_o"]["color"])


from config import tic_tac_toe as CFG
print(CFG["user"]["player_x"]["color"])