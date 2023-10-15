#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


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
        """Create a new User instance"""
        if arg == "User":
            new_user = User()
            new_user.save()
            print(new_user.id)

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show details of a User instance"""
        args = arg.split()
        if len(args) == 2 and args[0] == "User":
            user_id = args[1]
            user = models.storage.get(User, user_id)
            if user is not None:
                print(user)
            else:
                print("** no instance found **")
                

    def do_destroy(self, arg):
        """Destroy a User instance"""
        args = arg.split()
        if len(args) == 2 and args[0] == "User":
            user_id = args[1]
            user = models.storage.get(User, user_id)
            if user is not None:
                user.delete()
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all User instances"""
        if arg == "User":
            users = models.storage.all(User)
            for user in users.values():
                print(user)

    def do_update(self, arg):
        """Update attributes of a User instance"""
        args = arg.split()
        if len(args) >= 2 and args[0] == "User":
            user_id = args[1]
            user = models.storage.get(User, user_id)
            if user is not None:
                if len(args) >= 3:
                    attr_name = args[2]
                    if len(args) >= 4:
                        attr_value = args[3]
                        setattr(user, attr_name, attr_value)
                        user.save()
                        return
                print("** attribute name missing **")
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()