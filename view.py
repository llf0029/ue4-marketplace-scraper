# Imports
from abc import ABCMeta, abstractmethod

# Abstract base class
class View(metaclass=ABCMeta):

    @abstractmethod
    def display(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass

    @abstractmethod
    def display_items_formatted(self, data):
        pass

    @abstractmethod
    def display_image(url):
        pass