## Numpy Exercise 2
import numpy as np

## This array documents the last 5 sales for each of Superstore's four cash registers.
salesArray = np.array(
    [
        [150.68, 207.99, 107.88, 58.99, 60.59],
        [20.89, 98.99, 258.62, 19.76, 101.59],
        [70.66, 190.10, 134.54, 200.14, 15.59],
        [10.52, 201.59, 140.55, 13.99, 45.98],
    ]
)

## Step 1: Print the total sales for the store.
print(
    "-----------------------------------------------   STEP ONE   -----------------------------------------------"
)
totalSales = salesArray.sum()
print("Superstore's Total Sales: $", format(totalSales, ",.2f"), sep="")

## Step 2: What was Superstore's smallest and largest sale? Print them.
print(
    "-----------------------------------------------   STEP TWO   -----------------------------------------------"
)
minSales = salesArray.min()
print("Lowest Sale: $", format(minSales, ",.2f"), sep="")
maxSales = salesArray.max()
print("Highest Sale: $", format(maxSales, ",.2f"), sep="")

## Step 3: Print an array that will show which sales are greater than or equal to $100.
print(
    "-----------------------------------------------   STEP THREE  -----------------------------------------------"
)
hundredsArray = []
for sales in salesArray.flat:
    if sales > 100.0:
        hundredsArray.append(sales)
print(hundredsArray)
# print(salesArray >= 100.00)

## Step 4: Print the total sales for each register.
print(
    "-----------------------------------------------   STEP FOUR   -----------------------------------------------"
)
registerSales1 = salesArray[0].sum()
registerSales2 = salesArray[1].sum()
registerSales3 = salesArray[2].sum()
registerSales4 = salesArray[3].sum()
print("Register 1 Total Sales: $", format(registerSales1, ",.2f"), sep="")
print("Register 2 Total Sales: $", format(registerSales2, ",.2f"), sep="")
print("Register 3 Total Sales: $", format(registerSales3, ",.2f"), sep="")
print("Register 4 Total Sales: $", format(registerSales4, ",.2f"), sep="")

## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees.
# Each sale is subject to a 2% credit card fee.
# Using the salesArray, create a new array that stores the 2% fee for each sale and register.
# Print the array and then print the total fees.
print(
    "-----------------------------------------------   STEP FIVE  -----------------------------------------------"
)
feeArray = salesArray * 0.02
print(feeArray)
feeSum = feeArray.sum()
print("Total Credit Card Fees: $", format(feeSum, ",.2f"), sep="")

## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after
## paying credit card fees. Store this in a new array and print it.
print(
    "-----------------------------------------------   STEP SIX  -----------------------------------------------"
)
ebitArray = salesArray - feeArray
ebit = ebitArray.sum()
print(ebitArray)
print("Earnings Before Interest & Tax (EBIT): $", format(ebit, ",.2f"), sep="")

## Step 7: Print the sales only for the second and forth cash register
print(
    "-----------------------------------------------   STEP SEVEN  -----------------------------------------------"
)
print("Register 2 Sales: ", salesArray[1])
print("Register 2 Total Sales: $", format(registerSales2, ",.2f"), sep="")
print("Register 4 Sales: ", salesArray[3])
print("Register 4 Total Sales: $", format(registerSales4, ",.2f"), sep="")

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister.
## Add the new register to the original array. Print the updated salesArray.
print(
    "-----------------------------------------------   STEP EIGHT  -----------------------------------------------"
)
newRegister = np.array([17.89, 13.59, 107.89, 176.88, 56.78])
salesArray = np.vstack((salesArray, newRegister))
print(salesArray)

## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly.
# The sale should have been $20.14. Update the array to correct this error.
# Print the array before and after the update to see the change.
print(
    "-----------------------------------------------   STEP NINE  -----------------------------------------------"
)
print("Register 3 Sales: ", salesArray[2], sep="")
print("Current Sale Error: ", salesArray[2][3], sep="")
salesArray[2][3] = 20.14
print()
print("Adjusted Register 3 Sales: ", salesArray[2], sep="")
print("Adjusted Sale: ", salesArray[2][3], sep="")
