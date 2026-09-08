items =["Coffee","sandwich","juice"]
prices = [12,13,14]

total = 0
for price in prices:
    total+= price
vat = total *0.15
final_total = total+vat

print("items:")
for item in items:
    print("- ", item)
print("total:", total)
print("vat:", vat)
print("final total:", final_total)
