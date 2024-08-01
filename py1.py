# https://github.com/Prayashh7/Mayalu.gitdef highest(x):
print(f"The highest number is {x}")
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))
if a>b>c:
    highest(a)
elif b>a>c:
    highest(b)
elif c>b>a:
    highest(c)