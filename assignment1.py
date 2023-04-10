print("Welcome to the Global Energy bill calculator!")

accountName = int(input("Enter your account number."))

month = int(input("Enter the month number (e.g., for January, enter 1)."))

#bills include both electricity and gas
#Electricity and gas prices are in cents. To convert to Canadian dollars (CDN$), multiply by 0.01.
elect_type = input("Enter your electricity plan (EFIR or EFLR).")
match elect_type:
    case "EFIR":
        priceEFIR1 = 8.36 #Fixed rate #first 1000 kWh
        priceEFIR2 = 9.41 #Firxed rate #after 1000th kWh
    case _: #EFLR
        priceEFLR = 9.11 #Floating rate
#   case _:
#       print("Please only input either 'EFIR' or 'EFLR'.")

elect_amount = int(input(f'Enter the amount of electricity you used in month of {month} (in kWh).'))
#EFIR = elect_type
if (elect_type == "EFIR"):
    if (elect_amount <= 1000):
        elect_charge = elect_amount * priceEFIR1
    elif (elect_amount >1000):
        elect_charge = (1000 * priceEFIR1) + ((elect_amount - 1000) * priceEFIR2)
else: #EFLR
    elect_charge = float(elect_amount * priceEFLR)

gas_type = input("Enter your gas plan (GFIR or GFLR).")
match gas_type:
#convert rate times 0.01
    case "GFIR":
        priceGFIR1 = 4.56 #Fixed Rate #first 950 GJ
        priceGFIR2 = 5.89 #Fixed Rate #after 950th GJ
    case _: #GFLR
        priceGFLR = 3.93 #Floating rate
#   case _:
#       print("Please only input either 'GFIR' or 'GFLR'.")

gas_amount = int(input(f'Enter the amount of gas you used in month of {month} (in GJ).'))
#GFIR = gas_type
if (gas_type == "GFIR"):
        if (gas_amount <=950):
            gas_charge = gas_amount * priceGFIR1
        elif (gas_amount > 950):
            gas_charge = (950 * priceGFIR1) + ((gas_amount - 950) * priceGFIR2)
#gas_charge = gas_amount * gasPrice
else:
    #GFLR
    gas_charge = gas_amount * priceGFLR

fixed_monthly_fee = 120.62
fixed_monthly_transaction_fee = 1.32

converted_elect_n_gas_charge = (elect_charge + gas_charge) * 0.01
total_b4_tax = fixed_monthly_transaction_fee + fixed_monthly_fee + converted_elect_n_gas_charge

#converted_elect_charge = elect_charge * 0.01
#converted_gas_charge = gas_charge * 0.01
#conversion of price of electricity and gas charges

province = input("Enter the abbreviation for your province of residence (two letters).")
#if (province == "AB" or "CB" or "MB" or "NT" or "NU" or "QC" or "SK" or "YT"):
#elif(province == "ON"):
#else:
    #NB NL, NS, PE
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
    case _: #NB NL NS PE
        taxRate = 0.15
#   case "NL":
#        taxRate = 0.15
#   case "NS":
#        taxRate = 0.15
#   case "PE":
#        taxRate = 0.15
#   case _:
#   print("Please only input the abbreviation of the name of your province (two letters).")

total_after_tax = total_b4_tax * (1 + taxRate)

#2 decimal points ONLY
print("Thank you! Your total amount due now is: $", float("%.2f" % total_after_tax),".")