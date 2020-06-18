# -*- coding: utf-8 -*-

# #########################
# BORRAR
balance = 42
annualIterestRate = 0.2
monthlyPaymentRate = 0.04
# #########################

for month in range(13):
    if month == 0:
        updated_balance = balance
        interest = 0

    balance = updated_balance + interest
    min_monthly_payment = balance * monthlyPaymentRate
    updated_balance = balance - min_monthly_payment
    interest = (annualIterestRate / 12) * updated_balance
    # print('Month', month, 'Remaining balance:', balance)

print('Remaining balance:', round(balance, 2))
