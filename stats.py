import string

def key_to_sort(e):
     return e["Count"]

def get_num_words(book_contents):
    result = len(book_contents.split())
    return result

def count_letters (book_contents):
    lowered_contents = book_contents.lower()
    results = {}
    for character in lowered_contents:
        if character not in results and character.isalpha():
            results[character] = lowered_contents.count(character)
    return results

def sort_characters(characters):
    results = []
    for character in characters:
            results.append(
                {"character":character,
                "Count":characters[character]})
    results.sort(key=key_to_sort,reverse=True)
    return results
