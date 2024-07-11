#!/usr/bin/python3
"""AirBnB Container Module"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, line):
        """A Command To Exit The Program."""
        return True

    def do_EOF(self):
        """Exit The Console."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
