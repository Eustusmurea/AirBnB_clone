#!/usr/bin/python3

"""
This shows the location of the place
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class that inherits from BaseModel Class
    Attributes:
        city_id(str): the city id
        user_id(str): the user id
        name(str): name input
        description(str): description input
        number_of_rooms(int): the number of rooms
        number_of_bathrooms(int): the number of bathrooms
        max_guests(int): the maximum number of guests
        price_per_night(int): the price for each night
        latitude(float): latitude coordinates of the place
        longitude(float): longitude coordinates of the place
        amenity_ids(list): ids for amenities available in the place
    """

    def __init__(self):
        super().__init__()
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_of_rooms = 0
        self.number_of_bathrooms = 0
        self.max_guests = 0
        self.price_per_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
