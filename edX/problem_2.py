# -*- coding: utf-8 -*-

# #########################
# BORRAR
balance = 3329
annualIterestRate = 0.2
# #########################

monthly_payment = 10
monthly_interest_rate = annualIterestRate / 12

def get_lowest_payment(balance, annualIterestRate, monthly_payment, monthly_interest_rate):
    for month in range(1, 13):
        if month == 1:
            monthly_unpaid_balance = balance
        else:
            monthly_unpaid_balance = monthly_unpaid_balance - monthly_payment
            
        updated_balance = monthly_unpaid_balance * (1 + monthly_interest_rate)
        print('Month', month, '| Monthly_unpaid_balance', monthly_unpaid_balance, '| Updated_balance:', updated_balance)
    if updated_balance >= 0:
        monthly_payment += 10
        return get_lowest_payment(balance, annualIterestRate, monthly_payment, monthly_interest_rate)
    else:
        return monthly_payment

lowest_payment = get_lowest_payment(balance, annualIterestRate, monthly_payment, monthly_interest_rate)
print('Lowest Payment:', lowest_payment)
