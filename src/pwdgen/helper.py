from rich.console import Console
from rich.table import Table


def pwd_table(name, password, length):
    console = Console()

    table = Table()

    table.add_column(name, justify="center")
    table.add_column("length", justify="center")

    table.add_row(password, str(length))

    console.print(table)
