# Film 0..n <-------> 0..n Actor

import models_da

class Film:
    def __init__(self, eidr, title, year):
        self.__eidr = eidr
        self.__title = title
        self.__year = year
        #-Link attribute----------------------------
        self.__actors = None
        #-------------------------------------------
    
    @property
    def eidr(self):
        return self.__eidr
    
    @property
    def title(self):
        return self.__title
    
    @property
    def year(self):
        return self.__year
    
    #-Association management methods----------------------
    @property 
    def actors(self):
        if self.__actors is None:
            self.__actors = models_da.ActorDA().find_by_film(self)
        return self.__actors
    
    def add_actor(self, actor): 
        self.__actors[actor.id] = actor
        actor.add_film(self) # Bidirectional creation
    #-----------------------------------------------------


class Actor:
    def __init__(self, number, first_name, surname):
        self.__number = number
        self.__first_name = first_name
        self.__surname = surname
        #-Link attribute----------------------------
        self.__films = None # Link attribute
        #-------------------------------------------

    @property
    def number(self):
        return self.__number
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def surname(self):
        return self.__surname
    
    #-Association management methods----------------------
    @property
    def films(self):
        if self.__films is None:
            self.__films = models_da.FilmDA().find_by_actor(self)
        return self.__films
    
    def add_film(self, film):
        self.__films[film.eidr] = film
        film.add_actor(self) # Bidirectional creation
    #-----------------------------------------------------