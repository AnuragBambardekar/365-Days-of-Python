import os

size = ''

while not size.isnumeric():
    size = input('How big would you like your file to be (mb)? ')

size = int(size)

name = input('Enter the file name: ')

# Get the current working directory
current_directory = os.getcwd()
file_path = os.path.join(current_directory, name)

open(file_path, 'w').write('')

for mb in range(size):
    open(file_path, 'a').write('M' * 1000000)

print('Done!')
