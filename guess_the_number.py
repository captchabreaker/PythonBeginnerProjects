import random
random_number=random.randrange(0,21,1)
input_number=input("Enter a number between 0 to 20\n")

if input_number==random_number:
    print "Number found "
elif input_number<random_number:
    print "You entered a smaller number"
elif input_number>random_number:
    print "You entered a large number"