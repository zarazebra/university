from display import Display


class MenuPage:
    def __init__(self, title, options):
        self.menu_title = title
        self.menu_options = options

    def select_menu_option(self):
        display = Display()
        display.clear()
        title = self.menu_title
        options = self.menu_options
        return display.print_menu(title, options)
