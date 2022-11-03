"""
Main module for command line interface
"""
import typer

# seems to throw import error even though import works fine
from cli import count_stars as cs  # pylint: disable=import-error
from cli import desc_update as du
from cli import status_update as su


app = typer.Typer(no_args_is_help=True)
# app.add_typer(cl.count_stars_cmd, name="starcount")


@app.command()
def count_stars():
    """
    Prompt for account info and prints results from starcount of the chosen
    target
    """
    cs.main_starcount()


@app.command()
def update_description():
    """
    Prompt for account info and update user account description message (bio)
    """
    du.main_description_update()


@app.command()
def update_status():
    """
    Prompt for account info and update user status with new emoji and message
    """
    su.main_status_update()


if __name__ == "__main__":
    app()
