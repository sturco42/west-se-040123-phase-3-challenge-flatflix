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
        # Returns a list of all the Review instances for the Movie.
        return [review for review in Review.all if review.movie is self]
    
    def reviewers(self):
        # Returns a unique list of all of the Viewer instances that reviewed the Movie.
        return list({review.viewer for review in self.reviews()})
    
    def average_rating(self):
        # aggregate and association
        # Returns the average of all ratings for the Movie instance
        # To average ratings, add all ratings together and
        # divide by the total number of ratings
        if isinstance(self, Movie):
            scores = [review.rating for review in Review.all if review.movie is self]
            return mean(scores) if len(scores) else 0
    
    @classmethod
    def highest_rated(cls):
        # Returns the Movie instance with the highest average rating.
        if isinstance(cls, Movie):
            max_score = 0
            max_movie = None
            for movie in cls.all:
                avg_score = movie.average_rating()
                if avg_score > max_score:
                    max_score = avg_score
                    max_movie = movie
            return max_movie
                    
            
    
from classes.review import Review
from classes.viewer import Viewer
from statistics import mean
