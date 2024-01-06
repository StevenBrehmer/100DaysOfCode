print("Tip Calculator")

billTotal = input("What is the total bill?\n ")
numPeople = input("How many people are splitting the bill? ")
tipPercent = input("Tip Percentage? 10,12,14,20? ")

payment = str(round((float(billTotal)* ((int(100) + float(tipPercent))/int(100))) / int(numPeople),2))

#print f-string to sneak vars into the line without messy cat
print(f" Each person should pay: ${payment}")