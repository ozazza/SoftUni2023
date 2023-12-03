def word_is_min_3_chars(word: str) -> bool:
    if len(word) >= 5:
        return True
    return False


def word_is_surrounded_by(symbol: str, word: str) -> bool:
    if symbol in word:
        if word[0] == symbol and word[-1] == symbol:
            return True
    return False


def word_contains_symbol(symbol: str, word: str) -> bool:
    if symbol in word:
        return True
    return False


def string_has_min_len(string: str, number: int) -> bool:
    clean_str = string[1:len(string)-1]
    if len(clean_str) >= number:
        return True
    return False


def string_starts_with_upper_others_are_lower(string: str) -> bool:
    clean_str = string[1:len(string) - 1]
    if clean_str[0].isupper() and clean_str[1:len(clean_str)].islower():
        return True
    return False


def string_is_alphabetical(string: str) -> bool:
    clean_str = string[1:len(string) - 1]
    if clean_str.isalpha():
        return True
    return False


def is_valid_string_command(string) -> bool:
    string1, string2 = string.split(":")

    if word_is_min_3_chars(string1) \
            and word_is_surrounded_by('!', string1) \
            and word_contains_symbol(':', string) \
            and string_has_min_len(string2, 8) \
            and string_starts_with_upper_others_are_lower(string1)\
            and string_is_alphabetical(string2):
        return True
    return False


n = int(input())

for i in range(n):
    command = input()
    symbols_ascii = []

    if is_valid_string_command(command):
        str1, str2 = command.split(':')

        clean_1 = str1[1:len(str1) - 1]
        clean_2 = str2[1:len(str2) - 1]

        for ch in clean_2:
            symbols_ascii.append(ord(ch))

        result = [str(x) for x in symbols_ascii]
        print(f'{clean_1}: {" ".join(result)}')

    else:
        print('The message is invalid')
