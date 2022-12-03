
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate","Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#average of total prices:
print()

sum = sum(prices)
average = sum/len(prices)
print("Average of total prices is: GHS", round(average, 2))

print()

#reduce price by "-5" cedis:

price = [x-5 for x in prices]
print("The new prices are: ", price)

print("")




#total revenue:
total_revenue = 0
for item in range(len(prices)):
   total_revenue += (prices[item] * last_week[item])
print("The total revenue is: GHS", total_revenue)
print()


#Products less than 30 cedis

less_than_30_cedis = []
for i in range(len(products)):
    if price[i] < 30:
        less_than_30_cedis.append(products[i])


print ("The products less than 30 cedis are: ") 
print()

for product in less_than_30_cedis:
     print (product)

     print()
