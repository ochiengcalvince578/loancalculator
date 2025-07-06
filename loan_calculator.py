import argparse

def loan_schedule(principal, interest, months):
    
    repaymentcount = 0; 

    monthly_interest_rate = interest/12/100; 
    
    #armotization formula
    monthly_payment = principal * ((monthly_interest_rate * (1 + monthly_interest_rate)**months)/((1 + monthly_interest_rate)**months - 1));

    balance = principal

    for month in range(1, months + 1):

        interest = monthly_interest_rate * balance;

        principal_payment = monthly_payment - interest;

        balance = balance - principal_payment;
       

        print(f"{month:<5} {monthly_payment:<10.2f} {interest:<10.2f} {principal_payment:<10.2f} {balance:<10.2f}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Loan Armotization Schedule Calculator")
    parser.add_argument("principal", type = float)
    parser.add_argument("interest", type = float)
    parser.add_argument("months", type = int)

    args = parser.parse_args()

    loan_schedule(args.principal, args.interest, args.months)