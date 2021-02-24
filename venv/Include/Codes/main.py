import sqlite3
#add all commit here


#coupons [coupon code, customer name, customer email, location of complaint, available balance, isActive,  initial balance, number of transactions, date of creation, average transaction, validating manager, comments ]

connection = sqlite3.connect("coupondata.db")
cursor = connection.cursor()

# table creation

com1 = """CREATE TABLE IF NOT EXISTS
coupons(coupon_code TEXT PRIMARY KEY, customer_name TEXT, customer_email TEXT, location TEXT, available_balance REAL, active INTEGER, initial_balance REAL, number_of_transactions INTEGER, date_of_creation TEXT, avg_transaction REAL, validating_manager TEXT, comments TEXT )"""
com2 = """CREATE TABLE IF NOT EXISTS
codes(coupon_code TEXT PRIMARY KEY, used INTEGER)"""
#blob is just a datetime thingy

cursor.execute(com1)
cursor.execute(com2)
for i in ["ZAO3Q","QLEEO","ESR3X"]:
    cursor.execute(f"INSERT INTO codes VALUES ('{i}', 0)")

#cursor.execute("INSERT INTO coupons VALUES ('ZAO3Q', 'Alex Hal', 'blip@gmail.com', 'CV', 20, 1, 20, 0, NULL, 0, 'alex', NULL)")

coupon_code = "ZAO3Q"

cursor.execute("SELECT * FROM coupons WHERE coupon_code = ?", (coupon_code,))
row = cursor.fetchone()
#if row is None:
    #print(f"Coupon {coupon_code} does not exist")
#else:
    #print(f"Coupon {coupon_code} exists")
    #print(row)
    #array = [i for i in row]
    #print(array)



def searchAvailableCode():
    cursor.execute("SELECT * FROM codes WHERE used = ?", (0,))
    row = cursor.fetchone()
    return [i for i in row]

def updateCode(code):
    cursor.execute("UPDATE codes SET used = 1 WHERE coupon_code = ?", (f"{code}",))
    #debug
    cursor.execute("SELECT * FROM codes")
    row = cursor.fetchall()
    print(row)

def addCoupon(code, customer_name, customer_email, location, available_balance, isActive,  initial_balance, number_of_transactions, date_of_creation, avg_transaction, validating_manager, comments):
    cursor.execute(f"INSERT INTO coupons VALUES ('{code}', '{customer_name}', '{customer_email}', '{location}', {available_balance}, {isActive}, {initial_balance}, {number_of_transactions}, '{date_of_creation}', {avg_transaction}, '{validating_manager}', '{comments}')")
    updateCode(code)

def searchCouponRow(code):
    cursor.execute("SELECT * FROM coupons WHERE coupon_code = ?", (code,))
    row = cursor.fetchone()
    return [i for i in row]

def updateCoupon(code, balance, number_of_transaction, avg_transaction):
    cursor.execute(f"UPDATE coupons SET available_balance = {balance}, number_of_transactions = {number_of_transaction}, avg_transaction = {avg_transaction}  WHERE coupon_code = ?", (f"{code}",))
