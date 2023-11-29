count_words = int(input())

synonyms_dict = {}

for i in range(count_words):
    word = input()
    synonym_word = input()

    if word in synonyms_dict.keys():
        synonyms_dict[word].append(synonym_word)
    else:
        synonyms_dict[word] = [synonym_word]

for k, v in synonyms_dict.items():
    list_value = ', '.join(v)
    print(f'{k} - {list_value}')
