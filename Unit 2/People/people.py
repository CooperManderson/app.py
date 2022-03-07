import sqlite3

# connect to the database
con = sqlite3.connect("People/people.db")


name = input("what is your name?")
age = input("what is your age?")
sex = input("what is your gender?")
earns = input("how much do you earn?")
likes = input("what are your likes?")
dislikes = input("what are your dislikes?")

sql = """
    
    insert
    into people (name, age, sex, earns, likes, dislikes)
    (?, ?, ?, ?, ?, ?,);


"""

cur.execute(sql, ('name', 'age', 'sex', 'earns', 'likes', 'dislikes',))