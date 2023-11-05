def repeat_string(sentence: str, repeat_times: int):
    result = ''
    for _ in range(repeat_times ):
        result += sentence

    return result


repeat = input()
times_repeated = int(input())

print(repeat_string(repeat, times_repeated))
