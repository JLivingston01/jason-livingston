# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:58:35 2017

@author: Jason Livingston
"""

import pandas as pd
import numpy as np

check = pd.DataFrame()
check['date'] = ['2017-01-01','2017-01-02','2017-01-03','2017-01-04','2017-01-05','2017-01-06','2017-01-07','2017-01-08','2017-01-09','2017-01-10']
check['a'] = list(np.random.randint(0,10,10))
check['b'] = list(np.random.randint(0,10,10))
check['c'] = list(np.random.randint(0,10,10))

#Hardcode Table to Query String
string1 = []
for j in range(len(check['date'])):
    for i in list(check.columns.values):
        y = str(check[i][j])
        string = i+"="+y
        amp = "&"
        string1.append(string)
        if i != list(check.columns.values)[len(list(check.columns.values))-1]:
            string1.append(amp)
    lin = "\n"
    if j != len(check[list(check.columns.values)[0]])-1:
        string1.append(lin)    

str1 = "".join(string1)

#def to_data_str(X):
#    string1 = []
#    for j in range(len(X[list(X.columns.values)[0]])):
#        for i in list(X.columns.values):
#            y = str(X[i][j])
#            string = i+"="+y
#            amp = "&"
#            string1.append(string)
#            if i != list(X.columns.values)[len(list(X.columns.values))-1]:
#                string1.append(amp)
#        lin = "\n"
#        if j != len(X[list(X.columns.values)[0]])-1:
#            string1.append(lin)
#    str1 = "".join(string1)
#    return(str1)

#Function Table to String
def to_data_str(X):
    string1 = []
    for j in range(len(X[list(X.columns.values)[0]])):
        for i in list(X.columns.values):
            y = str(X[i][j])
            string = i+"="+y
            amp = "&"
            string1.append(string)
            if i != list(X.columns.values)[len(list(X.columns.values))-1]:
                string1.append(amp)
        lin = "\n"
        if j != len(X[list(X.columns.values)[0]])-1:
            string1.append(lin)
    str1 = "".join(string1)
    return(str1)

str1 = to_data_str(check)

#Function Table to HTML


def table_to_html(X):
    string = ['<table><tr>']
    for j in list(X.columns.values):
        x = '<th>'+j+'</th>'
        string.append(x)
    string.append('</tr>')
    for i in range(len(X[list(X.columns.values)[0]])):
        string.append('<tr>')
        for k in list(X.columns.values):
            x = str(X[k][i])
            y = '<td>'+x+'</td>'
            string.append(y)
        string.append('</tr>')
    string.append('</table>')
    string1 = "".join(string)
    return(string1)

html = table_to_html(check)   



testdata = pd.DataFrame()
testdata['A'] = [1,2,3,4,5,6,7,8,9,0]
testdata['B'] = [0,9,8,7,6,5,4,3,2,1]
testdata['C'] = [5,6,4,7,3,8,2,9,1,0]
html2 = table_to_html(testdata)


#Hardcode HTML Elements to HTML Page
filename = 'test table to html.html'
html_file = open(filename,"w")
wrapper = ("""<html>
    <head>
    <title> Test Table to Html </title>
    </head>
    <body><p>"""
    + html2 + 
    """</p></body>
    </html>""")
html_file.write(wrapper)
html_file.close()    

#Function HTML Elements to HTML page
def html_page(Title, Elements, filename):
    wrapper = ("""<html>
    <head>
    <title>"""+ Title +"""</title>
    </head>""" 
    +"\n".join(Elements)+
    """</p></body>
    </html>""")
    html_file = open(filename,"w")
    html_file.write(wrapper)
    html_file.close()

html_page('Test HTML 1',[html,html2],'test html 1.html')

#Hardcode Query String to Table
rows = str1.split("\n")
row1 = rows[0]
row1 = row1.replace("=",",")
row1 = row1.replace("&",",")
row1_sep = row1.split(",")
fields = []
data = []
for i in range(len(row1_sep)):
    if i % 2 == 0:
        fields.append(row1_sep[i])
    else:
        data.append(row1_sep[i])
        
fields = []
data = []
for i in range(len(rows)):
    row_n = rows[i].replace("=",",")
    row_n = row_n.replace("&",",")
    row1_sep = row_n.split(",")
    for j in range(len(row1_sep)):
        if i == 0:
            if j % 2 == 0:
                fields.append(row1_sep[j])
            else:
                data.append(row1_sep[j])
        else:
            if j % 2 != 0:
                data.append(row1_sep[j])

data1 = pd.DataFrame()
for i in range(len(fields)):
    tempfields = []
    for j in range(len(rows)):
        tempfields.append(data[i+j*len(fields)])
    data1[fields[i]] = tempfields
        
#Function Query String to Table
def str_to_tbl(X,lin_space,equal,elem_space):
    rows = X.split(lin_space)
    fields = []
    data = []
    for i in range(len(rows)):
        row_n = rows[i].replace(equal+elem_space,equal+"nan"+elem_space)
        row_n = rows[i].replace(equal,",")
        row_n = row_n.replace(elem_space,",")
        row1_sep = row_n.split(",")
        for j in range(len(row1_sep)):
            if i == 0:
                if j % 2 == 0:
                    fields.append(row1_sep[j])
                else:
                    data.append(row1_sep[j])
            else:
                if j % 2 != 0:
                    data.append(row1_sep[j])
    data1 = pd.DataFrame()
    for i in range(len(fields)):
        tempfields = []
        for j in range(len(rows)):
            tempfields.append(data[i+j*len(fields)])
        data1[fields[i]] = tempfields
    data1 = data1.replace("nan",np.NaN)
    return(data1)

new_table = str_to_tbl(str1,"\n","=","&")


##
class data_manipulation:
    
    def to_data_str(X):
        string1 = []
        for j in range(len(X[list(X.columns.values)[0]])):
            for i in list(X.columns.values):
                y = str(X[i][j])
                string = i+"="+y
                amp = "&"
                string1.append(string)
                if i != list(X.columns.values)[len(list(X.columns.values))-1]:
                    string1.append(amp)
        lin = "\n"
        if j != len(X[list(X.columns.values)[0]])-1:
            string1.append(lin)
        str1 = "".join(string1)
        return(str1)
    
    def table_to_html(X):
        string = ['<table><tr>']
        for j in list(X.columns.values):
            x = '<th>'+j+'</th>'
            string.append(x)
        string.append('</tr>')
        for i in range(len(X[list(X.columns.values)[0]])):
            string.append('<tr>')
            for k in list(X.columns.values):
                x = str(X[k][i])
                y = '<td>'+x+'</td>'
                string.append(y)
            string.append('</tr>')
        string.append('</table>')
        string1 = "".join(string)
        return(string1)
        
