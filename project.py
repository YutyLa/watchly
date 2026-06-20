import csv
from tabulate import tabulate
from pyfiglet import Figlet


def main():
    figlet = Figlet(font="standard")
    shows = load_shows("shows.csv")
    print(figlet.renderText("Watchly"))
    while True:
        print("""
              1. View all shows
              2. Add show
              3. Remove show
              4. Edit show
              5. Search show
              6. Statistics
              7. Exit""")
        choice = input("Select an option: ")
        if choice == "1":
            display_shows(shows)
        elif choice == "2":
            add_shows(shows)
            save_shows("shows.csv", shows)
        elif choice == "3":
            remove_show(shows)
            save_shows("shows.csv", shows)
        elif choice == "4":
            edit_shows(shows)
            save_shows("shows.csv", shows)
        elif choice == "5":
            search_show(shows)
        elif choice == "6":
            statistics(shows)
        elif choice == "7":
            break
        else:
            print("Invalid Selection")


def load_shows(filename):
    shows = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                shows.append(row)
    except FileNotFoundError:
        pass
    return shows


def display_shows(shows):
    print(tabulate(shows, headers="keys", tablefmt="grid"))


def add_shows(shows):
    title = input("Title: ")
    show_type = input("Type: ")
    genre = input("Genre: ")
    while True:
        print("""
            1. To Watch
            2. Completed""")

        choice = input("Status: ")

        if choice == "1":
            status = "To Watch"
            break
        elif choice == "2":
            status = "Completed"
            break
        else:
            print("Invalid status")
    for show in shows:
        if show["Title"].lower() == title.lower():
            print("Show already exists")
            return
    shows.append({"Title": title, "Type": show_type, "Genre": genre, "Status": status})
    print("Show has been added")


def remove_show(shows):
    title = input("Show title: ")
    for show in shows:
        if show["Title"].lower() == title.lower():
            shows.remove(show)
            print("Show has been removed")
            return
    print("Show not found")


def save_shows(filename, shows):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Type", "Genre", "Status"])
        writer.writeheader()
        writer.writerows(shows)


def find_shows(shows, title):
    matches = []
    for show in shows:
        if title.lower() in show["Title"].lower():
            matches.append(show)
    return matches


def search_show(shows):
    title = input("Search: ")
    matches = find_shows(shows, title)
    if matches:
        display_shows(matches)
    else:
        print("Show not found")


def edit_shows(shows):
    title = input("Show title : ")
    for show in shows:
        if show["Title"].lower() == title.lower():
            while True:
                print("""
                    1. Change Type
                    2. Change Genre
                    3. Change Status""")
                choice = input("Select an option: ")
                if choice == "1":
                    new_type = input("Enter new show type: ")
                    show["Type"] = new_type
                    print("Show updated")
                    return
                elif choice == "2":
                    new_genre = input("Enter new show genre: ")
                    show["Genre"] = new_genre
                    print("Show updated")
                    return
                elif choice == "3":
                    while True:
                        print("""
                                1. To Watch
                                2. Completed""")
                        choice = input("Status: ")
                        if choice == "1":
                            show["Status"] = "To Watch"
                            break
                        elif choice == "2":
                            show["Status"] = "Completed"
                            break
                        else:
                            print("Invalid selection")
                    print("Show updated")
                    return
                else:
                    print("Invalid selection")
    else:
        print("Show not found")


def count_completed(shows):
    completed = 0
    for show in shows:
        if show["Status"] == "Completed":
            completed += 1
    return completed


def get_completion_rate(shows):
    if len(shows) == 0:
        return 0
    completed = count_completed(shows)
    return round((completed / len(shows)) * 100, 2)


def statistics(shows):
    total_shows = 0
    to_watch = 0
    movies = 0
    anime = 0
    for show in shows:
        total_shows += 1
        if show["Status"] == "To Watch":
            to_watch += 1
        if show["Type"] == "Anime":
            anime += 1
        if show["Type"] == "Movie":
            movies += 1
    completed = count_completed(shows)
    completion_rate = get_completion_rate(shows)
    print(f"""
          Total shows: {total_shows}
          Completed: {completed}
          To Watch: {to_watch}
          Anime: {anime}
          Movies: {movies}
          Completion rate: {completion_rate}%""")


if __name__ == "__main__":
    main()
