import random
a = random.randint(0,9)
b = random.randint(0,9)
print(a,"*",b,"=" ,end='')
c = int(input())
if c==a*b:
        print("Right")
else:
    print("Wrong.The answer is",a*b)
