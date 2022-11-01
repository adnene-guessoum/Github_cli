"""
Main module for command line interface
"""
import typer

# seems to throw import error even though import works fine
from cli import count_stars_cli as cl  # pylint: disable=import-error

app = typer.Typer(no_args_is_help=True)
app.add_typer(cl.count_stars_cmd, name="starcount")

if __name__ == "__main__":
    app()
