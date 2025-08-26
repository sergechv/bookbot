def get_num_words(file):
    with open(file) as f:
        file_contents = f.read()
        words = file_contents.split()
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file}")
        print("----------- Word Count ----------")
        print(f"Found {len(words)} total words")

char_dict = {}

def get_num_char(file):
    with open(file) as f:
        file_contents = f.read()
        characters = list(file_contents.lower())
        for character in characters:
            if character in char_dict:
                char_dict[character] += 1
            else:
                char_dict[character] = 1
        return char_dict

def sort_dict(char_dict):
    def sort_on(items):
        return items["num"]

    chars = []
    for c in char_dict:
        result = {"char": c, "num": char_dict[c]}
        chars.append(result)

    chars.sort(reverse=True, key=sort_on)

    print("--------- Character Count -------")
    for c in chars:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")
