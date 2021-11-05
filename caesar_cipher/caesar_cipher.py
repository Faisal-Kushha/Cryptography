from nltk.corpus import words, names
import nltk
import re

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)


word_list = words.words()
name_list = names.words()

uppercase_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text_phrase, numeric_shift):
    """
    Encrypt function that takes in a plain text phrase and a numeric shift.
    """
    text = ''
    for char in plain_text_phrase:
        if char in uppercase_letter:
            character = (uppercase_letter.index(char) + numeric_shift) % 26
            text += uppercase_letter[character]
        elif char in lowercase_letter:
            character = (lowercase_letter.index(char) + numeric_shift) % 26
            text += lowercase_letter[character]
        elif char not in uppercase_letter and char not in lowercase_letter:
            character = re.sub(r'[^A-Za-z][^,.!?;:"@#$%*()-+=]', ' ', char)
            text += character
    return text


def decrypt(plain_text_phrase, numeric_shift):
    """
    Decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
    """
    return encrypt(plain_text_phrase, -numeric_shift)


def count_words(plain_text_phrase):
    """
    Counts the amount of english words in a string
    """
    words = plain_text_phrase.split()
    word_count = 0
    for i in words:
        clean_word = re.sub(r'[^A-Za-z][^,.!?;:"@#$%*()-+=]', ' ', i)
        if clean_word.lower() in word_list or clean_word in name_list:
            word_count += 1
    return word_count


def crack(plain_text_phrase):
    """
    Crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
    """
    text = ''
    for i in range(26):
        total_words = decrypt(plain_text_phrase, i)
        word_count = count_words(total_words)
        ratio = word_count / len(total_words.split())
        percentage = int(ratio * 100)
        if percentage > 50:
            text += total_words
    return text


if __name__ == "__main__":
    text1 = encrypt('It was the best of times, it was the worst of times.', 7)
    text2 = encrypt('it was the worst of times', 7)
    text3 = decrypt(text1, 7)
    text4 = decrypt(text2, 7)
    text_no_key1 = crack(text3)
    text_no_key2 = crack(text4)
    print(text1)
    print(text2)
    print(text3)
    print(text4)
    print(text_no_key1)
    print(text_no_key2)
