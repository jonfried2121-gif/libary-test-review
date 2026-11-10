from validations.validations import number_validation,valid_pick,all_menu_validations
from system.function import display_books,search_books,add_book,borrow_book,return_book,get_availble_books,get_book_by_author
from user.inputs import enter_menu_pick
print("""================================
       LIBRARY MANAGEMENT
================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
8. Exit

""")

def menu():

    while True:
        pick = enter_menu_pick()

        check = all_menu_validations(pick)
        if check != "ok":
            print(check)
            continue

        if pick == "1":
            display_books()
        if pick == "2":
            search_books()
        if pick == "3":
            add_book()
        if pick == "4":
            borrow_book()
        if pick == "5":
            return_book()
        if pick == "6":
            get_availble_books()
        if pick == "7":
            get_book_by_author()
        if pick == "8":
            break
menu()
    







