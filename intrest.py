

principle = 0
rate = 0
time = 0


while principle<=0:
    principle = float(input("Enter the priciple amount: "))

    if principle<=0:
        print("principle cant be less tha zero")

while rate<=0:
    rate = float(input("Enter the intrest rate amount: "))

    if rate<=0:
        print("rate cant be less than or equal to zero")

while time<=0:
    time = int(input("Enter the time : "))

    if time<=0:
        print("time cant be less than or equal to zero")

total = principle * pow((1+ rate/100),time)
print(f"Balance after {time} years : ${total : .2f}")