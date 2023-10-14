#!/usr/bin/python3
"""
This shows the city where the place is located.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from base model.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    def __init__(self):
        super().__init__()
        self.state_id = ""
        self.name = ""
