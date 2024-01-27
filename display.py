from os import system, name


class Display:
    def print_menu(self, title, options):
        print(f"Welcome - you are in the {title}\n")
        print(f"{options}\n")  # for keys, values in dict (dict comprehension)
        return int(input("What do you want do do? "))

    def print_table(self, table):
        print(table)

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
