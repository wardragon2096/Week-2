side1=int(input("Enter first side of triangle: "))
side2=int(input("Enter the second side of the triangle: "))
side3=int(input("Enter the thrid side of the triangle: "))
if (side1*side1+side2*side2)==side3*side3 or (side1*side1+side3*side3)==side2*side2 or (side2*side2+side3*side3)==side1*side1:
          print("This triangle is a right angled triangle.")
else:
    print("This triangle is not a right angled triangle.")
