#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Handles the EOF signal (Ctrl+D) to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn't execute anything.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file,
        and prints the id.

        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.

        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            instances = storage.all()
            key = args[0] + "." + args[1]
            print(instances[key])
        except IndexError:
            if args[0] in storage.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.

        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            instances = storage.all()
            key = args[0] + "." + args[1]
            del instances[key]
            storage.save()
        except IndexError:
            if args[0] in storage.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances based or not
        on the class name.

        Usage: all or all <class name>
        """
        args = arg.split()
        instances = storage.all()
        obj_list = []
        if not args:
            for key in instances:
                obj_list.append(str(instances[key]))
        else:
            if args[0] in storage.classes:
                for key in instances:
                    if key.split(".")[0] == args[0]:
                        obj_list.append(str(instances[key]))
            else:
                print("** class doesn't exist **")
                return
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating an attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            instances = storage.all()
            key = args[0] + "." + args[1]
            obj = instances[key]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            setattr(obj, attr_name, attr_value)
            obj.save()
        except IndexError:
            if args[0] in storage.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()