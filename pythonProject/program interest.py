response=input("Please enter number of years")
t=int(response)
P=10000
n=12
r=0.08
A=P*(1+r/n)**(n*t)
print("Final amount is",A)
