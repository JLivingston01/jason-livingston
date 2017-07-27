# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:07:20 2017

@author: Jason Livingston
"""
##Transform pandas DFs for other uses
##DF to query string creates string of form 'date=2017-01-01&a=8&b=5&c=6\ndate=2017-01-02&a=3&b=3&c=0' from DF
##df_to_html writes html table from contents of pandas DF
##df_to_lists_of_lists creates a list of rows, with each row as a list of elements. This was designed for my gradient descent experiments. I know its not a string.
class data_to_string:
    def df_to_str(X):
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
    
    def df_to_html(X):
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
        
        
    def df_to_list_of_lists(df):
        df2 = []
        for i in range(len(df[list(df.columns.values)[0]])):
            templist = []
            for col in list(df.columns.values):
                x = df[col][i]
                templist.append(x)
            df2.append(templist)
        return df2

##transform data string in form 'category equal element elem_space lin_space' into Pandas DF
##example of query string 'date=2017-01-01&a=8&b=5&c=6\ndate=2017-01-02&a=3&b=3&c=0'
##casting would be manual after application
class strings_to_df:
    def query_str_to_tbl(X,lin_space,equal,elem_space):
        import pandas as pd
        import numpy as np
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
        
        
        