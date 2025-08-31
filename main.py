import cmd
import os
from colorama import Fore
from prettytable import PrettyTable, TableStyle

list = ["item 1", "item 2", "item 3", "item 4"]
fm = Fore.MAGENTA
fy = Fore.YELLOW
fr = Fore.RESET

header = PrettyTable()
header.field_names = [f" {fm}Simple CLI{fr}"]
header.add_row([f'  Type {fy}"help"{fr} for a list of all commands'])
header.align = "l"
header.format = True
header.set_style(TableStyle.DOUBLE_BORDER)


def clear_terminal():
    match os.name:
        case "nt":
            os.system("cls")
        case _:
            os.system("clear")


class MyCLI(cmd.Cmd):
    clear_terminal()
    prompt = "󰄾 "
    intro = header.get_string()

    def precmd(self, line):
        return line

    def do_hello(self, line):
        print("Hello!")

    def do_q(self, line):
        print("Bye Bye :(")
        return True

    def q(self):
        print("It quits")


if __name__ == "__main__":
    MyCLI().cmdloop()
    clear_terminal()
