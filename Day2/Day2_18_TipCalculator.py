print("Tip Calculator")

billTotal = input("What is the total bill?\n")
numPeople = input("How many people are splitting the bill?")
tipPercent = input("Tip Percentage? 10,12,14,20?")

payment = (float(billTotal)* ((int(100) + float(tipPercent))/int(100))) / int(numPeople)

print(" Each person should pay: " + str(payment))