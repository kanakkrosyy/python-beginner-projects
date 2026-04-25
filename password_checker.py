import string

pswd = input("enter the password : ")

strength = 0
feedback = []

#Length check 

common = ["123456", "password", "qwerty"]
if pswd.lower() in common:
    print("This is a very common password!")

#Length check 
elif len(pswd) >= 8 :
    strength += 1 

else : 
    feedback.append("password should atleast be 8 character")

#Uppercase check 

if any(char.isupper() for char in pswd) :
    strength += 1 

else :
    feedback.append("add an uppercase letter")
#Lowercase check 

if any(char.islower() for char in pswd) : 
    strength += 1 

else :
    feedback.append("add an lowercase letter")


if any(char.isdigit() for char in pswd) :
    strength += 1 

else : 
    feedback.append("add a number")

if any(char in string.punctuation for char in pswd) :
    strength += 1

else :
    feedback.append("add a special character")

print(f"Strength: {strength}/5")

if strength >= 2 :
    print("weak password")

elif strength >= 4 :
    print("medium password")

else :
    print("strong password")

# Show feedback
if feedback:
    print("\nSuggestions:")
    for f in feedback:
        print("-", f)