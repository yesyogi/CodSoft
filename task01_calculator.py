def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "can not divide by zero"
def calculator():
    while true :
            print("\nSIMPLE CALCULATOR MENU")
            print("1.add")
            print("2.subtract")
            print("3.multiply")
            print("4.divide")
            print("5.quit")

            choice=input("enter your choice(1-5):")
            if choice in['1','2','3','4']:
                num1=float(input("enter the 1st number:"))
                num2=float(input("enter the 2nd number:"))

                if choice=='1':
                    print(f"result:{add(num1,num2)}")
                elif choice=='2':
                    print(f"result:{sub(num1,num2)}")
                elif choice=='3':
                    print(f"result:{mul(num1,num2)}")
                elif choice=='4':
                    print(f"result:{divide(num1,num2)}")
                elif choice=='5':
                    print("exiting the calculator!")
                    break
                else:
                    print("invalid choice.kindly select a number between 1 and 5.")
if __name__=='__main__':   
        calculator()
