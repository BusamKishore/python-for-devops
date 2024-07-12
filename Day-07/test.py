import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Ok, will create the instance for you")

else:
    print("your input not maching, so we can't create")

print("*****************************")

import sys

type = sys.argv[1]

if type == "t2.micro":
    print("It will charge 2 dollars per a day")

elif type == "t2.medium":
    print("It will charge 6 dollars per a day")

elif type == "t2.xlarge":
    print("It will charge 8 dollars per a day")

else:
    print("Please provide suitable instace")

print("==================================")

