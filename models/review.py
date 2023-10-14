#!/usr/bin/python3

"""
This shows the previous reviews of the apartment
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class which inherits from BaseModel
    Attributes:
        place_id (str): The id of the place.
        user_id (str): The id of the user.
        text (str): The review.
    """
    def __init__(self):
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
