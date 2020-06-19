# -*- coding: utf-8 -*-

# ########################
# NO INCLUIR EN SOLUCIÖN
balance = 320000
annualInterestRate = 0.2
# balance = 999999
# annualInterestRate = 0.18
# ########################


interest_rate = annualInterestRate / 12.0
payment_lower_bound = balance / 12.0
payment_upper_bound = (balance * (1 + interest_rate)**12) / 12.0

def disection_search(payment_lower_bound, payment_upper_bound, interest_rate):
    """
    Paying debt off in a year using bisection search.

    Parameters
    ----------
    payment_lower_bound : float
        Miminum search value.
    payment_upper_bound : float
        Maximum search value.
    interest_rate : float
        Annual interest rate.

    Returns
    -------
    float
        The minimum fixed mounthly payment needed in order pay off a credit 
        card balance within 12 months.
    """
    
    error = 0.01
    payment = (payment_lower_bound + payment_upper_bound) / 2
    # print('payment', payment)
    
    def get_updated_balance(balance, payment, interest_rate):
        
        updated_balance = 0
        
        for month in range(1, 13):
            
            if month == 1:
                unpaid_balance = balance - payment
            else:
                unpaid_balance = updated_balance - payment
            
            updated_balance = unpaid_balance * (1 + interest_rate)
            
        return updated_balance

    updated_balance_lower = get_updated_balance(balance, payment_lower_bound, interest_rate)
    updated_balance_payment = get_updated_balance(balance, payment, interest_rate)
    # updated_balance_upper = get_updated_balance(balance, payment_upper_bound, interest_rate)
    
    if abs(updated_balance_payment) <= error:
        return payment
    else:
        if updated_balance_lower * updated_balance_payment < 0:  # The solution is in this interval.
            payment_upper_bound = payment
            return disection_search(payment_lower_bound, payment_upper_bound, interest_rate)
        else:
            payment_lower_bound = payment
            return disection_search(payment_lower_bound, payment_upper_bound, interest_rate)
    
lowest_payment = disection_search(payment_lower_bound, payment_upper_bound, interest_rate)
print('Lowest Payment:', round(lowest_payment, 2))
