# -*- coding: utf-8 -*-

# ########################
balance = 3329
annualInterestRate = 0.2
# ########################



interest_rate = annualInterestRate / 12.0
payment_lower_bound = balance / 12.0
payment_upper_bound = (balance * (1 + interest_rate)**12) / 12.0

print('interest_rate', interest_rate)
print('payment_lower_bound', payment_lower_bound)
print('payment_upper_bound', payment_upper_bound)

def disection_search(payment_lower_bound, payment_upper_bound, interest_rate):
    
    error = 0.1
    payment = (payment_lower_bound + payment_upper_bound) / 2
    NMAX = 1000
    
    print('payment', payment, '\n')
    
    # for month in range(1, 13):
        
    #     if month == 1:
    #         unpaid_balance = balance
    #     else:
    #         unpaid_balance = unpaid_balance - payment
            
    #     updated_balance = unpaid_balance * (1 + interest_rate)
    #     print('Month', month, '| Monthly_unpaid_balance', unpaid_balance, '| Updated_balance:', updated_balance)
    
    # print('\nLatest updated balance', updated_balance)
    

    def get_updated_balance(balance, payment, interest_rate):
        
        print('payment', payment)
        
        for month in range(1, 13):
            
            if month == 1:
                unpaid_balance = balance
            else:
                unpaid_balance = unpaid_balance - payment
            
            updated_balance = unpaid_balance * (1 + interest_rate)
            # print('Month', month, '| Monthly_unpaid_balance', unpaid_balance, '| Updated_balance:', updated_balance)
            
        # print('Latest updated balance', updated_balance)
        return updated_balance
    
    print()
    updated_balance_lower = get_updated_balance(balance, payment_lower_bound, interest_rate)
    print('updated_balance_lower', updated_balance_lower)
    updated_balance_payment = get_updated_balance(balance, payment, interest_rate)
    print('updated_balance_payment', updated_balance_payment)
    updated_balance_upper = get_updated_balance(balance, payment_upper_bound, interest_rate)
    print('updated_balance_upper', updated_balance_upper)
    
    # while abs(updated_balance_payment) > error:
    print('\nupdated_balance_payment', updated_balance_payment, '| error', error)
        
    if updated_balance_lower * updated_balance_payment < 0:  # The solution is in this interval.
        payment_upper_bound = payment
        print('\npayment_lower_bound', payment_lower_bound)
        print('payment_upper_bound', payment_upper_bound)
    else:
        payment_lower_bound = payment
        print('\npayment_lower_bound', payment_lower_bound)
        print('payment_upper_bound', payment_upper_bound)
    
    payment = (payment_lower_bound + payment_upper_bound) / 2
    print('new_payment', payment)


    
    # N = 1
    # while N <= NMAX:
        
    #     print('\n N', N, 'NMAX', NMAX, '\n')
    #     updated_balance_lower = get_updated_balance(balance, payment_lower_bound, interest_rate)
    #     print()
    #     updated_balance_payment = get_updated_balance(balance, payment, interest_rate)
    #     print()
    #     updated_balance_upper = get_updated_balance(balance, payment_upper_bound, interest_rate)
        
    #     if abs(updated_balance_payment) < error:
    #         print('updated_balance_payment < error', updated_balance_payment < error)
    #         return updated_balance_payment
        
    #     N += 1
        
        # if updated_balance_lower > updated_balance_payment:
        #     print('updated_balance_lower > updated_balance_payment', updated_balance_lower > updated_balance_payment)
        #     payment_upper_bound = payment
        # else:
        #     print('updated_balance_lower > updated_balance_payment', updated_balance_lower > updated_balance_payment)
        #     payment_lower_bound = payment

    print('\nupdated_balance_payment', updated_balance_payment)