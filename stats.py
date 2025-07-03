def count_words(file_contents):
        words = file_contents.split()
        wordcount = len(words)
        return wordcount

def count_characters(file_contents):
        characters_dict = {} 
        characters = file_contents.lower()
        for char in characters:
                if char in characters_dict:
                        characters_dict[char] += 1
                else:
                         characters_dict[char] = 1
        return characters_dict

def list_characters(characters_dict):
        character_list = []
        for characters in characters_dict:
                if characters.isalpha():
                        character_list.append({"char": characters, "num": characters_dict[characters]})
        character_list.sort(key=sort_on, reverse=True)
        return character_list
            
def sort_on(item):
        return item["num"]
        