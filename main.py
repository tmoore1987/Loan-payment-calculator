# input for loan amount, interest rate and term

def main():
    print('Monthly payment loan calculator ')
    print(' ')

    loan_amt =float(input('Enter loan amount: '))
    term = float(input('Enter the term in years: '))
    apr = float(input('Enter the annual interest rate: '))

    # calculate monthly payment
    monthly_rate = apr/1200
    months = term*12
    monthly_payment = loan_amt * monthly_rate / (1- (1+ monthly_rate) ** (- months))
    
    # show result
    print(f'The monthly payment is:  {monthly_payment}.')


main()
