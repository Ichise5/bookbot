def word_count(user_string:str) -> int:
    """Counts words of the user_string string type variable.

    Args:
        user_string (str): input string.

    Returns:
        int: number of words in the string separated by space.
    """
    words = user_string.split()
    return len(words)

def char_count(user_string:str) -> dict:
    """Counts number of individual letters of input user_string string type variable.

    Args:
        user_string (str): input string.

    Returns:
        dict: dictionary of number of individual letters
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_dict = {x:0 for x in letters}

    for character in user_string.lower():
        try:
            letter_dict[character] += 1
        except KeyError:
            continue
    return letter_dict

def report(book_name: str, num_words:int, num_letters: dict, relative_letters: dict) -> None:
    """Function to create a report to command line.

    Args:
        book_name (str): name of the file/book that is analysed.
        num_words (int): number of words.
        num_letters (dict): number of letters 
    """
    rep = [f"--- Begin report of books: {book_name} ---"]
    rep.append(f"{num_words} words were found in the document.")
    rep.append("")
    for letter in num_letters:
        rep.append(f"The '{letter}' character was found {num_letters[letter]} times with relative frequency {100*relative_letters[letter]:0.2f}%.")
    rep.append("--- End of report ---")

    print("\n".join(rep))

def relative_frequency(letters:dict):
    english_letters = {
        "a":  8.167e-2,
        "b":  1.492e-2,
        "c":  2.782e-2,
        "d":  4.253e-2,
        "e": 12.702e-2,
        "f":  2.228e-2,
        "g":  2.015e-2,
        "h":  6.094e-2,
        "i":  6.966e-2,
        "j":  0.153e-2,
        "k":  0.772e-2,
        "l":  4.025e-2,
        "m":  2.406e-2,
        "n":  6.749e-2,
        "o":  7.507e-2,
        "p":  1.929e-2,
        "q":  0.095e-2,
        "r":  5.987e-2,
        "s":  6.327e-2,
        "t":  9.056e-2,
        "u":  2.758e-2,
        "v":  0.978e-2,
        "w":  2.360e-2,
        "x":  0.150e-2,
        "y":  1.974e-2,
        "z":  0.074e-2
    }
    
    sum_letters = 0
    rel_letters = dict()
    rel_diff = dict()
    for letter in letters:
        sum_letters+= letters[letter]
        rel_letters[letter] = letters[letter]
    
    diff_letters = dict()
    for letter in letters:
        rel_letters[letter] /= sum_letters
        diff_letters[letter] = rel_letters[letter] - english_letters[letter]
        rel_diff[letter] = diff_letters[letter] / english_letters[letter]

    return rel_letters, diff_letters, rel_diff
    pass

###% Main program 
file = 'frankenstein.txt'
with open(f"books/{file}") as f:
    file_contents = f.read()

words = word_count(file_contents)
letters = char_count(file_contents)
freq_letters = dict(sorted(letters.items(), key =lambda x: x[1], reverse=True))
relative_letters, diff_letters, rel_diff = relative_frequency(freq_letters)
#print(letters)
#print(freq_letters)
report(file, words, freq_letters, relative_letters)
print(diff_letters)
print(rel_diff)