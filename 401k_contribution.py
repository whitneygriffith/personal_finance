from math import ceil, floor

class Strategy401K:

    def __init__(self, current_age, personal_contribution=19000, company_contribution_rate=.50):
        self.current_age = current_age
        self.personal_contribution = personal_contribution
        self.company_contribution = company_contribution_rate * self.personal_contribution
        self.monthly_contribution = ceil(personal_contribution / 12)
        self.biweekly_contribution = ceil(personal_contribution / 24)

    def get_monthly_contribution(self):
        return self.monthly_contribution

    def get_biweekly_contribution(self):
        return self.biweekly_contribution

    def get_total_annual_contribution(self):
        return self.personal_contribution + self.company_contribution

    def years_to_retirement(self):
        return ceil(59.5 - self.current_age)
    
    def future_standard_deduction(self, current_standard_deduction=12400):
        """
        Calculates standard deducation at retirement, adjusted for inflation

        Arguments:
            current_standard_deduction      for your tax bracket (single, married)
                                            default is 2020 value for single person filing
        """

        count = self.years_to_retirement()
        future_standard_deduction = current_standard_deduction
        while count >0:
            #0.03 is the standard inflation rate 
            future_standard_deduction += 0.03 * future_standard_deduction
            count -=1 
        return floor(future_standard_deduction)

    def target_401k_total(self):
        """
        Desired 401K total at retirement that ensures you wouldn't be taxed upon your required minimum distribution
        """
        target_401k = self.future_standard_deduction() / 0.0365
        return ceil(target_401k)
    
    def when_to_stop_contributing(self):
        stop_contributing = False
        target_401k = self.target_401k_total()
        years_of_contribution = 1 
        current_401K_value = self.get_total_annual_contribution()

        while not stop_contributing:
            current_401K_value = current_401K_value * years_of_contribution
            count = self.years_to_retirement() - years_of_contribution
            while count > 0:
                current_401k_value = self.growth_of_current_401k(current_401K_value)
                count -= 1 
            if current_401K_value >= target_401k:
                stop_contributing = True
            years_of_contribution += 1
        return [years_of_contribution, current_401K_value]

    def growth_of_current_401k(self, current_value_401k=None):
        
        if current_value_401k == None:
            # Total contribution after 1 year
            current_value_401k = self.get_total_annual_contribution()

        new_value =  current_value_401k + floor(current_value_401k * 0.06) #return rate of 401k typically between 6-8%
        return new_value
    

        
            


if __name__ == "__main__":

    current_age = 23 

    my401K_strategy = Strategy401K(current_age)

    print(f"Estimated biweekly contribution: {my401K_strategy.get_biweekly_contribution()}")
    print(f"Estimated annual contribution: {my401K_strategy.personal_contribution}")
    print(f"Estimated annual contribution with company match: {my401K_strategy.get_total_annual_contribution()}")
    print(f"Estimated Standard Deduction at Retirement at 59.5: {my401K_strategy.future_standard_deduction()}")
    print(f"Target 401K Total to not pay any tax upon required minimum distribution: {my401K_strategy.target_401k_total()}")
    print(f"Stop contibuting after {my401K_strategy.when_to_stop_contributing()[0]} years to have a 401K of {my401K_strategy.when_to_stop_contributing()[1]} upon retirement")





        