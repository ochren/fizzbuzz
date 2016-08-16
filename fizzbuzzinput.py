print("Enter the lower and upper boundaries of fizzbuzz number set.")
lower=int(input("Lower value:"))
upper=int(input("Upper value:"))
for n in range(lower, upper+1):
    status = ''
    if n % 3 == 0:
        status+="Fizz"
    if n % 5 == 0:
        status+="Buzz"
    if not status:
        status+=str(n)
    print status
