def is_palindrome(n: str) -> bool:
    if n == n[::-1]:
        return True
    else:
        return False


def check_sequence_if_palindromes(sequence: list):
    for i in sequence:
        print(is_palindrome(i))


nums = input().split(', ')
check_sequence_if_palindromes(nums)
