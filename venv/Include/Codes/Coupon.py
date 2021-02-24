from datetime import date
import main
import sqlite3
import email1

#creation
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
    email1.opening(customer_email, code, initial_balance) #can add expiry date later

#usage



def processTransaction(coupon_code, transaction):
    array = main.searchCouponRow(coupon_code)
    balance = array[4]
    if transaction <= balance:
        new_balance = balance - transaction
        nb_transaction = array[7]
        new_nb_transaction = array[7] + 1
        avg_transaction = array[9]
        new_avg_transaction = (nb_transaction*avg_transaction + transaction)/new_nb_transaction
        main.updateCoupon(coupon_code, new_balance, new_nb_transaction, new_avg_transaction )


    else:
        return email1.failure(coupon_code,balance,transaction)


