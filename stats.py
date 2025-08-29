def count_words(file_contents):
    return len(file_contents.split())

def count_characters(file_contents):
    file_contents_lower = file_contents.lower()
    dictionaries = []
    for c in set(file_contents_lower):
        character_count = {
            "char": c,
            "num": file_contents_lower.count(c)
        }
        
        dictionaries.append(character_count)
        
    return dictionaries

def sort_on(items):
    return items["num"]

def sort_characters_dictionary(character_dict):
    sorted_character_dict = character_dict.sort(reverse=True, key=sort_on)
    return sorted_character_dict
        