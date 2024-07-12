#!/usr/bin/python3
"""AirBnB Container Module"""

import cmd
from models import storage


# from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_show(self, line=None):
        """Get A Stored Instance of A Class."""
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
        """Create New Instance of A Class"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.my_class_list():
            print("** class doesn't exist **")
        else:
            new_obj = storage.my_class_list()[line]()
            new_obj.save()
            print(new_obj.id)

    def do_destroy(self, line):
        """Delete Create Instance of Class."""
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
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Get All Instances for Class(es)."""
        results = []
        if line == "" or line is None:
            for k, v in storage.all().items():
                # results.append(str(v))
                sub_args = k.split(".")
                results.append(f"[{sub_args[0]}] ({sub_args[1]}) {v}")
            print(results)
        else:
            args = line.split(" ")
            if args[0] not in storage.my_class_list():
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    if v["__class__"] == args[0]:
                        # results.append(str(v))
                        sub_args = k.split(".")
                        results.append(f"[{sub_args[0]}] ({sub_args[1]}) {v}")
                print(results)

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
