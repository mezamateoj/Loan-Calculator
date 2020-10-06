
"""
Created on Tue Oct  6 10:58:08 2020

@author: Mateo M
"""

import argparse
import sys
import math


parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str, help='Type of operation')
parser.add_argument('--principal', type=float, help='Loan Principal')
parser.add_argument('--periods', type=int, help='Number of periods')
parser.add_argument('--payment', type=float, help='monthly payment')

parser.add_argument('--interest', type=float, help='what is the interest')
    
args = parser.parse_args()
    # sys.stdout.write(str(creditcal(args)))

if args.type == 'diff' and args.periods != None and args.principal != None and args.interest != None:
    m = 0
    e = 0
    o = 0
    for i in range(args.periods):
        m += 1
        e += 1
        d = (args.principal / args.periods) + (args.interest / (12 *100)) * (args.principal - (args.principal * ((m - 1) / args.periods)))
        f = math.ceil(d)
        o += math.ceil(d)
        print('Month ' + str(e) + ' : payment is ' + str(f))
        print('Overpayment = ' + str(o - args.principal))
        
elif args.type == 'annuity' and args.payment != None and args.principal != None and args.interest != None:
    i = (args.interest / 100) / 12
    n = math.log(args.payment / (args.payment - i * args.principal), 1 + i)
    years_months = divmod(math.ceil(n), 12)
    years = years_months[0]
    months = years_months[1]
    over = math.ceil(args.payment * (years * 12)) - args.principal  
    if years == 1 and months == 1:
        print('It will take', years, 'year to repay this loan!')
    else:
        print('It will take', years, 'years to repay this loan!')
        print('Overpayment = ' + str(over))
   
    
elif args.type == 'annuity' and args.periods != None and args.principal != None and args.interest != None:
    i = (args.interest / 100) / 12
    a = args.principal * ((i * ((1 + i) ** args.periods)) / (((1 + i) ** args.periods) - 1))
    final_a = math.ceil(a)
    print('Your annuity payment = ' + str(final_a) + '!')
    over = (final_a * args.periods) - args.principal
    print('Overpayment = '+ str(over))
    
elif args.type == 'annuity' and args.periods != None and args.payment != None and args.interest != None:
    i = (args.interest / 100) / 12
    p = args.payment / ((i * ((1 + i) ** args.periods)) / (((1 + i) ** args.periods) - 1))
    final_p = round(p)
    over = (args.payment * args.periods) - final_p
    print('Your loan principal = ' + str(final_p) + '!')
    print('Overpayment = ' + str(over))
    
    
        
else:
    print('Incorrect parameters')
        
            
    
        
# if __name__== '__main__':
    # main()

            
    
