import cmd, os, parse, platform, sys
from colorama import Fore
from prettytable import PrettyTable, TableStyle

fm = Fore.MAGENTA
fy = Fore.YELLOW
fr = Fore.RED
freset = Fore.RESET

header = PrettyTable()
header.field_names = [f" {fm}Simple CLI{freset}"]
header.add_row([f'  Type {fy}"help"{freset} for a list of all commands'])
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
        print()
        return line

    def do_print(self, arg):
        "Prints his arguments"
        print(arg)

    def do_q(self, line):
        "Quit CLI"
        print("Bye Bye :(")
        return True

    def postcmd(self, stop, line):
        print()
        return stop

    def help_help(self):
        print("List help")


if __name__ == "__main__":
    MyCLI().cmdloop()
    clear_terminal()
