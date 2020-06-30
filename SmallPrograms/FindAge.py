from datetime import date

y=date.today().year

birth_year= input('whats your year of birth?')

age= y-int(birth_year)
print(age)