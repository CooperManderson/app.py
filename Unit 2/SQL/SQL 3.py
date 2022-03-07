import sqlite3

# connect to the database
con = sqlite3.connect("SQL-Data/rockyconcrete.db")

# create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row  # enables us to use the column heading
cur = con.cursor()  # is the pointer to use in the database
run = True
while run is True:
    variable = str(input("""1. Get Customer Details
2. Get Order Details
3. Get Product Details
4. Quit 
    
Input a number: """))

    if variable == "1":
        name = str(input("""
Enter the customer name to search for: """))

        sql = """
                select *
                from customers
                where cust_name like ?;


        """

        cur.execute(sql, (
            '%' + name + '%',))  # each variable, town, creditlimit, is paired with the things in the tuple above(sql) respective to their orders
        results = cur.fetchall()
        for row in results:
            print(""" 
""", row['cust_name'], 'lives in', row['street'], 'in', row['town'], 'and has a credit limit of',
row['cr_limit'], 'their customer number is', row['cust_no'], """
                  """)

    elif variable == "2":
        order_number = str(input("Enter the order number to search for: "))

        sql = """
                select *
                from orders
                where order_no like ?
                order by order_no asc;
    
    
        """

        cur.execute(sql, (
            '%' + order_number + '%',))  # each variable, town, creditlimit, is paired with the things in the tuple above(sql) respective to their orders
        results = cur.fetchall()
        for row in results:
            print(""" 
        """, "Order", row['order_no'], 'was made on', row['order_date'], 'by customer number', row['cust_no'], """
                          """)

    elif variable == "3":
        product_code = str(input("Enter the product code to search for: "))

        sql = """
                        select *
                        from products
                        where prod_code like ?;


                """

        cur.execute(sql, (
            '%' + product_code + '%',))  # each variable, town, creditlimit, is paired with the things in the tuple above(sql) respective to their orders
        results = cur.fetchall()
        for row in results:
            print("Product", row['prod_code'], "is a", row['description'], 'in the group of', row['prod_group'], "its list price is", row['list_price'], "the quantity on hand is", row['qty_on_hand'], "the remake level is", row['remake_level'], "and the remake quantity is", row['remake_qty'],"""""
                                  """)


    elif variable == "4":
        run = False
    else:
        print("please only reply one of the above numbers")
print("goodbye")