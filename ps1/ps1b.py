annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12
monthly_r = r / 12
number_of_months = 0

while current_savings < total_cost * portion_down_payment:
    if number_of_months % 6 == 0 and number_of_months != 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
    current_savings += (monthly_salary * portion_saved) + \
        (current_savings * monthly_r)
    number_of_months += 1

print("Number of months:", number_of_months)