"""
Filename: action.py
Description: Class definition for an action item
Author: Porter Farley
Contact: pfarley509@gmail.com
Date Created: 08/27/2024
"""

class Action():
    
    def __init__(self, name: str, description: str, on_call: callable) -> None:
        self.name = name
        self.description = description
        self.on_call = on_call
        
    def __str__(self) -> str:
        return f'\033[4m{self.name}\033[0m: {self.description}'