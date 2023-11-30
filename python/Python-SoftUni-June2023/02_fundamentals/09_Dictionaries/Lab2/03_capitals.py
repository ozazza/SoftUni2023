countries = input().split(', ')
capitals = input().split(', ')

country_capital = {countries[index]: capitals[index] for index in range(len(capitals))} # any of countries or capitals

for country, capital in country_capital.items():
    print(f'{country} -> {capital}')
