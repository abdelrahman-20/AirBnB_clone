#!/usr/bin/python3
"""AirBnB Container Module"""

import cmd
from models import storage


# from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_show(self, line=None):
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.my_class_list():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(f"[{args[0]}] ({storage.all()[key]['id']}) {storage.all()[key]}")

    def do_create(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.my_class_list():
            print("** class doesn't exist **")
        else:
            new_obj = storage.my_class_list()[line]()
            new_obj.save()
            print(new_obj.id)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """Exit The Console."""
        return True

    def emptyline(self):
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
