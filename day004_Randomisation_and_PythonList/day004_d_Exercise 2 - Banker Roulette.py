#Exercise 2 - Banker Roulette
# ou are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

#Important: You are not allowed to use the choice() function.

#Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

import random

list1 = input("Give me everybody's names, separated by a comma. RANDOM-NAME-HERE is going to buy the meal today! ")
list2 = list1.split(",")


# CACH 1
# sl = len(list2)
# ppl = random.randint(0,sl - 1)
# person_pay_the_bill = list2[ppl]

#CACH 2

person_pay_the_bill = random.choice(list2)
print(f"{person_pay_the_bill} has to pay the bill")
