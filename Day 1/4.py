cp,sp = list(map(float,input("Enter the cost price and selling price of the product: ").split()))
profit = sp-cp
sp1 = 1.05 * profit + cp
print("Profit: ", profit)
print("Selling price to increase profit by 5%: ", sp1)
