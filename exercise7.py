# Write a program that will calculate the discount and amount to be paid by the customer, given that if the sales is less than N50,000 then discount is 5% of the sales otherwise discount is 10%.

# first lets get the original price which is the sales
sales = int(input("Enter the sales: "))
# Now lets check for the discount
discount = 0

if sales < 50000: 
    discount = 5
else:
    discount = 10

# Formular for percentage discount
discounted_price = sales - (sales * discount / 100)

print("Your discounted price is:  ", discounted_price)