# booklover.py- module 8 hw

import pandas as pd
import numpy as np

class BookLover:
    def __init__(self, n, e, g, nb = 0, bl = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = n
        self.email = e
        self.fav_genre = g
        self.num_books = nb
        self.book_list = bl
        
    def add_book(self, book_name, rating):
        if book_name not in self.book_list['book_name'].values:
            new_book = pd.DataFrame({'book_name': [book_name], 
            'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book],
                                  ignore_index=True)
            self.num_books += 1
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        books = self.book_list[self.book_list['book_rating'] > 3]
        return books
    

        
    