import typer
import cli.count_stars_cli
#from cli.count_stars_cli import count_stars_cmd

app = typer.Typer(no_args_is_help=True)
app.add_typer(cli.count_stars_cli.count_stars_cmd, name = "starcount")

if __name__ == "__main__":
    app()
