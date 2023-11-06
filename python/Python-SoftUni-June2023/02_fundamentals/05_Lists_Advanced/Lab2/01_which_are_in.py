seq1 = input().split(', ')
seq2 = input().split(', ')

output = list()

for s1 in seq1:
    for s2 in seq2:

        if s1 in s2 and s1 not in output:
            output.append(s1)


# output = [x for x in seq1 for y in seq2 if x in y]
# output = list(set(output))

print(output)
