import json
import os

# File to store library data
LIBRARY_FILE = "library.txt"

# Load library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library():
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book():
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    if not title or not author or not year.isdigit():
        print("❌ Invalid input! Please enter correct details.")
        return

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    save_library()
    print(f"✅ '{title}' added successfully!\n")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library()
            print(f"✅ '{title}' removed successfully!\n")
            return
    print("❌ Book not found!\n")

# Search for a book
def search_book():
    print("Search by: \n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    
    if choice not in ["1", "2"]:
        print("❌ Invalid choice! Try again.\n")
        return
    
    keyword = input("Enter search keyword: ").strip().lower()
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]

    if results:
        print("\n📖 Matching Books:")
        for i, book in enumerate(results, start=1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        print()
    else:
        print("❌ No matching books found!\n")

# Display all books
def display_books():
    if not library:
        print("📚 Your library is empty!\n")
        return

    print("\n📚 Your Library:")
    for i, book in enumerate(library, start=1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    print()

# Display statistics
def display_statistics():
    total_books = len(library)
    read_books = sum(book["read"] for book in library)
    percent_read = (read_books / total_books) * 100 if total_books else 0

    print(f"\n📊 Library Statistics:")
    print(f"📚 Total books: {total_books}")
    print(f"📖 Books read: {read_books} ({percent_read:.2f}% read)\n")

# Main menu
def main():
    while True:
        print("\n📚 Personal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("📁 Library saved to file. Goodbye! 🚀\n")
            break
        else:
            print("❌ Invalid choice! Please enter a number from 1 to 6.\n")

# Load existing library
library = load_library()

# Run the program
if __name__ == "__main__":
    main()
