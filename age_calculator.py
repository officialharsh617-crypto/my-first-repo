from datetime import datetime

def calculate_age(birth_year):
    current_year=datetime.now().year
    age=current_year-birth_year
    return age

#user input
birth_year=int(input("Enter your birth year:"))

#result
age=calculate_age(birth_year)
print(f"you are {age}year old")