import sqlite3

#connect to the database
con = sqlite3.connect("SQL-Data/rockyconcrete.db")


#create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row #enables us to use the column heading
cur = con.cursor() #is the pointer to use in the database

# sql = """
#
#     select *
#     from customers
#     where town = 'Brisbane';
# """
#
# cur.execute(sql)
# results = cur.fetchall()
#
# print(type(results))
# print(results)

#parameter query
# town = str(input("Enter the town to search for: "))
# creditlimit = input("enter a credit limit: ")
#
# sql = """
#         select *
#         from customers
#         where town like ?
#         and cr_limit >= ?;
#
# """
#
# cur.execute(sql,('%'+town+'%', creditlimit)) #each variable, town, creditlimit, is paired with the things in the tuple above(sql) respective to their orders
#results = cur.fetchall()
#print(results)



# if len(results) > 0:
#     for row in results:
#         print(row['cust_name'], 'lives in', row['street'], 'in', row['town'], 'and has a credit limit of', row['cr_limit'])
# else:
#     print("No records found")