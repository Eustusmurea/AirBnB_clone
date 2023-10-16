import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

"""
Retrieve all objects from storage.

 Returns:
      dict: A dictionary of all stored objects.
"""
    def all(self):
        return self.__objects

"""
 Add a new object to storage.

Args:
 obj: The object to be added to storage.
"""
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        
        self.__objects[key] = obj

"""
Save objects to the JSON file.
"""
         
    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

"""
Load objects from the JSON file and populate the storage.
"""
  
    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "BaseModel":
                        class_ = BaseModel
                    elif class_name == "User":
                        class_ = User
                    elif class_name == "Place":
                        class_ = Place
                    elif class_name == "State":
                        class_ = State
                    elif class_name == "City":
                        class_ = City
                    elif class_name == "Amenity":
                        class_ = Amenity
                    elif class_name == "Review":
                        class_ = Review
                    else:
                        continue
                    obj = class_(**obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass