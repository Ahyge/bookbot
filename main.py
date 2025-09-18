import sys
from stats import get_num_words, get_char_count, sorted_char


def get_book_text(filepath):
    with open(filepath, "r", encoding = "utf-8") as f:
        return f.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path =sys.argv[1]

    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error Could not find file '{book_path}'.")
        sys.exit(1)
    print(f"Analyzing book found at {book_path}")

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    char_counts = get_char_count(text)
    sorted_report = sorted_char(char_counts)
    
    for entry in sorted_report:
        ch = entry["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {entry['num']}")    
if __name__ == "__main__":
    main()

