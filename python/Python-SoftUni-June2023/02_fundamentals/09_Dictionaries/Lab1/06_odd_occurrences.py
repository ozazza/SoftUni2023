words = input().lower().split()

odd_occurrences = [x for x in words if words.count(x) % 2 != 0]
unique_words = list(dict.fromkeys(odd_occurrences))

# print(f"odd_occ: {odd_occurrences}")
# print(f"dict: {dict.fromkeys(odd_occurrences)}")
# print(f"unique list: {unique_words}")

print(' '.join(unique_words))
