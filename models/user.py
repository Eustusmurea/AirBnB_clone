#!/usr/bin/python3
"""Defines the User class."""
#!/usr/bin/python3

"""
Shows the user details of a User instance
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from base model.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self):
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
