


print("#################")
print("select INPUT currency")
print("*EUR")
print("*USD")
print("*MDL")
print("#################")
currency_IN =input("choose:")

money_IN=float(input("money:"))
print("#################")
print("select OUTPUT currency")

if currency_IN !="EUR":
    print("*EUR")
if currency_IN !="USD":
    print("*USD")
if currency_IN !="MDL":
    print("*MDL")
print("#################")
currency_out =input("choose:")
eur_usd=1.10
eur_mdl=20.00
usd_mdl=18.00

if currency_IN == "EUR" and currency_out =="USD":
    money_out=money_IN*eur_usd

if currency_IN == "USD" and currency_out =="EUR":
    money_out=money_IN/eur_usd
if currency_IN == "MDL" and currency_out =="USD":
    money_out=money_IN/usd_mdl
if currency_IN == "USD" and currency_out =="MDL":
    money_out=money_IN*usd_mdl
if currency_IN == "EUR" and currency_out =="MDL":
    money_out=money_IN*eur_mdl
if currency_IN == "MDL" and currency_out =="EUR":
    money_out=money_IN/eur_mdl


print(money_out)
print(round(money_out,2))

#money_usd=input("enter ur money usd")
#money_usd=float(money_usd)
#usd_2_Eur=0.9
#money_eur=money_usd*usd_2_Eur

# print("your money in eur:",money_eur)