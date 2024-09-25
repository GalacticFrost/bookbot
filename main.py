def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    total_word_count = len(words)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_count = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

    for word in words:
        for letter in word.lower():
            if letter in alphabet:
                letter_count[letter] += 1
        
    print("--- Report of book: frankenstein.txt ---\n")
    print(f"{total_word_count} words found in the document\n")
    
    for letter in alphabet:
        print(f"The {letter} character was found {letter_count[letter]} times")
    
    print("\n--- End of report ---")
    
main()
