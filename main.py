from stats import get_num_words, count_letters, sort_characters
import sys


def formatted_print(filepath,wordcount,sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        print(f"{character["character"]}: {character["Count"]}")
    print("============= END ===============")
    return

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv[1])
    path = sys.argv[1]
    #path = "books/frankenstein.txt"
    book = get_book_text(path)
    words = get_num_words(book)
    #print(book)
    #print(f"{words} words found in the document")
    letters = count_letters(book)
    #print(letters)
    sorted_characters = sort_characters(letters)
    formatted_print(path,words,sorted_characters)
main()
