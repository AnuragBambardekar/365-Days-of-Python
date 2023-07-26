import dis

def comp_floats():
    return 0.1+0.2 == 0.3

dis.dis(comp_floats)