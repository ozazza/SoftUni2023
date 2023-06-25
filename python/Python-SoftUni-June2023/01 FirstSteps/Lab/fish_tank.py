length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume = length * width * height / 1000
free_volume = volume - (volume * percent)

print(free_volume)