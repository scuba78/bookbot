def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    words = word_count(file_contents)
    letters = letter_count(file_contents)
    sorted = sort_letters(letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document\n")
    for i in sorted:
        print(f"The '{i["char"]}' character was found {i["num"]} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(string):
    words = string.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def letter_count(string):
    character_count= {}

    lower_string = string.lower()
    for i in range(0, len(lower_string)):
        character_count[lower_string[i]] = character_count.get(lower_string[i], 0) + 1
    return character_count

def sort_letters(dict):
    out_list = []
    for j in dict:
        if j.isalpha():
            out_list.append({"char":j, "num":dict[j]})
    out_list.sort(reverse=True, key=sort_on)
    return out_list

main()


