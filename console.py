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
    This class contains the command interpreter for the HBnB console.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        This method handles the case when an empty line is entered.
        It does nothing and simply returns to the prompt.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a specified class, save it, and print the ID.

        Args:
            arg (str): The class name.

        Example:
            create BaseModel
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        new_obj = eval(class_name)()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance based on the class name and ID.

        Args:
            arg (str): The class name and instance ID.

        Example:
            show BaseModel 1234-1234-1234
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on class and ID.

        Args:
            arg (str): The class name and instance ID.

        Example:
            destroy BaseModel 1234-1234-1234
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print string representations of all instances based on the class name.

        Args:
            arg (str): (Optional) The class name.

        Example:
            all BaseModel
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = args[0]
            if class_name not in ["BaseModel", "User"]:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in globals()[class_name].all().values()])

    def do_update(self, arg):
        """
        Update an instance's attribute based on the class name and ID.

        Args:
            arg (str): The class name, instance ID, attribute name, and attribute value.

        Example:
            update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = storage.all()[key]
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_quit(self, arg):
        """
        Exit the command interpreter.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the command interpreter.
        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
