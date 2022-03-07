# import sqlite3
#
# #connect to the database
# con = sqlite3.connect("SQL-Data/rockyconcrete.db")
#
#
# #create a cursor/pointer to navigate the database
# con.row_factory = sqlite3.Row #enables us to use the column heading
# cur = con.cursor() #is the pointer to use in the database
#
#
# name = str(input("Enter the customer name to search for: "))
#
# sql = """
#         select *
#         from customers
#         where cust_name like ?;
#
#
# """
#
# cur.execute(sql,('%'+name+'%',)) #each variable, town, creditlimit, is paired with the things in the tuple above(sql) respective to their orders
# results = cur.fetchall()
# #print(results)
#
# if len(results) > 0:
#     for row in results:
#         print(row['cust_name'], 'lives in', row['street'], 'in', row['town'], 'and has a credit limit of', row['cr_limit'], 'their customer number is', row['cust_no'])
#         cust_no = row['cust_no']
#         sql2 = """
#                 select max(order_no) as 'order_no', max(order_date) as 'order_date'
#                 from orders
#                 where cust_no = ?;
#
#
#         """
#         cur.execute(sql2, ('cust_no',))
#         results2 = cur.fetchone()
#         if not results2:
#             results2 = 'no orders made'
#         else:
#             result2 = "last order number" + str(results2['order_no'])
#         latest_order = 0
#         order_date = 0
#
#         print("most recent order was", results2)
#
# else:
#     print("No records found")

import sqlite3

# connect to the database
con = sqlite3.connect("SQL-Data/rockyconcrete.db")

# create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row  # enables us to use the column heading
cur = con.cursor()  # is the pointer to use in the database

name = str(input("Enter the customer name to search for: "))

sql = """
        select *
        from customers
        where cust_name like ?;


"""

cur.execute(sql, (
'%' + name + '%',))  # each variable, town, creditlimit, is paired with the things in the tuple above(sql) respective to their orders
results = cur.fetchall()
print(results)

if len(results) > 0:
    for row in results:
        print(row['cust_name'], 'lives in', row['street'], 'in', row['town'], 'and has a credit limit of',
              row['cr_limit'], 'their customer number is', row['cust_no'])
        cust_no = row['cust_no']
        sql2 = """
                select *
                from orders
                where cust_no = ?;


        """
        cur.execute(sql2, (cust_no,))
        results2 = cur.fetchall()
        latest_order = 0
        order_date = 0
        for row2 in results2:
            if int(row2['order_no']) > latest_order:
                latest_order = int(row2['order_no'])
                order_date = row2['order_date']
        print("most recent order was", latest_order, "on", order_date)

else:
    print("No records found")