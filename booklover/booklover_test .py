# booklover_test.py- module 8 hw

import pandas as pd
import numpy as np
from booklover import BookLover
import unittest


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        tobj = BookLover("Test Man", "tman22@gmail.com", "Romance")
        tobj.add_book("The Bible", 4)
        if "The Bible" in tobj.book_list['book_name'].values:
            testValue = True
        else:
            testValue = False
        # message if not correct
        message = "The book is not present in the list."
        self.assertTrue(testValue, message)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        tobj = BookLover("Test Man", "tman22@gmail.com", "Romance")
        tobj.add_book("The Bible", 4)
        tobj.add_book("The Bible", 4)
        self.assertEqual(len(tobj.book_list[tobj.book_list['book_name'] == 'The Bible']), 
                         1, 
                         "The book is not in the list the correct number of times.")
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        tobj = BookLover("Test Man", "tman22@gmail.com", "Romance")
        tobj.add_book("Alice in Wonderland", 5)
        self.assertTrue(tobj.has_read('Alice in Wonderland'), "has_read has failed in some way.")
        
    def test_4_has_read(self):
                        
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        tobj = BookLover("Test Man", "tman22@gmail.com", "Romance")
        tobj.add_book("Alice in Wonderland", 5)
        self.assertFalse(tobj.has_read('Jumangi'), "has_read has failed in some way.")
                        
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        tobj = BookLover("Test Man", "tman22@gmail.com", "Romance")
        tobj.add_book("Alice in Wonderland", 5)
        tobj.add_book("Jumangi", 4)
        tobj.add_book("The Scarlet Letter", 4)
        tobj.add_book("The Adventures of Huck Finn", 3)
        self.assertEqual(tobj.num_books, 4, "The number of books read is wrong!")

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        tobj = BookLover("Test Man", "tman22@gmail.com", "Romance")
        tobj.add_book("Alice in Wonderland", 5)
        tobj.add_book("The Adventures of Huck Finn", 3)
        tobj.add_book("Jumangi", 4)
        fav_books = tobj.fav_books()
        for a in fav_books['book_rating']:
            val = a > 3
            self.assertTrue(val, "fav_books is wrong!!!")
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
        
    
    
    