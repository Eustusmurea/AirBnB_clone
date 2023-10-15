#!/bin/python3

"""
This shows the resources of a place. 
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class that inherits from base model.
    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self):
        super().__init__()
        self.name = ""
