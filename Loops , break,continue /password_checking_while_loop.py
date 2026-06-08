#Write a program that keeps asking the user to enter a password until they enter the correct one.
password = "vivek123"

entered_pass = input("enter the password : ")
while(entered_pass != password):
    entered_pass = input("wrong password! try again and enter password : ")

print("succes ! You are logged in")
