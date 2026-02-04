print("DSA tutorials")

# simple function
def greet_user(name: str):
    print(f'{name.capitalize()}, welcome to our python tutorials')
    print(f'Hey there {name.capitalize()}')

def calculate_age(birth_year: int, birth_month: int, birth_day: int):
    from datetime import date
    today = date.today()
    age = today.year - birth_year
    # Adjust if birthday hasn't occurred this year yet
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1
    return age

# Example usage:
print(f"Age: {calculate_age(1990, 5, 15)}")

greet_user('marvin')
   