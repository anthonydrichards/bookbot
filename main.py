def read_file(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents):    
        words = file_contents.split()
        print(f"{len(words)} words found in the document")

def count_characters(file_contents):    
    character_count = {}
    for character in file_contents:          
        character_count[character.lower()] = character_count.get(character.lower(), 0) + 1
    character_array = []
    for character in character_count.keys():
        if character.isalpha():
            character_array.append({"character": character, "count": character_count[character]})
            
    def sort_on(dict):
        return dict["count"]
    
    character_array.sort(key=sort_on, reverse=True)
    for sorted_character in character_array:
        print(f"The '{sorted_character["character"]}' character was found {sorted_character["count"]} times")

def main():
    file_contents = read_file("books/frankenstein.txt")
    count_words(file_contents)
    print("")
    count_characters(file_contents)

main()