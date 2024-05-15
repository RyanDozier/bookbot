def main():
    file_path = "books/frankenstein.txt"
    content = get_text(file_path)
    number_of_words = how_many_words(content)
    all_letters = find_letters(content)
    all_letters_sorted = dict(sorted(all_letters.items()))
    print_report(all_letters_sorted, number_of_words, file_path)

def get_text(file):
    with open(file) as f:
        file_content = f.read()
    return file_content

def how_many_words(text):           #Function that counts how many words in text
    all_the_words = text.split()    #Split text by white space into a list
    words = len(all_the_words)      #How many items in list (words)
    return words                    #Print how many words

def find_letters(string):
    alphabet = ('a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z') 
    lower_string = string.lower()
    letters = {}

    for letter in lower_string:
        if letter in alphabet and letter not in letters:
            letters[letter] = 1
        elif letter in alphabet and letter in letters:
            letters[letter] += 1
    return letters

def print_report(sort_dict, word_count, path_to_file):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"There are {word_count} words.\n")
    for alpha, num in sort_dict.items():
        print(f"There are {num} {alpha}\'s in this document.")
    print("--- End report ---")

 
          
main()