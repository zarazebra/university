from os import system, name
from rich.console import Console
from rich.table import Table


class Display: # TODO: show tables with library rich
    def print_menu(self, menu_title, menu_options):
        table = Table(title=menu_title)
        table.add_column("No.")
        table.add_column("Option")
        for key, value in menu_options.items():
            table.add_row(key, value)
        console = Console()
        console.print(table)
        return input("What do you want do do? ")

    def print_table(self, table_title, column_titles, row_values):
        table = Table(title=table_title)
        self.clear()
        for title in column_titles:
            table.add_column(title)
        for value in row_values:
            table.add_row(value[0], value[1], value[2])
        console = Console()
        console.print(table)

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
