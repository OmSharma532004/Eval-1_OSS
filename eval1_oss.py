library_inventory = {}

def add_book(title, author, isbn, genre, availability):
    book={'title': title,'author': author,'genre': genre,'availability': availability
    }
    library_inventory[isbn] = book
    print("Book " ,title, " added successfully \n .")

def update_book_details(isbn, title=None, author=None, genre=None, availability=None):
    if title is not None:
        library_inventory[isbn]['title'] = title
    if author is not None:
        library_inventory[isbn]['author'] = author
    if genre is not None:
        library_inventory[isbn]['genre'] = genre
    if availability is not None:
        library_inventory[isbn]['availability'] = availability
    print("\n Book with ISBN ", isbn ," updated successfully.\n Updated Book:-  ",library_inventory[isbn])

def search_by_isbn(isbn):
    book = library_inventory.get(isbn)
    if book:
        print(" \n  Book Found:- ",book)
    else:
        print(" \n  Book Not Found")
       


def generate_genre_report():
    genre_report = {}
    for book in library_inventory.values():
        genre = book['genre']
        if genre not in genre_report:
            genre_report[genre] = []
        if book['availability']:
            genre_report[genre].append(book['title'])
    
    for genre, books in genre_report.items():
        print("Genre :- ",genre)
        for book in books:
            print(f" - {book}")
        print()


        
add_book("Stocks","Om",1,"Market",True)
add_book("F/O","Om",2,"Market",True)
add_book("MF","Om",3,"Investement",True)

update_book_details(1,availability=False)


search_by_isbn(2)
search_by_isbn(4)

generate_genre_report()







