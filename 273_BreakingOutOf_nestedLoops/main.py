# for i in range(10):
#     for j in range(20):
#         print(f"{i=},{j=}")
#         if i+j == 10:
#             print('condition met, breaking out!')
#             break


# for...else
for i in range(10):
    # done = False
    for j in range(5):
        print(f"{i=},{j=}")
        if i+j == 10:
            print('condition met, breaking out!')
            # done = True
            break
    else:
        continue
    break
    print("rest of code...")