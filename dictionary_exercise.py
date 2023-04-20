# make a books dictionary, with 3 authors as keys and multiple books as values. least 2 books for each author
# usse an input()asking for author name and print as a string the list of books by that
#author. use the .join()method

books_dictionary = {"Stephanie Myers": ["Twilight", "New Moon", "Eclipse"], "Jane Austen": ["Pride and Prejudice", "Sense and sensibilities", "Mansfield Park"], "Stephen King": ["The Shining", "Fairy Tale", "It"]}
                    
print(books_dictionary)

y = input("enter author name: ")
print(", ".join(books_dictionary[y]))


