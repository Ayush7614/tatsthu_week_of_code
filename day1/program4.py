costprice = float(input("Enter the cost price of product: "))
sellprice = float(input("Enter the sell price of product: "))
profit = sellprice - costprice
newSellingprice = 1.05 * profit + sellprice
print("The profit from this sell is", profit)
print("To increase the profit by 5% the selling price should be", newSellingprice)
