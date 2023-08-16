import glob
print(glob.glob('**/*.py',
                root_dir='/Users/anura/Documents/VSCode_Workspace/365-Days-of-Python',
                recursive=True))

# Access it in a memory-efficient way by creating a generator
globs = (glob.iglob('**/*.py',
                root_dir='/Users/anura/Documents/VSCode_Workspace/365-Days-of-Python',
                recursive=True))

print(globs.__next__())
print(globs.__next__())
print(globs.__next__())

for i,file in enumerate(globs, 1):
    print(i, file, sep=': ')