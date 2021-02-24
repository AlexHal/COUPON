from datetime import date
import main
import sqlite3
#coupons [coupon code, customer name, customer email, location of complaint, available balance, isActive,  initial balance, number of transactions, date of creation, average transaction, validating manager, comments ]


# get data from form




def coupon_initialisation(customer_name, customer_email, location, available_balance, validating_manager, comments):
    active = 1
    initial_balance = available_balance
    number_of_transactions = 0
    date_of_creation = date.today()
    avg_transaction = 0

    array = main.searchAvailableCode()
    code = array[0]
    print(code)

    main.addCoupon(code, customer_name, customer_email, location, available_balance, active,  initial_balance, number_of_transactions, date_of_creation, avg_transaction, validating_manager, comments)


coupon_initialisation("alexj", "alex@","CV",20,"alex", "no")
coupon_initialisation("alex", "alex@","CV",20,"alex", "no")