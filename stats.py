
def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
    return book_text

def get_word_count(count_string):
    word_list = count_string.split()
    count = 0
    for word in word_list:
        count += 1
    return count

def get_char_count(char_string):
    char_dict = {}
    for char in char_string.lower():
        if not char in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict

def sort_on(this_dict):
    return this_dict["count"]

def sort_dict(this_dict):
    dict_list = []
    for c, v in this_dict.items():
        dict_list.append({"char": c, "count": v})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def print_book_analysis(filepath):
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for count in sorted_char_count:
        if count["char"].isalpha():
            print(f"{count['char']}: {count['count']}")
    print("============= END ===============")
