import click

@click.group(invoke_without_command=True)
@click.pass_context
def cmd(ctx):
    if not ctx.invoked_subcommand:
        return
    print("This is a group command!")

@cmd.command()
def subcommand():
    print("This is a sub-command.")

"""
python subcommand.py
python subcommand.py subcommand
"""

if __name__=="__main__":
    cmd()