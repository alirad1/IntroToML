x = 0 
for i in range(100,1000):
    sum = 0 
    first = i % 10 
    second =(i //10) % 10  
    third = (i//100)
    #print(first, second, third)
    sum = first + second + third
    if (sum % 2 == 1):
        x+=1

print(x)