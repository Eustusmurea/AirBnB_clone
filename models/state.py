#!/usr/bin/python3

"""
This shows the stste in which the place is located
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    State class which inherits from BaseModel
    Attributes:
        name (str): name of the state
    """
    def __init__(self):
        super().__init__()
        self.name = ""

