# Exercise- BANKING APPLICATION showing ADDITION OF VARIOUS ACCOUNTS OF ACCOUNT HOLDERS using LOOPS

# lets assume balance in various accounts be
# 1. savings account balance = 1000
# 2. current account = 2000
# 3. fixed deposit = 4000


individual_acct_bal_list = [1000, 2000, 4000]
total = 0
for individual_acct in individual_acct_bal_list:
    total = total + individual_acct

print(total)

