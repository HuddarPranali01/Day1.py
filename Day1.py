'''
# program to declare variables to store rno,name,fees
rno=123
name="pranali"
fees=5000
is_active=True
print("----student details----")
print("Roll number", rno)
print("Name",name)
print("fees",fees)
print("is active",is_active)
#type function is used to check the datatype
print(type(name))
print(type(fees))
print(type(is_active))
'''
'''
#input function is used to accept input from the user, by default input func string 
rno=int(input("enter roll number"))
name=input("enter name")
fees=float(input("enter fees amount"))
is_active=bool(input("enter True or False of is active"))
'''
'''
#multiple variables in one line
n1,n2,n3=10,20,30
print(f"num1 : {n1}, num2 : {n2}, num3 : {n3}")
'''
'''
n1 = "14"
n2 = "22"
result = int(n1) + int(n2)
print(f"Result : {result}")
 

# converting input to boolean
# convert input to a bollean (eg. for yes/no questions)
 
is_student=input("Are you a student? (yes/no): ").lower()=="yes"
print("Student status:", is_student) #output : student status: True
if input is "yes" 
is_active=bool(input("enter True or False for student"))
'''
'''
#accept multiple inputs
#split input string to accept multiple values.
x, y = input("Enter two numbers (separated by space): ").split()
print(f"x = {x}, y = {y}")

n1,n2,n3 = input ("Enter three numbers (separated by space): ").split()
print (f"n1 = {n1}, n2 = {n2}, n3 = {n3} ")
total= int(n1) + int(n2) + int(n3)
print(f"Total :{total}")
'''
'''
#program to accept len and  bre in same line and print area
len,bred = input("Enter numbers(separated by space) :").split()
print(f"len = {len}, bred = {bred}")
area = float(len) * float(bred)
print(f"Area : {area}")
'''

'''
#program to accept 5 subject marks in same line and print total and per 
m1,m2,m3,m4,m5 =input("Enter subject marks: ").split()
print(f"m1={m1}, m2={m2}, m3={m3}, m4={m4}, m5={m5}")
total=int(m1)+int(m2)+int(m3)+int(m4)+int(m5)
percentage=(total/500)*100
print(f"Total : {total}")
print(f"Percentage : {percentage}")
'''

#program to accept empno, empname,designation and salary in same line
empno,empname,designation,salary = input("Employee number,name,designation and salary:").split()
print(f"Employee Number : {empno}")
print(f"Employee Name : {empname}")
print(f"Designation : {designation}")
print(f"Salary : {salary}")



           
        
