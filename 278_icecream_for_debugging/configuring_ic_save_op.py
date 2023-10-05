from icecream import ic

def add(x,y):
    return x+y

def output_to_file(text):
    with open('debug_log.txt','a') as f:
        f.write(text + "\n")

ic.configureOutput(
    prefix='Debug| ', outputFunction=output_to_file,
    includeContext=True
)

ic(add(10,20))