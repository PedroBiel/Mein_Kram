# -*- coding: utf-8 -*-

# #########################
# NO INCLUIR EN SOLUCIÖN
# balance = 3329
# balance = 4773
# balance = 3926
# annualIterestRate = 0.2
# balance = 3561
# annualIterestRate = 0.04
# balance = 3757
# annualIterestRate = 0.18
# balance = 4600
# annualIterestRate = 0.04
balance = 4557
annualIterestRate = 0.04
# #########################

monthly_payment = 10
monthly_interest_rate = annualIterestRate / 12

def get_lowest_payment(balance, annualIterestRate, monthly_payment, monthly_interest_rate):
    
    updated_balance = 0
    
    for month in range(1, 13):
        
        if month == 1:
            monthly_unpaid_balance = balance - monthly_payment
        else:
            monthly_unpaid_balance = updated_balance - monthly_payment
            
        updated_balance = monthly_unpaid_balance * (1 + monthly_interest_rate)
        print('Month', month, '| Monthly_unpaid_balance', monthly_unpaid_balance, '| Updated_balance:', updated_balance)
    
    if updated_balance >= 0:
        monthly_payment += 10
        return get_lowest_payment(balance, annualIterestRate, monthly_payment, monthly_interest_rate)
    else:
        return monthly_payment

lowest_payment = get_lowest_payment(balance, annualIterestRate, monthly_payment, monthly_interest_rate)
print('Lowest Payment:', lowest_payment)
