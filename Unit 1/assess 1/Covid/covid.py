from flask import Flask, render_template, request, redirect, url_for, session, flash
import random #needed for random number generation
app = Flask(__name__)
filename = "covid.txt"
contents = open(filename)



#open covid.txt
#read contents of the file
#for each line split it into two on the :
#image equals line 1, part 1 then .jpg
#add dictionary to list

for i in contents:
    a_list = []
    title = "a"
    value = i.split(":")
    dictionary = {title: value}
    print(dictionary["a"])
    dictionary[title] = {
        "description": "b",
        "model": "Mustang",
        "year": 1964
    }
    #dictionary_copy = (title).copy()
    #a_list.append(dictionary_copy)

    #John = "nice guy"
    #programmer = John
    #echo ${!programmer}  # echos nice guy

#open file




@app.route("/")

def index():

    return render_template("index.html", cars=thisdict)
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)

