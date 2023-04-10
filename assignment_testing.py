print("Welcome to the Global Energy bill calculator!")

accountName = int(input("Enter your account number."))

month = int(input("Enter the month number (e.g., for January, enter 1)."))

#bills include both electricity and gas
#Electricity and gas prices are in cents. To convert to Canadian dollars (CDN$), multiply by 0.01.
elect_type = input("Enter your electricity plan (EFIR or EFLR).")
match elect_type:
    case "EFIR":
        priceEFIR1 = float(8.36) #Fixed rate #first 1000
        priceEFIR2 = float(9.41) #Firxed rate #after 1000th
    case "EFLR": 
        priceEFLR = float(9.11) #Floating rate
    case _:
        print("Please only input either 'EFIR' or 'EFLR'.")

#print("Enter the amount to electricity used in the month of ",month, "(in kWh).")

elect_amount = int(input("Enter the amount of electricity you used (in kWh) in month of ")) #print("month")
#EFIR = elect_type
if (elect_type == "EFIR"):
    if (elect_amount <= 1000):
        elect_charge = elect_amount * priceEFIR1
    if (elect_amount >1000):
        elect_charge = (1000 * priceEFIR1) + ((elect_amount - 1000) * priceEFIR2)
else:
    #EFLR
    elect_charge = elect_amount * priceEFLR

gas_type = input("Enter your gas plan (GFIR or GFLR).")
match gas_type:
    case "GFIR":
        priceGFIR1 = float(4.56) #Fixed Rate #first 950
        priceGFIR2 = float(5.89) #Fixed Rate #after 950th
    case "GFLR":
        priceGFLR = float(3.93 * 0.01) #Floating rate
    case _:
        print("Please only input either 'GFIR' or 'GFLR'.")

gas_amount = int(input("Enter the amount of gas you used (in GJ) in month of" ,month,))
#GFIR = gas_type
if (gas_type == "GFIR"):
        if (gas_amount <=950):
            gas_charge = gas_amount * priceGFIR1
        if (gas_amount > 950):
            gas_charge = (950 * priceGFIR1) + ((gas_amount - 950) * priceGFIR2)
#gas_charge = gas_amount * gasPrice
else:
    #GFLR
    gas_charge = gas_amount * priceGFLR

# ****another method to perform the same task****
#if (province == "AB" or "CB" or "MB" or "NT" or "NU" or "QC" or "SK" or "YT"):
    #taxRate = 0.05
#elif(province == "ON"):
    #taxRate = 0.13
#else: #NB NL, NS, PE
    #taxRate = 0.15

province = input("Enter the abbreviation for your province of residence (two letters).")
match province:
    case "AB":
        taxRate = 0.05
    case "BC":
        taxRate = 0.05
    case "MB":
        taxRate = 0.05
    case "NT":
        taxRate = 0.05
    case "NU":
        taxRate = 0.05
    case "QC":
        taxRate = 0.05
    case "SK":
        taxRate = 0.05
    case "YT":
        taxRate = 0.05
    case "ON":
        taxRate = 0.13
    case _:                     #NB NL, NS, PE
        taxRate = 0.15

fixed_monthly_fee = 120.62
fixed_monhtly_transaction_fee = 1.32

converted_elect_charge = elect_charge * 0.01
converted_gas_charge = gas_charge * 0.01
#conversion of price. To convert to Canadian dollars (CDN$), multiply by 0.01.

total_b4_tax = fixed_monhtly_transaction_fee + fixed_monthly_fee + converted_elect_charge + converted_gas_charge
total_after_tax = total_b4_tax * (1 + taxRate)

#2 decimal points ONLY
print("Thank you! Your total amount due now is: $", float("%.2f" % total_after_tax),".")