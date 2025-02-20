'''
@author:tahacolak

'''
#Question1
stuName=input("Please enter your name: ")
print(f"Hello {stuName} ")

stuID=input("Please enter your Student ID: ")
print(f"ID: {stuID}")

#Question2
var1=float(input("First variable: "))
var2=float(input("Second variable: "))

sum=var1+var2
diff=var1-var2
prod=var1*var2

if(diff<0):
    print("Please takes difference reversedly!")

else:
    print(f"Difference = {diff}")

print(f"{var1} + {var2}={ sum}")
print(f"{var1} * {var2}= { prod}")

#Question3
studentName=input("Please enter student name: ")
labGrade=float(input("Enter Lab Grade: "))
midtermGrade=float(input("Enter Midterm Grade: "))
finalGrade=float(input("Enter Final Grade: "))

generalScore=labGrade/4+midtermGrade*35/100+finalGrade*2/5

print(f"Name: {studentName}")
print(f"ID: {stuID}")
print(f"Lab:{labGrade}")
print(f"Midterm:{midtermGrade}")
print(f"Final: {finalGrade}")

#Question4


