maxlimit = 100

for i in range(0,maxlimit):
    if(i%3 ==0 and i%5==0):
        print("FIZZBUZ")
    elif i%3 == 0:
        print("FIZZ")
    elif i%5 ==0:
        print("BUZ")
    else:
        print(i)

print("gameOver")