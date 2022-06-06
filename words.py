def print_upper_words(string_word, must_start_with):
    '''This function is to convert letters to all uppercase'''
    
    for char in string_word:
        for must in must_start_with:
            if char.startswith(must):
                print(char.upper())
                


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})