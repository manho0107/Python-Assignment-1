print("Welcome to the Global Energy bill calculator!")

accountName = int(input("Enter your account number."))

month = int(input("Enter the month number (e.g., for January, enter 1)."))

#bills include both electricity and gas
#Electricity and gas prices are in cents. To convert to Canadian dollars (CDN$), multiply by 0.01.
elect_type = input("Enter your electricity plan (EFIR or EFLR).")

match elect_type:
    case "EFIR":
    case "EFLR":
    case _:
        print("Please only input either 'EFIR' or 'EFLR'.")

elect_amount = int(input("Enter the amount of electricity you used in month" ,month, "(in kWh)"))

priceEFIR1 = float(8.36 * 0.01) #ERIF #Fixed rate #first 1000
priceEFIR2 = float(9.41 * 0.01) #ERIF #Firxed rate #after 1000th
priceEFLR = float(9.11 * 0.01) #EFLR #Floating rate

if ((elect_type == EFIR) and elect_amount <=1000):
    elect_charge = elect_amount * priceEFIR1
elif ((elect_type == EFIR) and elect_amount >1000):
    elect_charge = (1000 * priceEFIR1) + ((elect_amount - 1000) * priceEFIR2)
else:
    elect_charge = elect_amount * priceEFLR

gas_type = input("Enter your gas plan (GFIR or GFLR).")
match gas_type:
    case "GFIR":
    case "GFLR":
    case _:
        print("Please only input either 'GFIR' or 'GFLR'.")

gas_amount = int(input("Enter the amount of gas you used in month 2 (in GJ)."))

priceGFIR1 = float(4.56 * 0.01) #GFIR #Fixed Rate #first 950
priceGFIR2 = float(5.89 * 0.01) #GFIR #Fixed Rate #after 950th
priceGFLR = float(3.93 * 0.01) #GFLR #Floating rate

if ((gas_type == "GFIR") and gas_amount <=950):
    gas_charge = gas_amount * priceGFIR1
elif((gas_type =="GFIR") and gas_amount >950):
    gas_charge = (1000 * priceGFIR1) + ((gas_amount - 1000) * priceGFIR2)
#gas_charge = gas_amount * gasPrice
else:
    gas_charge = gas_amount * priceGFLR

province = input("Enter the abbreviation for your province of residence (two letters).")
if (province == "AB" or "CB" or "MB" or "NT" or "NU" or "QC" or "SK" or "YT"):
    taxRate = 0.05
elif(province == "ON"):
    taxRate = 0.13
else:
    taxRate = 0.15

fixed_monthly_fee = 120.62
fixed_monhtly_transaction_fee = 1.32

total_b4_tax = fixed_monhtly_transaction_fee + fixed_monthly_fee + elect_charge + gas_charge
total_after_tax = total_b4_tax * (1 + taxRate)

print("Thank you! Your total amount due now is: $", float(total_after_tax), ".")