#Find the Circumference, area, and volume of a radius of 2.75 of a circle and sphere

r=input("enter the radius:")
r=float(r)

Circum=2*3.14159*r
Area=3.14159*r**2
Volume=4/3*3.14159*r**3

print("The circumference of a circle with a radius", r , "is" , Circum)
print("The area if a circle with a radius", r , "is" , Area)
print("The volume of a sphere with a radius", r , "is" , Volume)
