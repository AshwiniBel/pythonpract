import enum
class Country(enum.IntEnum):
    Afghanistan = 93
    Albania = 100
    Algeria = 34
    Andorra = 56
country_code_list = list(map(int, Country))
print(country_code_list)
print('Country Names ordered by country code')
print('\n'.join('  ' + c.name for c in sorted(Country)))


