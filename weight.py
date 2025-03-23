

weight = float(input("Enter your waight: "))
unit = input("Enter the unit of the weight (P/K): ").upper()

if unit == 'K':
    weight = weight * 2.205
    unit = "Lbs"
    print(f"your weight is : {round(weight,1)} {unit}")
elif unit == 'P':
    weight = weight/2.205
    unit = "kgs"
    print(f"your weight is : {round(weight,1)} {unit}")
else :
    print(f"{unit} Not valid")

