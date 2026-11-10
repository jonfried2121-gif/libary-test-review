from data.books import books


def get_books_by_name(name:str):
    result = []
    for book in books:
        if name in book["name"]:
            result.append(book)
    return result

def get_book_by_id(id:int):
    for book in books:
        if book["id"] == id:
            return book
    return

def search_book_by_author(author):
    all_books=[]
    for book in books:
        if book["author"] == author:
            all_books.append(book)
    return all_books 

def already_have_book(name,author):
    for book in books:
        if book["name"] == name and book["author"] == author:
            return True
    return

def add_new_book(name,author,year):
    new_book={"id":len(books)+1,"name":name,"author":author,"year":year,"available":True}
    books.append(new_book)

def is_availble(book):
    if book["available"] == True:
        return True
    else:
        return False


def borrow_by_id(book):
    book["available"] == False
    return

def return_by_id(book):
    book["available"] == True
    return
    

def all_availble_books():
    all_books=[]
    for book in books:
        if is_availble(book):
            all_books.append(book)
    return all_books