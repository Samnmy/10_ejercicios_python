movies = {}

def add_movie():
    title = input("Movie title: ")
    movies[title] = []
    print("Movie added.\n")

def register_rating():
    title = input("Movie title: ")
    if title in movies:
        try:
            rating = int(input("Rating (1-5): "))
            if 1 <= rating <= 5:
                movies[title].append(rating)
                print("Rating recorded.\n")
            else:
                print("Rating out of range.\n")
        except ValueError:
            print("Invalid input.\n")
    else:
        print("Movie not found.\n")

def average_rating():
    title = input("Movie title: ")
    if title in movies and movies[title]:
        avg = sum(movies[title]) / len(movies[title])
        print(f"Average rating for {title}: {avg:.2f}\n")
    else:
        print("No ratings available.\n")

def movie_menu():
    while True:
        print("----- Movie Menu -----")
        print("1. Add movie")
        print("2. Register rating")
        print("3. Calculate average")
        print("4. Exit")
        option = input("Option: ")

        if option == "1": add_movie()
        elif option == "2": register_rating()
        elif option == "3": average_rating()
        elif option == "4": break
        else: print("Invalid option.\n")

movie_menu()
