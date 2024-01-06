upperLimit = int(input("Sum of Even Numbers between 1 and ??: "));
while(int(upperLimit) > int(1000)):
    upperLimit = input("Please try a number less than 1000... : ");

superSum = 0
print("perfect! - calculating....")
for i in range(0,upperLimit):
    if(i%2 == 0):
        superSum = superSum + i
        print(".", end='')

print("Found Answer: " + str(superSum))


