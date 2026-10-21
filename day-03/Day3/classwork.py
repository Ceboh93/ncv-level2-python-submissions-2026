from datetime import date

#capture a name
name = input("Please enter your name: ")
#capture the year of birth
year_born = input("Please enter the year you were born in: ")

age = 2026 - int(year_born)

print(name, "is", age)
today = date.today()

print(today.year)

#order of precedence
print(60 + 80 / 2)
print((60 + 80) / 2)

