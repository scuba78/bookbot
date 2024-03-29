def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    print(file_contents)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()


