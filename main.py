def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    frankenstein = file_contents.split()
    total_word_count = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_count = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

    for word in frankenstein:
        
        total_word_count += 1

        if "a" in word.lower():
            letter_count['a'] += 1
        if "b" in word.lower():
            letter_count['b'] += 1
        if "c" in word.lower():
            letter_count['c'] += 1
        if "d" in word.lower():
            letter_count['d'] += 1
        if "e" in word.lower():
            letter_count['e'] += 1
        if "f" in word.lower():
            letter_count['f'] += 1
        if "g" in word.lower():
            letter_count['g'] += 1
        if "h" in word.lower():
            letter_count['h'] += 1
        if "i" in word.lower():
            letter_count['i'] += 1
        if "j" in word.lower():
            letter_count['j'] += 1
        if "k" in word.lower():
            letter_count['k'] += 1
        if "l" in word.lower():
            letter_count['l'] += 1
        if "m" in word.lower():
            letter_count['m'] += 1
        if "n" in word.lower():
            letter_count['n'] += 1
        if "o" in word.lower():
            letter_count['o'] += 1
        if "p" in word.lower():
            letter_count['p'] += 1
        if "q" in word.lower():
            letter_count['q'] += 1
        if "r" in word.lower():
            letter_count['r'] += 1
        if "s" in word.lower():
            letter_count['s'] += 1
        if "t" in word.lower():
            letter_count['t'] += 1
        if "u" in word.lower():
            letter_count['u'] += 1
        if "v" in word.lower():
            letter_count['v'] += 1
        if "w" in word.lower():
            letter_count['w'] += 1
        if "x" in word.lower():
            letter_count['x'] += 1
        if "y" in word.lower():
            letter_count['y'] += 1
        if "z" in word.lower():
            letter_count['z'] += 1
        
    print("--- Begin report of books/frankenstein,txt ---")
    print(f"{total_word_count} words found in the document\n\n")
    
    for letter in alphabet:
        print(f"The {letter} character was found {letter_count[letter]} times")
    
    print("--- End report ---")
    
    
main()