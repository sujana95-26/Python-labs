import statistics

#personal allowance = 11850
#0 -34500 at 20%
#34501 - 150000 at 40%
#over 150000 at 45%
# salary - 11850, /0.2
# 34500 x 0.2 =  6900
#(salary - 34500) * 0.4
# +11850

def get_income_tax(salary):
        if salary <= 11850:
            return 0
        elif salary <= 34500:
            tax = (salary - 11850) * 0.2
            return tax
        elif  salary >= 34501 and salary <= 150000:
            tax = (salary - 11850) * 0.4
            return tax
        else:
             tax = (salary - 11850) * 0.45
             return tax

salary = (80000)

print("The income tax is: ", get_income_tax(salary))



    



