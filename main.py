from stats import count_words, count_characters, sort_characters_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    file_content = get_book_text(filepath)
    word_count = count_words(file_content)
    dicts = count_characters(file_content)
    # sorted_dict = sort_characters_dictionary(dict)

    s = f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""
    print(s)
    
    for dict in dicts:
        for val in dict:
            char = dict["char"]
            num = dict["num"]
            
            if char.isalpha():
                print(f"{char}: {num}")
    
    print("============= END ===============")
    
main()