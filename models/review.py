#!/usr/bin/python3
"""
Review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines attributes for Review object
    """
    place_id = ""
    user_id = ""
    text = ""
