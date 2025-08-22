# Function to count number of words.    
def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

# Function to count character usage.
def char_count(book_text):
    # Convert text to lower case.
    book_text = book_text.lower()
    # Initialize empty dictionary to store character counts.
    count = {}
    # Iterate over each character in the text.
    for char in book_text:
            if char.isalpha():
                  if char in count:
                    count[char] += 1
                  else:count[char] = 1
        
           
    
    return count
    

# Function to sort character usage.
def sort_char(character_count):
    # Convert dictionary to a list  of dictionaries with "char" and "num" keys.
    sorted_list = [{"char": k, "num": v} for k, v in character_count.items()]
    # Sort the list by "num" (count) in descending order.
    sorted_list.sort(key=lambda x: x["num"], reverse = True)

    return sorted_list