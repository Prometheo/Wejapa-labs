#For the following practice question you will need to write code in Python in the workspace below. This will allow you to practice the concepts discussed in the Scripting lesson, such as reading and writing files. You will see some older concepts too, but again, we have them there to review and reinforce your understanding of those concepts.

#Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

#Sample Output:

#>>> Enter your First [space] Last name only: Bill Newman
#>>> Unique flower name with the first letter: Bellflower

# Write your code here

# HINT: create a dictionary from flowers.txt

# HINT: create a function
flower_dict = dict()

with open(r'wave 4\Labs\Scripting labs\flowers.txt', 'r') as rs:
    for lines in rs.readlines():
        lin = lines.split(':')
        ki = lin[0].strip()
        val = lin[1].strip()
        flower_dict[ki]=val

name = input('please Enter your First and Last name only, separated with a space:')
key = name.strip()[0]
print(flower_dict[key.upper()])
#print(flower_dict)