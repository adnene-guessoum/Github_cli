"""
Command for counting number of stars in specified account
"""
import typer
from .count_stars import main_starcount

count_stars_cmd = typer.Typer(no_args_is_help=True)


@count_stars_cmd.command()
def prompt_count():
    """
    prompt for account info and prints results from count
    """
    main_starcount()


if __name__ == "__main__":
    count_stars_cmd()
