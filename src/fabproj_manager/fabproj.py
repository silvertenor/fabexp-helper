# cli.py
import click, os, sys, shutil
dirname = os.path.dirname(__file__)
sys.path.append(dirname)
import modules.ipyCreate as ipyCreate

dirname = os.getcwd()


@click.command()
@click.argument("command")
@click.option("--name", "-n")


def create_project(command, name):
    if command == "add":
        confirmation = input(
            f"Do you want to add a new project titled {name} in the current working directory? (yes/no) "
        )
        if confirmation == "yes":
            os.makedirs(os.path.join(dirname, "upload"), exist_ok=True)
            os.makedirs(os.path.join(dirname, "download"), exist_ok=True)
            os.makedirs(os.path.join(dirname, "include"), exist_ok=True)
            shutil.copy('./modules/img/fabric_logo.png', './include/img/fabric_logo.png')
            ipyCreate.create_fab_notebook(name)


if __name__ == "__main__":
    create_project()
