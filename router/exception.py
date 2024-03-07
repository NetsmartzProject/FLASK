
# In exception.py
class StoryException(Exception):
    def __init__(self, name):
        self.name = name
