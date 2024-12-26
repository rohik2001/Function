# function defination /decclearation
def add(x,y):
     return x+y
def sub(x,y):
     return x-y
def mul(x,y):
     return x*y
def circle(r):
     pie=3.1416
     area=pie*r*r
     return area
def circle_curcumference(r):
     pie=3.1416
     area=2*pie*r
     return area

print("\nPlease Select operation")
print("a. add")
print("b. substract")
print("c. multiply")
print("d. devide")
choice=input("Select your option a/b/c/d : ").lower()
num1=int(input("Number 1 : "))
num2=int(input("Number 2 : "))
if choice=="a":
    print(num1,"+", num2, "=", add (num1,num2)) 
elif choice=="b":
    print(num1,"-", num2, "=", sub (num1, num2))
elif choice=="c":
     print(num1,"*", num2, "=", mul (num1, num2))


print("\nPlease Select operation")
print("1. circle")
print("2. rectangle")
print("3. circle curcumference")
print("4. rectangle curcumference")
choice2=int(input("Select your option 1/2/3/4: "))
r=float(input("Enter Radius: "))
if choice2=="1":
    print("Circle Area is: ", circle(r))
elif choice2=="2":
    print("Circle curcumference Area is: ", circle_curcumference(r))
