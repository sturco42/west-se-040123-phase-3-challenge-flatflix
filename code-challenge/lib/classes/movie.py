class Movie:
    
    all = []
    
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and new_title:
            self._title = new_title
        else:
            raise Exception('title must be string greater than 0')
    
    def reviews(self):
        pass
    
    def reviewers(self):
        pass
    
    def average_rating(self):
        pass
    
    @classmethod
    def highest_rated(cls):
        pass
    
from classes.review import Review
from classes.viewer import Viewer
