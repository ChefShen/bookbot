def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    words = get_words(text)
    # print(len(words))
    char_dict_count = count_characters(text)
    # print(list(char_dict_count))

    #Report
    print(f"--- Begin report of {book_path}")
    print(f"{len(words)} words found in the document")
    print()

    list_of_char = get_char_list_sorted(char_dict_count)
    for item in list_of_char:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
    
def sort_on(d):
    return d["num"]

def get_char_list_sorted(char_dict_count):
    sorted_list = []
    for char in char_dict_count:
        sorted_list.append({"char": char, "num": char_dict_count[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    return text.split()

def count_characters(text):
    char_dict = {}

    for c in text.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict
        

main()