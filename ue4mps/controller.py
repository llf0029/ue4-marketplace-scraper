# Imports
from abc import ABCMeta, abstractmethod

# Abstract base class
class Controller(metaclass=ABCMeta):

    @abstractmethod
    def search(self, args):
        pass

    @abstractmethod
    def category(self, args):
        pass

    @abstractmethod
    def display_asset_image(self, args):
        pass

    @abstractmethod
    def analyse_results(self, args):
        pass

    @abstractmethod
    def set_search_results(self, args):
        pass

    @abstractmethod
    def save_last_query(self):
        pass

    @abstractmethod
    def load_stored_query(self):
        pass

    @abstractmethod
    def wishlist_add(self, args):
        pass

    @abstractmethod
    def wishlist_view(self, args):
        pass

    @abstractmethod
    def wishlist_clear(self, args):
        pass