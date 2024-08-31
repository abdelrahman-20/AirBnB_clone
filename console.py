"""Command Line Module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Base Class For The Console Application."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit The Console"""
        return True

    def do_EOF(self):
        """Exit The Console"""
        return True

    def emptyline(self):
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
