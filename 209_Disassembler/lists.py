import dis
def list_func1():
    results = []
    for x in range(10):
        results.append(x)
    return results

def list_func2():
    return [x for x in range(10)]

print("===============================================================")
dis.dis(list_func1)
print("===============================================================")
dis.dis(list_func2)
print("===============================================================")