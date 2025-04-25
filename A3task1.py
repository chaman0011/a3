def fact1(n):
    if n<=0:
        return 1
    else:
        return n*fact1(n-1)

n1=int (input("Enter a number :"))
x1= fact1(n1)
print(f"Factorial of number {n1} :{x1}")
