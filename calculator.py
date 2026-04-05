#calculator
num = int(input("Enter a number :  "))
num2 = int(input ("Enter another number : "))
ops = ("  *  , +  , - , / , //") 
choice = (input("Enter your operation :  *  , +  , - , / , // : "))

if choice  ==  "*"  :
   print (num*num2) 
    
elif choice  == "+":
        print (num + num2)  

elif choice == "-":
            print (num - num2)

elif choice == "/" :
       print(num/num2)

elif choice == "//" :
       print(num//num2)

else : 
     print ("not valid")