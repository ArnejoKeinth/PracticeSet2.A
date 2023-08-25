
# FUNCTION 1
def heron_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the length of side 'b': "))
c = float(input("Enter the length of side 'c': "))

triangle_area = heron_area(a, b, c)
print(f"The area of the triangle is: {triangle_area}")


# FUNCTION 2
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Taking user input for the year
user_input = int(input("Enter a year: "))

if is_leap_year(user_input):
    print(f"{user_input} is a leap year.")
else:
    print(f"{user_input} is not a leap year.")
