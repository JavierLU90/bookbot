def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def get_sorted_characters(char_dict):
    return dict(sorted(char_dict.items(), key=lambda x: int(x[1]), reverse=True))
