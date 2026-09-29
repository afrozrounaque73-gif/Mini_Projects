num1 = float(input("Enter 1st number : ")) #type conversion
num2 = float(input("Enter 2nd number : ")) #type conversion

print("Choose what you want : \n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Remainder\n6. Exponential(Power)")

select = int(input("What is your choice(number only) :"))

# function definition
def Addition(num1, num2 ):
    print(f"Sum is {num1 + num2}")
    
def Substraction(num1, num2 ):
    print(f"Sub is {num1 - num2}")
    
def Multiplication(num1, num2 ):
    print(f"Product is {num1 * num2}")
    
def Division(num1, num2 ):
    print(f"Division is {num1 / num2}")
    
def Remainder(num1, num2 ):
    print(f"Remainder is {num1 % num2}")
    
def Power(num1, num2 ):
    print(f"Power is {num1 ** num2}")   
    
#logic

if(select == 1):
    Addition(num1, num2) #function call
elif(select == 2):
    Substraction(num1, num2)  
elif(select == 3):
    Multiplication(num1, num2) 
elif(select == 4):
    Division(num1, num2) 
elif(select == 5):
    Remainder(num1, num2) 
elif(select == 6):
    Power(num1, num2) 
else:
    print("Abe bewde shii number daal!")                      
                     

