import random
import string


def list_to_string(list):
    str1 = ""
    return str1.join(list)


print "Enter the length of password"
length_password = input()
while (length_password < 6):
    print "Length of password cannot be less than 6.  Reenter"
    length_password = input()
print "Enter no of letters"
length_letters = input()
print "Enter no of numbers"
length_numbers = input()
password = []
for i in range(1, length_letters + 1):
    password.append(random.choice(string.ascii_letters))
for i in range(1, length_numbers + 1):
    password.append(random.choice(string.digits))
length_special = 0
if len(password) < length_password:
    length_special = length_password - len(password)
for i in range(1, length_special + 1):
    password.append(random.choice(string.punctuation))
random.shuffle(password)
print "The generated password is ", list_to_string(password)
