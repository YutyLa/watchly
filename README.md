# Watchly

**Video demo:** https://www.youtube.com/watch?v=gV22w9WdCVo

**Description:**

Watchly is a command-line interface program which helps you keep track and manage your shows.  I specifically made it for anime/movies, to mark them as "completed" or "to watch".

When running the program, "Watchly" shows with a font generated using figlet and then a menu with seven options.

1. View all shows - Displays a list of all shows in the csv file formatted using tabulate, grouping them by title, type, genre and status.
2. Add show - Used to add a show to the list, you can specify the title, type (preferably "Anime" or "Movie") and status between "completed" or "to watch". The program checks if a show is already added to the list case-insensitively, so duplicates aren't allowed.
3. Remove show - Prompts for the title of the show you want to remove, if the show is not on the list, you are returned back to the menu.
4. Edit show - Lets you edit a show of your choice by specifying the title first. You can update its type, genre or status.
5. Search show - Prompts you for a show title and checks if a mention of the title is in the list, if it is then it will return a tabulate table with all the shows which contain the title entered.
6. Statistics - Displays information regarding the list, the total number of shows, how many are completed, how many are to watch, how many are anime, how many are movies, also calculates a completion rate as a percentage.
7. Exit the program.

Every change made is saved back to "shows.csv" so it stays updated.

# Files

- project.py -- Contains everything regarding the program's functionality. The main() function is a continuous loop and inside it calls each function individually per the user's input.
    - load_shows(filename) -- Reads the file as a list of dictionaries using the csv library. If the file doesn't exist then an empty list is used.
    - save_shows(filename, shows) -- Writes the current list of shows back to the csv file.
    - display_shows(shows) -- Displays a list of shows in the csv file, the first row is taken as a header and keys to the dictionaries.
    - add_shows(shows) -- Specify the title, type, genre and status ("Completed" or "To Watch") for a show you wish to add. If the show is already added the program won't allow duplicates.
    - remove_shows(shows) -- Specify the title of the show you want to remove, case-insensitively.
    - edit_shows(shows) -- Specify the title of the show you want to edit. You can change its type, genre and status ("Completed" or "To Watch").
    - find_shows(shows, title) -- Helper function which takes as arguments a list of shows and a search term, it returns the shows which include the term, case-insensitively
    - search_shows(shows) -- Prompts for the title of a show (search term) then calls the find_shows(show, title) function and then display_shows(show) to print the shows which contain the search term.
    - count_completed(shows) -- Helper function which counts how many shows have the status "Completed" in the list.
    - get_completion_rate(shows) -- Helper function which calculates the percentage of how many shows have been completed. It divides the result of count_completed(shows) function with the length of the list of shows, rounds it to two decimal digits, returns the result.
    - statistics(shows) -- Uses the two helper functions count_completed(shows), get_completion_rate(shows) and prints a summary report.
- test_project.py -- Contains the test functions for project.py, these functions don't require user input.
    - test_find_shows() -- Checks that searching "death" returns 2 out of 3 shows given, which is correct.
    - test_count_completed() -- Checks that there are 2 shows with the status "Completed" which is correct.
    - test_get_completion_rate() -- Checks the completion rate is calculated correctly.
- shows.csv -- The data file which is read and written, it has four columns (Title, Type, Genre, Status). The file is created automatically the first time a show is added if it doesn't exist.
- requirements.txt -- A list of packages used in the project.

# How to run the program:

1. Install the packages:
```pip install -r requirements.txt```
2. Run the program:
```python project.py```
3. Follow the menu to add, view, edit, remove or search shows.

To run the test functions:
```pytest test_project.py```

# Design choices

 The project was made with personal use in mind. It isn't very flexible/friendly and forces the user to only choose between "Completed" and "To Watch".

 The statistics(shows) function won't count if a user adds a show with a type other than "Anime" or "Movie". Also, if two shows happen to have the same title, the remove and edit functions would only affect the first matching one.

 Originally I was planning on using object-oriented programming for the project but it was becoming complex and the csv module was a simpler solution. It was proving to be difficult to test the normal functions in test_project.py, that is why the helper functions were added so those could be tested instead.

 Overall, the project's main goal was to see which shows were to watch and which were completed.