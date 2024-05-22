from abc import ABC, abstractmethod

"""
Defineste o clasa abstracta AbstractVideo.
Aceasta va avea o metoda abstracta show_details.
De asemenea, va mai avea o metoda, play, care va afisa mesajul
'Video is playing.'
"""
class AbstractVideo(ABC):

    @abstractmethod
    def show_details(self):
        pass

    def play(self):
        print('Video is playing')


"""
Defineste o clasa Videoclip.
Aceasta va implementa clasa abstracta AbstractVideo.
Va avea atribute in constructor: title, duration.
Va implementa metoda show_details, in care va afisa mesajul:
'<title> has a duration of <duration> minutes.'
"""
class Videoclip(AbstractVideo):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_details(self):
        print(f'{self.title} has a duration of {self.duration} minutes.')


"""
a. Defineste o clasa numita Movie care va mosteni clasa Videoclip.
Extinde constructorul/metoda de initializare a clasei Movie,
astfel incat sa aiba ca atribute si :
- genre (str)
- director (str) -> ATRIBUT PRIVAT!
- actors (list)

b. Extinde metoda show details, astfel incat sa se afiseze si
mesajul: 
'Is directed by {director} and the actors are {actors}.'

c. Defineste o proprietate director, cu getter, setter si deleter,
care incapsuleaza atributul privat __director.
"""

class Movie(Videoclip):
    def __init__(self, title, duration, genre, director, actors):
        super().__init__(title, duration)
        self.genre = genre
        self.__director = director
        self.actors = actors

    def show_details(self):
        super().show_details()
        print(f'Is directed by {self.__director} and the actors are {self.actors}.')

    @property
    def director(self):
        pass
    @director.getter
    def director(self):
        return self.__director

    @director.setter
    def director(self, name):
        if all(i.isalpha() or i.isspace() for i in name):
            self.__director = name
            print(f'Getter: The director is: {self.__director}')
        else:
            raise TypeError('The name must contain only alphabetical characters')

    @director.deleter
    def director(self):
        self.__director = None


# movie1 = Movie('The Godfather', 175, 'Crime/Drama', 'Francis Ford Coppola', ["Marlon Brando", "Al Pacino", "James Caan", "Robert Duvall", "Diane Keaton"])
# movie1.play()
# movie1.show_details()
#
# print(movie1.director)
# movie1.director = 'F F Coppola'
# print(movie1.director)
#
# print(f'{movie1.title} is a {movie1.genre} movie, has a duration of {movie1.duration} minutes and it was directed by {movie1.director}.')
# print(f'The main roles are played by:')
# for actor in movie1.actors:
#     print(actor)