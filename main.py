import sys
from stats import get_num_words
from stats import get_num_char
from stats import sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    get_num_words(sys.argv[1])
    result = get_num_char(sys.argv[1])
    sort_dict(result)
main()

