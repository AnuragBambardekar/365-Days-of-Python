# pip install rich

from rich import print

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

from rich.console import Console

console = Console()
console.print("Hello", "World!", style="bold red")
console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

# print emojis in console
console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")