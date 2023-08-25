import click

VERSION = "0.1.0"

@click.command()
@click.version_option(VERSION, message="%(version)s")
def main():
    print("This is a test command!")
"""
python main.py --help 
python main.py --version
"""

@click.command()
@click.argument("names",nargs=2) # nargs=-1 means no limit
def profile(names):
    print(names)
"""
python main.py anurag bamba 
"""

@click.command()
@click.option("-a","--age", type=int, default=0)
def Age(age):
    print(age)
"""
python main.py -a 24 
"""

@click.command()
@click.argument("names",nargs=2) # nargs=-1 means no limit
@click.option("-a","--age", type=int, default=0)
# @click.option("-s","--shout", is_flag=True)
@click.option("--shout/--no-shout")
@click.option("-f","--file", type=click.File("w"))
def Bio(names,age,shout,file):
    text = f"My name is {' '.join(names)} and I am {age} years old."
    
    if shout:
        text = text.upper()

    if file:
        print(f"Saving to {file.name}")
        file.write(text)
    
    print(text)
"""
python main.py Anurag Bambardekar -a 24 -s
python main.py Anurag Bambardekar -sa 24
python main.py Anurag Bambardekar -a 24 --shout
python main.py Anurag Bambardekar -a 24 --no-shout
python main.py Anurag Bambardekar -a 24 -f profile.txt
"""

if __name__ == "__main__":
    # main()
    # profile()
    # Age()
    Bio()