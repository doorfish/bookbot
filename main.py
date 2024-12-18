def main():
    path = 'books/frankenstein.txt'
    text = read_text(path)
    counter = word_count(text)
    char = character_count(text)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{counter} words found in the document\n')
    sort_on(char)
    print('--- End report ---')

def read_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    text = text.lower()
    character = {}
    for letter in text:
        if letter in character:
            character[letter] += 1
        else:
            character[letter] = 1
    return character

def sort_on(text):
    sorted_order = dict(sorted(text.items(), key=lambda item: item[1], reverse=True))
    for key in sorted_order:
        if key.isalpha():
            print(f"The '{key}' character was found {sorted_order[key]} times")



main()