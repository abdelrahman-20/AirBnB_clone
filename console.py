#!/usr/bin/python3
"""AirBnB Container Module"""

import cmd
from models import storage


# import re


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
        if line == "" or line is None:
            results = []
            for k, v in storage.all().items():
                # results.append(str(v))
                sub_args = k.split(".")
                results.append(f"[{sub_args[0]}] ({sub_args[1]}) {v}")
            print(results)
        else:
            results = []
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

    def do_update(self, line):
        # if line == "" or line is None:
        #     print("** class name missing **")
        #     return
        #
        # rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        # match = re.search(rex, line)
        # classname = match.group(1)
        # uid = match.group(2)
        # attribute = match.group(3)
        # value = match.group(4)
        # if not match:
        #     print("** class name missing **")
        # elif classname not in storage.my_class_list():
        #     print("** class doesn't exist **")
        # elif uid is None:
        #     print("** instance id missing **")
        # else:
        #     key = "{}.{}".format(classname, uid)
        #     if key not in storage.all():
        #         print("** no instance found **")
        #     elif not attribute:
        #         print("** attribute name missing **")
        #     elif not value:
        #         print("** value missing **")
        #     else:
        #         cast = None
        #         if not re.search('^".*"$', value):
        #             if '.' in value:
        #                 cast = float
        #             else:
        #                 cast = int
        #         else:
        #             value = value.replace('"', '')
        #         attributes = storage.attributes()[classname]
        #         if attribute in attributes:
        #             value = attributes[attribute](value)
        #         elif cast:
        #             try:
        #                 value = cast(value)
        #             except ValueError:
        #                 pass  # fine, stay a string then
        #         setattr(storage.all()[key], attribute, value)
        #         storage.all()[key].save()
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            class_name = args[0]
            if class_name not in storage.my_class_list():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj_id = args[1]
                attribute = args[2]
                value = args[3]
                key = f"{args[0]}.{obj_id}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    attributes = storage.my_class_attributes()[class_name]
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    print(
                        f"Class: {class_name} \nID: {obj_id} \nAll Attributes: {attributes} \nAttribute: {attribute} \nValue: {value}")
                    # setattr(storage.all()[key], attribute, value)
                    # storage.save()

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
