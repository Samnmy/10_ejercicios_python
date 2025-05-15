library = []

def add_book():
    title = input("Book title: ")
    author = input("Book author: ")
    try:
        pages = int(input("Number of pages: "))
    except ValueError:
        print("Invalid number of pages.")
        return
    book = {"title": title, "author": author, "pages": pages}
    library.append(book)
    print(f'Book "{title}" successfully added.\n')

def search_book():
    title = input("Enter title to search: ")
    results = [book for book in library if book["title"].lower() == title.lower()]
    if results:
        print("\nResults found:")
        for book in results:
            print(f'- {book["title"]}, {book["author"]} ({book["pages"]} pages)')
    else:
        print("Book not found.\n")

def show_books():
    if not library:
        print("No books in the library.\n")
    else:
        print("\nAvailable books:")
        for book in library:
            print(f'- {book["title"]}, {book["author"]} ({book["pages"]} pages)')
        print()

def library_menu():
    while True:
        print("Library Menu: ")
        print("1. Add book")
        print("2. Search book by title")
        print("3. Show all books")
        print("4. Exit")
        option = input("Select an option: ")

        if option == "1":
            add_book()
        elif option == "2":
            search_book()
        elif option == "3":
            show_books()
        elif option == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

library_menu()
