with open('118_Zen_Of_python_(Easter_eggs)/input.txt','r') as input, open('118_Zen_Of_python_(Easter_eggs)/output.txt','w') as output:
    text = input.readlines()
    uppercase = [t.upper() for t in text]
    output.writelines(uppercase)