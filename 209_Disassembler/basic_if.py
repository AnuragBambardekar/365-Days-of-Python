import dis

def fct(x):
    if x==5:
        return True
    else:
        return False
    
dis.dis(fct)