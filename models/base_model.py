#!/usr/bin/python3
import uuid
from datetime import datetime
''' a class base model that defines all
    common attributes/ methods for other classes
'''


class BaseModel:
    def __init__(self):
        ''' generates a unique id as string'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        ''' Useful for debugging: shows class name, ID, and all attributes
        (like a snapshot of the object). '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' public instance method that updates the
        public instance attribute update_at with the current
        datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' return a dictionary containing all key/values of __dict__
        on the instance:'''
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            **{k: v for k, v in self.__dict__.items()
                if k not in ['created_at', 'updated_at']}
        }
