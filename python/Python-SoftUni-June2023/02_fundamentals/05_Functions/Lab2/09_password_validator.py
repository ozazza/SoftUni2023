def is_valid_password(s: str):
    not_valid_len = 'Password must be between 6 and 10 characters'
    not_only_letters_digits = 'Password must consist only of letters and digits'
    not_enough_digits = 'Password must have at least 2 digits'
    is_valid = 'Password is valid'
    output_errors = list()

    if len(s) < 6 or len(s) > 10:
        output_errors.append(not_valid_len)
    if not is_only_letters_and_digits(s):
        output_errors.append(not_only_letters_digits)
    if not is_two_digits(s):
        output_errors.append(not_enough_digits)

    if len(output_errors) > 0:
        return '\n'.join(output_errors)
    else:
        return is_valid


def is_only_letters_and_digits(s: str) -> bool:
    if not s.isalnum():
        return False
    return True


def is_two_digits(s: str) -> bool:
    count_digits = 0
    for n in s:
        if n.isdigit():
            count_digits += 1

    if count_digits < 2:
        return False
    else:
        return True


str_pass = input()
print(is_valid_password(str_pass))
