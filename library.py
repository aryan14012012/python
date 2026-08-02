# My Library Book Organiser

# Lists to store book names
books = ["Python Basics", "Data Structures", "Machine Learning", "Algorithms"]

# Add a new book to the list
books.append("Web Development")

# Remove a book from the list
books.remove("Algorithms")

# Sort the books alphabetically
books.sort()

# Reverse the order of the books
books.reverse()

# Indexing example
first_book = books[0]

# Slicing example
book_slice = books[1:3]

# Dictionary to store librarian details
librarian = {
    "name": "Ms. Riya",
    "age": 32,
    "department": "Children's Section"
}

# Dictionary operations
librarian["shift"] = "Morning"
librarian.pop("age")
updated_librarian = librarian.copy()

# Convert two lists into a dictionary using dict() and zip()
book_ids = [101, 102, 103, 104]
book_titles = ["Python Basics", "Data Structures", "Machine Learning", "Web Development"]
book_directory = dict(zip(book_ids, book_titles))

# Display results
print("My Library Book Organiser")
print("-" * 30)
print("Book list:", books)
print("First book:", first_book)
print("Sliced books:", book_slice)
print("Librarian details:", updated_librarian)
print("Book directory:", book_directory)
