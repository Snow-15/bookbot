def get_num_words(contents):
    return len(contents.split())


def count_characters(contents):
    character_counts = {}

    for char in contents.lower():
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts
            

def sort_char_counts(char_counts):
    list_char_counts = []

    for char, num in char_counts.items():
        list_char_counts.append({"char": char, "num": num})
        
    list_char_counts.sort(reverse=True, key=lambda word: word["num"])

    return list_char_counts
