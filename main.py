def word_count(user_string:str) -> int:
    words = user_string.split()
    return len(words)

def char_count(user_string:str) -> dict:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_dict = {x:0 for x in letters}

    for character in user_string.lower():
        try:
            letter_dict[character] += 1
        except KeyError:
            continue
    return letter_dict

def report(book_name: str, num_words:int, num_letters: dict) -> None:
    rep = [f"--- Begin report of books: {book_name} ---"]
    rep.append(f"{num_words} were found in the document.")
    rep.append("")
    for letter in num_letters:
        rep.append(f"The '{letter}' character was found {num_letters[letter]} times")
    rep.append("--- End of report ---")

    print("\n".join(rep))


###% Main program 
file = 'frankenstein.txt'
with open(f"books/{file}") as f:
    file_contents = f.read()

words = word_count(file_contents)
letters = char_count(file_contents)
freq_letters = dict(sorted(letters.items(), key =lambda x: x[1], reverse=True))
print(letters)
print(freq_letters)
report(file, words, freq_letters)