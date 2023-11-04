def sequence_min_max_sum(sequence) -> str:
    min_s = min(sequence)
    max_s = max(sequence)
    sum_s = sum(sequence)

    out_min = f'The minimum number is {min_s}'
    out_max = f'The maximum number is {max_s}'
    out_sum = f'The sum number is: {sum_s}'

    output_line_str = f'{out_min},{out_max},{out_sum}'
    multi_output = '\n'.join(output_line_str.split(','))

    return multi_output


numbers = input().split(' ')
nums = [int(x) for x in numbers.copy()]

print(sequence_min_max_sum(nums))
