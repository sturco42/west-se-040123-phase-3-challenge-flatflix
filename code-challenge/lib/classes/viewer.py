class Viewer:
    
    all = []
    
    def __init__(self, username):
        self.username = username
        type(self).all.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 6 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise Exception('new_username must be a string between 6 and 16 chars inclusive')
    
    def reviews(self):
        # Returns a list of Review instances associated with the Viewer instance.
        return [review for review in Review.all if review.viewer is self]
    
    # Returns a list of Movie instances reviewed by the Viewer instance.
    def reviewed_movies(self):
        return list({review.movie for review in self.reviews()})
    #review.movie

    def has_reviewed_movie(self, movie):
        # Returns True if the Viewer has reviewed this Movie
        # (if there is a Review instance that has this Viewer and Movie),
        # returns False otherwise
        return movie in self.reviewed_movies()

from classes.review import Review
from classes.movie import Movie