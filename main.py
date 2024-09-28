def main():
    book_path = "/home/ericsignal/workspace/github.com/Signal46/bookbot/books/frankenstein.txt"
    # book_path = "github.com\\Signal46\\bookbot\\books"
    text = get_book_text(book_path)
    num_words = get_num_words(text)    
    found_letters = get_num_unique_characters(text)
    sorted_letters = sort_letters_by_frequency(found_letters)
    write_report(num_words, sorted_letters)
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_unique_characters(text):
    found_letters = {}
    for character in text.lower():
        if character.isalpha():
            found_letters[character] = found_letters.get(character, 0) + 1
    return found_letters

def write_report(num_words_found, sorted_found_letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words_found} words found in the document")
    print("")
    for letter, count in sorted_found_letters:
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def sort_letters_by_frequency(found_letters):
    return sorted(found_letters.items(), key=lambda x: x[1], reverse=True)

main()
