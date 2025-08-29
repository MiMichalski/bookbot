def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text_to_analyse):
    words = text_to_analyse.split()
    return len(words)

def get_char_count(text_to_analyse):
    letters = {}
    text_to_analyse = text_to_analyse.lower()

    for letter in text_to_analyse:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

    return letters

def dictionary_to_sorted_list(dictionary):
    record_list = []
    for record in dictionary:
        local_record = {"char": record, "num": dictionary[record]}
#        print(local_record)
        record_list.append(local_record)

    record_list.sort(reverse=True, key=sort_on)
#    print(record_list)     
    return record_list

def sort_on(items):
    return items["num"]
