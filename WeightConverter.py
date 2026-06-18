weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds(K or P)?: ").upper()

while True:
        
    if unit == "K":
        pounds = weight*2.205
        print(f"Your weight in Pounds: {pounds}Lbs")
        break
    elif unit == "P":
        kg = weight/2.205
        print(f"Your weight in Kg: {kg:.2f}kg")
        break
    else:
        print(f"{unit} was not valid")
        break
    