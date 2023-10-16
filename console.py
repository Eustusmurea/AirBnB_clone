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
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        new_obj = eval(class_name)()
        new_obj.save()
        print(new_obj.id)


    """The code defines a method called  do_show  that takes in arguments for class name and instance id. It checks if the provided class and instance exist in the storage and 
    prints the corresponding instance or error messages accordingly.
    """
    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
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

"""
 Delete an instance based on class and ID.

Args:
    arg (str): The class name and instance ID.

"""
        
       def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
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

"""
Show all instances or instances of a specific class.
 Args:
            arg (str): (Optional) The class name.
"""

 def do_all(self, arg):
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = args[0]
            if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in globals()[class_name].all().values()])

           def do_update(self, arg):
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
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
            print("** dictionary missing **")
            return
        try:
            attributes = eval(args[2])
            if not isinstance(attributes, dict):
                raise ValueError
        except (NameError, ValueError, SyntaxError):
            print("** invalid dictionary format **")
            return
        obj = storage.all()[key]
        for attr, value in attributes.items():
            setattr(obj, attr, value)
        obj.save()
      
"""
Count the number of instances in a class.

 Args:
     arg (str): The class name.
"""
def do_count(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        count = len(globals()[class_name].all())
        print(count)

"""
Exit the command interpreter.
"""

def do_quit(self, arg):
        return True

"""
Exit the command interpreter.
"""
def do_EOF(self, arg):
        print()
        return True



if __name__ == "__main__":
    HBNBCommand().cmdloop()