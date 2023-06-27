hall_length = float(input())
hall_width = float(input())

corridor_width = 1
student_width = 0.7
student_length = 1.2

lector_width = 1.2
lector_length = 1.6

lost_places = 3

places_by_length = hall_length // student_length
places_by_width = (hall_width - corridor_width) // student_width
available_places = places_by_length * places_by_width - lost_places

print(available_places)
