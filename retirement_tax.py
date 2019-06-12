# Road to The Zero Tax Bracket in Retirement 
# Without Fctoring expected Social Security benefit, half of which counts to to tax percentage at retirement.

my_contributions = 590
company_contributions = my_contributions * .50 
annual_contributions = ( my_contributions + company_contributions ) * 24 #paystubs

print("Annual Contributions", annual_contributions)

years_to_retirement = 59.5 - 23
print("Years To Retirement", years_to_retirement)

standard_deduction = 24000 
#adjusted for inflation
count = years_to_retirement
while count > 0:
    standard_deduction += 0.03 * 24000
    count -= 1

print("Est Standard Deduction at Retirement", standard_deduction)

#RMD
desired_401KTotal = standard_deduction / 0.0365
print("Desired 401K Total", desired_401KTotal)

#Growth of 401k Now
count = years_to_retirement
val_401K = annual_contributions 
while count > 0:
    count -= 1 
    val_401K += val_401K * 0.08
print("401K Value at retirement with 1 year contribution", val_401K)

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

print("Years of Contribution:", years_of_contribution)
print("Target 401K Value:", target_val_401K)

