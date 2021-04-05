# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:32:44 2021

@author: Abhishek
"""

from flask import Flask, render_template, request
from flask import render_template_string
import pickle
import numpy as np


import pymysql.cursors
import pandas as pd
import datetime
from itertools import combinations


app = Flask(__name__)

@app.route('/wtf')
def home():
	return render_template('pitt_nivesh_home.html')

@app.route('/user_reg', methods=['POST'])
def user_registration():
    if request.method == 'POST':
        #return render_template('index2.html')
        user_id = request.form['user_id']
        email_id = request.form['email']
        password = request.form['password']
        
        
        con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

        cursor = con.cursor()
        qry = 'INSERT INTO user_login (user_id, email, password)'
        qry = qry + 'VALUES(%s, %s, %s)'
        cursor.execute(qry, (user_id, email_id, password)) 
        con.commit()
        con.close()
            
        return render_template('index2.html')
 

@app.route('/home_page')
def user_home_page():
    return render_template('pitt_nivesh_home.html')

@app.route('/log_out_to_user_reg')
def log_out_to_user_reg():
    return render_template('index2.html')

@app.route('/login_user')
def login_user():
    return render_template('login_auth.html')


@app.route('/user_authentication',methods=['POST'])
def user_authentication():
    if request.method == 'POST':
        email_id = request.form['email']
        password = request.form['password']
        
        con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
        cursor = con.cursor()
        
        qry = 'SELECT * FROM user_login WHERE '
        qry = qry + 'email LIKE %s AND password LIKE %s '
        
        cursor.execute(qry, (email_id, password)) 
    
        rows = cursor.fetchall()
        #con.commit()
        #con.close()
        
        print(len(rows))
        
        #print(rows[0]['email'])
        
        con.commit()
        con.close()
        
        #return render_template('login_auth.html', what=rows)
        
        #return render_template('login_auth.html', what="USER DOES NOT EXIST")
        
        if(len(rows)==0):
            
            return render_template('login_auth.html', what= "USER DOES NOT EXIST" )
        
        if(rows[0]['email']==email_id and rows[0]['password']==password):
            
            return render_template('login_auth.html', what=rows)
        
        else:
            return render_template('login_auth.html', what= "USER DOES NOT EXIST" )
            
        
        
    
    
        

@app.route('/stock_search')
def stock_search_button():
    return render_template('stocks.html')
    
           
@app.route('/stock', methods=['POST'])
def stock_search():
    if request.method == 'POST':
        stock_id_info = request.form['stock_id_info']
        
        #stk_id='AAPL'
        
        con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
        cursor = con.cursor()
        qry = 'SELECT * FROM available_stocks WHERE '
        qry = qry + 'symbol LIKE %s '
        
        cursor.execute(qry, (stock_id_info)) 
    
        rows = cursor.fetchall()
        
        con.commit()
        
        con.close()
        
        
        #render_template_string('hello {{ what }}', what=rows)
        return render_template('stocks.html', what = rows)
        
        
        
        
    
if __name__ == '__main__':
	app.run(debug=True,use_reloader=False)
