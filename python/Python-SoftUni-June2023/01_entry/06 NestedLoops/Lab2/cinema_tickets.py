# Input
movie = ''

# Logic
movie_name = ''
total_tickets = 0
total_students = 0
total_standard = 0
total_kids = 0
while movie != 'Finish':

    movie = input()
    if movie == 'Finish':
        break

    movie_name = movie
    available_places = int(input())
    count_students = 0
    count_standard = 0
    count_kids = 0
    sold_tickets = 0
    movie_full_percent = 0

    for i in range(available_places):
        ticket_type = input()

        if ticket_type == 'End':
            break

        if ticket_type == 'student':
            count_students += 1
        elif ticket_type == 'standard':
            count_standard += 1
        elif ticket_type == 'kid':
            count_kids += 1

        sold_tickets = i + 1

    movie_full_percent = sold_tickets / available_places * 100
    total_students += count_students
    total_standard += count_standard
    total_kids += count_kids
    total_tickets += sold_tickets

    print(f'{movie_name} - {movie_full_percent:.2f}% full.')

# Output
print(f'Total tickets: {total_tickets}')
print(f'{(total_students / total_tickets * 100):.2f}% student tickets.')
print(f'{(total_standard / total_tickets * 100):.2f}% standard tickets.')
print(f'{(total_kids / total_tickets * 100):.2f}% kids tickets.')
