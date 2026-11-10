from books import books
from printer import print_book
from inputs import enter_name_book,enter_author_name,enter_year,enter_book_id
from libary_validation import get_books_by_name,already_have_book,add_new_book,get_book_by_id,borrow_by_id,is_availble,return_by_id,all_availble_books,search_book_by_author
from validations import number_validation,bigger_than_0,valid_string


def display_books():
    for book in books:
        print_book(book)
    return


def search_books():
    name = enter_name_book()
    result = get_books_by_name(name)
    if not result:
        print ("we coudnt find any book according to the name")
        return
    for book in result:
        print_book(book)
    return
    
    

def add_book():
    name = enter_name_book()
    author = enter_author_name()
    year = enter_year()
    try:
        year = number_validation(year)
    except ValueError ("please enter a number year"):
        return
    if not bigger_than_0(year):
        print("year has to be bigger than 0")
        return
    if not valid_string(author):
        print("please enter a valid authors name")
        return
    if already_have_book(name,author):
        print("the book is already in the libary")
        return
    add_new_book(name,author,year)
    return 
    
    

    

def borrow_book():
    book_id = enter_book_id()
    try:
            book_id = number_validation(book_id)
    except ValueError ("please enter a number year"):
        return
    if not bigger_than_0(book_id):
        print("year has to be bigger than 0")
        return
    book = get_book_by_id(book_id)
    if not book:
        print("no such book id")
        return
    if is_availble(book):
        borrow_by_id(book)
        print("book borrowed")
        return
    print("error: the book is currently borrowed")
    return

def return_book():
    book_id = enter_book_id()
    try:
        book_id = number_validation(book_id)
    except ValueError ("please enter a number year"):
        return
    if not bigger_than_0(book_id):
        print("year has to be bigger than 0")
        return
    book = get_book_by_id(book_id)
    if not book:
        print("no such book id")
        return
    if  not is_availble(book):
        return_by_id(book)
        print("book returned")
        return
    print("error: the book is alredy returned")
    return

def get_availble_books():
    availble_list = all_availble_books()
    for book in availble_list:
        print_book(book)
    return

def get_book_by_author():
    author = enter_author_name()
    if not valid_string(author):
        print("enetr a valid string")
        return
    all_books = search_book_by_author(author)
    if not all_books:
        print("no books of this author")
        return
    for book in books:
        print_book(book)
    return



if __name__ == "__main__":
    get_book_by_author()