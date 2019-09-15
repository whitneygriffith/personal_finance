# Road to The Zero Tax Bracket in Retirement 
# Without Fctoring expected Social Security benefit, half of which counts to to tax percentage at retirement.

#max personal contribution is 19K in 2019 
company_contributions = 19000 * .50 
annual_contributions = (19000 + company_contributions )

print("Estimated contribution each paystub at a biweekly rate: $%d" % (19000/24))

print("Annual Contributions: $%d" % (annual_contributions))

years_to_retirement = 59.5 - 23 # current age
print("Years To Retirement: %d" % (years_to_retirement))

standard_deduction = 24000 
#adjusted for inflation
count = years_to_retirement
while count > 0:
    standard_deduction += 0.03 * 24000
    count -= 1

print("Est Standard Deduction at Retirement: $%d" % (standard_deduction))

#Required Minimum Distribution
desired_401KTotal = standard_deduction / 0.0365
print("Desired 401K Total to not pay any tax on 401K withdrawal: $%d"  % (desired_401KTotal))

#Growth of 401k Now
count = years_to_retirement
val_401K = annual_contributions 
while count > 0:
    count -= 1 
    val_401K += val_401K * 0.08 #return rate of 401k typically between 6-8%
print("401K Value at retirement with 1 year contribution: $%d" % (val_401K))

stop_contributing = False
years_of_contribution = 1 
target_val_401K = annual_contributions

while not stop_contributing:
    target_val_401K = annual_contributions * years_of_contribution
    count = years_to_retirement - years_of_contribution
    #expected annual growth of 8%
    while count > 0:
        count -= 1 
        target_val_401K += target_val_401K * 0.08
    if target_val_401K >= desired_401KTotal:
        stop_contributing = True
    years_of_contribution += 1

print("Years of Contribution at max personal contribution and 50 percent company match: %d" %(years_of_contribution))
print('401K Value after %d years of contributions: $%d' %(years_of_contribution, target_val_401K ))

