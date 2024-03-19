#defined variables 
sideA=int(input("Enter side A: "))
sideB=int(input("Enter side B: "))
sideC=int(input("Enter side C: "))
sideD=int(input("Enter side D: "))
sideE=int(input("Enter side E: "))

#math statements for then new 2 variables
shape1= (sideA * sideB)

shape2 = (sideD - sideB - sideE) * (sideA - sideC)
#New variable called Triangle (Another shape besides the 2 other from before )
#calling the 2 variables rect1 and rect2 to substract side A and side c then
#multiply the result of those 2 for side E and multiply that result by 0.5 
triangle = (sideA - sideC) * sideE * 0.5
#calling the whole program to output te result of Room Area 
print("Room Area: " + str(shape1+ shape2+triangle))
