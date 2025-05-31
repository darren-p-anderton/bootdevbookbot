from stats import print_book_analysis
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print_book_analysis(sys.argv[1])
main()
