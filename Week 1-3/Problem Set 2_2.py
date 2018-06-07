# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 23:48:53 2018

@author: HuangXuankun
"""
balance = 320000
annualInterestRate = 0.2

MonthlyInterestRate = annualInterestRate / 12
MonthlyPayment = (balance/12)//10*10-10
balance_test = balance
while balance_test > 0:
    MonthlyPayment += 10
    balance_test = balance
    for month in range(1,13):
        balance_test = (balance_test - MonthlyPayment) * (1+MonthlyInterestRate)

print('Lowest Payment:' , int(MonthlyPayment))
