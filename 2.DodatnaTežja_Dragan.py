#Write a program that picks a random number and then tries to guess it --
#that is, it plays both roles.
#Let the program repeat this for one hundred times.
#In the end, it should print out the average number of guesses it needed.

#Now, we're interested in this:
#how many guesses does your program need
#if the number is chosen from 1 and 100,
#1 and 1000, 1 and 10000, 100000, 1000000...
#How does the average number of guesses increase with the interval size?

#You can either submit a program that prints a table-like output,
#with the interval in one column and the average number of guesses in another,
#or you can submit a graph (prepared in Python or in Excel, if you will)
#that shows the relation.

import matplotlib.pyplot as plt
import random
from matplotlib import pyplot as plt
from matplotlib import style

prvistevec = 0
zanka = int(input("How many times would you like the loop to repeat? "))
povprecje = 0
najvecx = int(input("Insert the biggest number: "))
while prvistevec != zanka:
    stevilo = random.randint(0, najvecx)
    najvec = najvecx
    najmanj = 0
    stevec = 0
    x = 0
    ugib = random.randint(najmanj, najvec)
    while ugib != stevilo:
        if stevilo > ugib:
            najmanj = ugib
            ugib = random.randint(najmanj, najvec)
            stevec = stevec + 1     
        elif stevilo < ugib:
            najvec = ugib
            ugib = random.randint(najmanj, najvec)
            stevec = stevec + 1       
        else:
            stevec = stevec + 1
    prvistevec = prvistevec + 1
    povprecje = povprecje + stevec
povprecje = povprecje / zanka
print("Average number of attempts is: ", povprecje)

prvistevec = 0
povprecje = 0
najvecx = 100
while prvistevec != 100:
    stevilo = random.randint(0, najvecx)
    najvec = najvecx
    najmanj = 0
    stevec = 0
    x = 0
    ugib = random.randint(najmanj, najvec)
    while ugib != stevilo:
        if stevilo > ugib:
            najmanj = ugib
            ugib = random.randint(najmanj, najvec)
            stevec = stevec + 1     
        elif stevilo < ugib:
            najvec = ugib
            ugib = random.randint(najmanj, najvec)
            stevec = stevec + 1       
        else:
            stevec = stevec + 1
    prvistevec = prvistevec + 1
    povprecje = povprecje + stevec
povprecje = povprecje / zanka
print("Average number of attempts with random 100 numbers, 100 times is: ", povprecje)
y = [povprecje]

prvistevec = 0
povprecje = 0
najvecx = 1000
while prvistevec != 100:
    stevilo = random.randint(0, najvecx)
    najvec = najvecx
    najmanj = 0
    stevec = 0
    x = 0
    ugib = random.randint(najmanj, najvec)
    while ugib != stevilo:
        if stevilo > ugib:
            najmanj = ugib
            ugib = random.randint(najmanj, najvec)
            stevec = stevec + 1     
        elif stevilo < ugib:
            najvec = ugib
            ugib = random.randint(najmanj, najvec)
            stevec = stevec + 1       
        else:
            stevec = stevec + 1
    prvistevec = prvistevec + 1
    povprecje = povprecje + stevec
povprecje = povprecje / zanka
print("Average number of attempts with random 1000 numbers, 100 times is: ", povprecje)
y2 = [povprecje]

prvistevec = 0
povprecje = 0
najvecx = 10000
while prvistevec != 100:
    stevilo = random.randint(0, najvecx)
    najvec = najvecx
    najmanj = 0
    stevec = 0
    x = 0
    ugib = random.randint(najmanj, najvec)
    while ugib != stevilo:
        if stevilo > ugib:
            najmanj = ugib
            ugib = random.randint(najmanj, najvec)
            stevec = stevec + 1     
        elif stevilo < ugib:
            najvec = ugib
            ugib = random.randint(najmanj, najvec)
            stevec = stevec + 1       
        else:
            stevec = stevec + 1
    prvistevec = prvistevec + 1
    povprecje = povprecje + stevec
povprecje = povprecje / zanka
print("Average number of attempts with random 10000 numbers, 100 times is: ", povprecje)
y3 = [povprecje]

style.use('ggplot')

x = [100]
x2 = [1000]
x3 = [10000]

plt.bar(x, y, align='center', width=100)
plt.bar(x2, y2, color='g', align='center', width=500)
plt.bar(x3, y3, color='r', align='center', width=500)

plt.ylabel('Number of attempts')
plt.xlabel('Amount of numbers')

plt.show()

