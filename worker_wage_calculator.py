print("\n~~~Welcome to the Worker Wage Calculator Program~~~\n\n")

str_length = input("please type Length : \n")
str_width = input("please type width : \n")
wage = input("How much for 1 meter? \n")

length = float(str_length)
width = float(str_width)

float_erea = length * width
float_worker_wage = float(wage) * float_erea

erea = str(float_erea)
worker_wage = str(float_worker_wage)

print("The total area is: " + erea)
print ("Give the guy : " + "$" + worker_wage)