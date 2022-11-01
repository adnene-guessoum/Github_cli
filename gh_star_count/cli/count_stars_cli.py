import typer

from .count_stars import *

count_stars_cmd = typer.Typer(no_args_is_help=True)

@count_stars_cmd.command()
def prompt_count():
   name_search, orga_status = ask_prompt()
   count(name_search, orga_status)

if __name__ == "__main__":
    count_stars_cmd()
