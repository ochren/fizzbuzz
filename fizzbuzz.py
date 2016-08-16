print("Fizzbuzz counting up to 200.")
for n in range(1,200):
    status = ''
    if n % 3 == 0:
        status+="Fizz"
    if n % 5 == 0:
        status+="Buzz"
    if not status:
        status+=str(n)
    print status
