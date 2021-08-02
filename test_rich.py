from rich.console import Console


# console = Console()
# console.print("Hello", "World!")
# console.print("Hello", "World!", style="bold red")
# console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

# test_data = [
#     {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},
#     {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
#     {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
# ]

# def test_log():
#     enabled = False
#     context = {
#         "foo": "bar",
#     }
#     movies = ["Deadpool", "Rise of the Skywalker"]
#     # console.log("Hello from", console, "!")
#     console.log(test_data, log_locals=True)


# test_log()


from rich.console import Console
from rich.table import Column, Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=6, justify='center')
table.add_column("Title", justify='center')
table.add_column("Production Budget", justify="right")
table.add_column("Box Office", justify="right")
table.add_row(
    "Dev 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
    "May 25, 2018",
    "[red]Solo[/red]: A Star Wars Story",
    "$275,000,000",
    "$393,151,347",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VIII: The Last Jedi",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)

console.print(table)

