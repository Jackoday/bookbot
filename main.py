def main():
    print("--- Begin report of books/frankenstein.txt ---")

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    print(f"{count} words found in the document\n")

    character_count = get_character_count(text)
    sorted_character_count = characters_dict_to_sorted_list(character_count)
    for character in sorted_character_count:
        if not character["char"].isalpha():
            continue
        print(f"The {character["char"]} character was found {character["num"]} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    characters = {}

    for c in text:
        lower = c.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1
    
    return characters

def sort_on(d):
    return d["num"]

def characters_dict_to_sorted_list(character_dict):
    sorted_list = []

    for ch in character_dict:
        sorted_list.append({"char": ch, "num": character_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

main()