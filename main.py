from stats import count_words, char_count, sort_char

# Function to read and return the contents of a file as a string
def get_book_text(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return None


# Main function to use get_book_text and print the contents
def main():
    # Relative path to frankenstein.txt
    file_path = "./books/frankenstein.txt"
    # Get the book text using the get_book_text function
    book_text = get_book_text(file_path)
    # Count the number of words in the book text.
    word_count = count_words(book_text)
    # Count the occurences of each character in the book.
    count = char_count(book_text)
    # Sort the character counts by descending order.
    sorted_char_counts = sort_char(count)
    
    # Check if the book text was successfully retrieved and print it
    if book_text is not None:
        print(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print(f"----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print(f"--------- Character Count -------")
        for item in sorted_char_counts:
            print(f"{item['char']}: {item['num']}")
        print("============= END ================")


# Call the main function to execute the program
if __name__ == "__main__":
    main()
