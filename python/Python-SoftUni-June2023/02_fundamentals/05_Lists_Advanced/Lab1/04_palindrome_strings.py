words = input()
palindrome = input()

found_palindromes = [x for x in words.split() if x == x[::-1]]
count_occurrences = found_palindromes.count(palindrome)

print(found_palindromes)
print(f'Found palindrome {count_occurrences} times')
