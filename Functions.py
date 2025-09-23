import math
#Function for area of circle
def circle_area(radius):
    area = math.pi * radius ** 2
    return area

r = float(input("Enter the radius of the circle: "))
result = circle_area(r)
print(result)

#Function to calculate money due
def total_due(money, tax_rate):
    total = money + (money * tax_rate)
    return total

money = float(input("Enter the amount of money: "))
tax_rate = float(input("Enter the tax rate: "))
result = total_due(money, tax_rate)
print(result)



#Function converts Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Enter the fahrenheit: "))
result = fahrenheit_to_celsius(fahrenheit)
print(result)