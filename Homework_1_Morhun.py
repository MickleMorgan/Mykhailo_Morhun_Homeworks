def Task1_Printer_Hello_World():
    print('Hello, world')

def Task2_Printer_three_any():
    print("What's up, world")
    print('Aloha, World')
    print('Hola, World')

def Task3_Area_of_Rectangle():
    length = int(input('Length of rectangle ='))
    width = int(input('Width of rectangle ='))
    area_rectangle = length * width
    print ("Area of rectangle = ", area_rectangle, "cm2")

def Task4_Basic_Math():
    number_1 = int(input('Please, put Number 1: '))
    number_2  = int(input('Please, put Number 2: '))
    summary = number_1 + number_2
    product = number_1 * number_2
    difference = number_1 - number_2
    quotient = number_1 / number_2
    print("Summ of numbers = ", summary )
    print("Product of numbers = ", product)
    print("Difference of numbers = ", difference)
    print("Quotient of numbers = ", quotient)

def Task5_Circle_calculation():
    radius = float(input('Radius pf the circle in cm ='))
    pi = 3.14159
    diameter = radius * 2
    circumference = diameter * pi
    area = pi * (radius ** 2)
    print("Circle diameter = ",diameter, "cm" )
    print("Circle circumference = ", circumference, "cm")
    print("Circle area = ", area, "cm2")

Task1_Printer_Hello_World()
Task2_Printer_three_any()
Task3_Area_of_Rectangle()
Task4_Basic_Math()
Task5_Circle_calculation()










