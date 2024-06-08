import string
from collections import Counter

def main():
    # Read the file contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Split the contents into words
    frankenstein = file_contents.split()
    
    # Initialize total word count
    total_word_count = len(frankenstein)
    
    # Initialize letter count dictionary
    letter_count = Counter()

    # Count the letters in each word
    for word in frankenstein:
        for letter in word.lower():
            if letter in string.ascii_lowercase:
                letter_count[letter] += 1

    # Print the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_word_count} words found in the document\n\n")
    
    for letter in string.ascii_lowercase:
        print(f"The {letter} character was found {letter_count[letter]} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    main()
