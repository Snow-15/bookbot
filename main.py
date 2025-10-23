from stats import get_num_words, count_characters, sort_char_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    contents = get_book_text(sys.argv[1])
    num_words = get_num_words(contents)
    sorted_char_counts = sort_char_counts(count_characters(contents))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in sorted_char_counts:
        if not dict["char"].isalpha():
            continue

        print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


main()
