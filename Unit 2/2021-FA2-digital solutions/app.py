from flask import Flask, render_template, request, redirect, flash, session, url_for
from datetime import datetime, date
from flask_wtf import FlaskForm
import sqlite3
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectMultipleField, SelectField
from wtforms.fields.html5 import DateField # see https://stackoverflow.com/questions/26057710/datepickerwidget-with-flask-flask-admin-and-wtforms
from wtforms.validators import DataRequired, URL, Optional, InputRequired

import random

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ddksididkdkdl'

#connect to database
con = sqlite3.connect("app.db", check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()



### Form models ####

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class VideoForm(FlaskForm):
    URL = StringField('Input Video URL', validators=[DataRequired()])
    description = StringField('Add a description if you want')
    classid = StringField('Input Class ID', validators=[DataRequired()])
    submit2 = SubmitField('Submit')
########## routes ##########


@app.route('/')
@app.route('/index')
def index():
    sql3 = """
                    select *
                    from Videos
                    order by Video_ID desc
                    limit 3;"""
    cur.execute(sql3)
    result = cur.fetchall()
    session['video1url'] = result[0][1]
    session['video1desc'] = result[0][2]
    session['video1class'] = result[0][3]
    session['video2url'] = result[1][1]
    session['video2desc'] = result[1][2]
    session['video2class'] = result[1][3]
    session['video3url'] = result[2][1]
    session['video3desc'] = result[2][2]
    session['video3class'] = result[2][3]
    session['url1'] = session['video1url'].replace('https://www.youtube.com/watch?v=', '')
    session['url2'] = session['video2url'].replace('https://www.youtube.com/watch?v=', '')
    session['url3'] = session['video3url'].replace('https://www.youtube.com/watch?v=', '')
    # print(url1)
    # print(url2)
    # print(url3)
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        print('posting')
        print(form.username.data)
        print(form.password.data)
        if form.validate_on_submit():
            print('has submitted stuff')
            un = form.username.data
            pw = form.password.data
            print(un,pw)

            sql = """
            select * 
            from Login
            where username = ?
            and password = ?;"""


            cur.execute(sql,(un,pw))
            result = cur.fetchall()
            if len(result) == 1:
                session['username'] = result[0][0]
                session['firstname'] = result[0][1]
                session['lastname'] = result[0][2]
                session['is_teacher'] = result[0][4]
                if session['is_teacher']:
                    session['teacher_code'] = result[0][5]
                session['login'] = True
                sql3 = """
                select *
                from Videos
                order by Video_ID desc
                limit 3;"""
                cur.execute(sql3)
                result = cur.fetchall()
                session['video1url'] = result[0][1]
                session['video1desc'] = result[0][2]
                session['video1class'] = result[0][3]
                session['video2url'] = result[1][1]
                session['video2desc'] = result[1][2]
                session['video2class'] = result[1][3]
                session['video3url'] = result[2][1]
                session['video3desc'] = result[2][2]
                session['video3class'] = result[2][3]
                session['url1'] = session['video1url'].replace('https://www.youtube.com/watch?v=', '')
                session['url2'] = session['video2url'].replace('https://www.youtube.com/watch?v=', '')
                session['url3'] = session['video3url'].replace('https://www.youtube.com/watch?v=', '')
                # print(url1)
                # print(url2)
                # print(url3)
                return redirect(url_for('index'))

            else:
                flash("username or password incorrect, try again")
        else:
            flash("There is something missing")
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    # clear out the session
    if session['username']:
        session['username'] = None
        session['firstname'] = None
        session['lastname'] = None
        session['is_teacher'] = None
        session['teacher_code'] = None
        session['login'] = None

    flash("You have successfully logged out")
    return redirect(url_for('index'))


@app.route('/Videos', methods=['GET', 'POST'])
def Videos():
    form = VideoForm()
    if request.method == 'POST':
        print("hi")
        if form.validate_on_submit():
            print("hi")
            sql2 = """
                    insert
                    into Videos (URL, Description, Class_ID)
                    values (?, ?, ?);"""

            try:
                cur.execute(sql2,(form.URL.data, form.description.data, form.classid.data))
                con.commit()
            except:
                flash("Oops! Something went wrong! Check the values and try again")
            return redirect(url_for('index'))
    return render_template('VideoSubmission.html', form=form)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8081
    app.run(host, port, debug=True)
