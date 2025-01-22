## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
low = 0.0
high = 1.0
r = (low + high) / 2
down_payment = 800000 * 0.25
months = 36
amount_saved = 0
max_amount_saved = amount_saved = initial_deposit * (1 + high / 12) ** months
steps = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
while abs(amount_saved - down_payment) > 100:
    if max_amount_saved < down_payment:
        r = None
        break
    amount_saved = initial_deposit * (1 + r / 12) ** months
    if amount_saved > down_payment:
        high = r
    else:
        low = r
    r = (low + high) / 2
    steps = steps + 1

print("Best savings rate:", r)
print("Steps in bisection search:", steps)