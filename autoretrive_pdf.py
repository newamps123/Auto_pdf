from flask import *
from tabula import read_pdf
import fnmatch
import os
import tabula
import pandas as pd

app = Flask(__name__)



@app.route('/ml/table',methods=['POST'])
def table():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, 'Qlik-Sense*.pdf'):
            df = read_pdf(file, pages='all',multiple_tables=True,encoding='ISO-8859-1',stream=True)
            parsejson = request.form
            if parsejson:
                if parsejson['table']:
                    col_2 = parsejson['table']
                    fil = df[int(col_2)-1]
                    string = ''.join(str(fil))
                    return string
            else:
                string_1 = ''.join(str(df))
                return string_1
        else:
            return 'no file is there'


@app.route('/ml/table/colomn',methods=['POST'])
def colomn():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file,'Qlik-Sense*.pdf'):
            df = read_pdf(file, pages='all', multiple_tables=True, encoding='ISO-8859-1', stream=True)
            parsejson=request.form
            if parsejson['table'] and parsejson['colomn']:
                col_2 = parsejson['table']
                col = parsejson['colomn']
                fil = df[int(col_2) - 1][int(col)]
                string_col = ''.join(str(fil))
                return string_col

@app.route('/ml/table/cell',methods=['POST'])
def cell():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file,'Qlik-Sense*.pdf'):
            df = read_pdf(file,pages='all',multiple_tables=True,encoding='ISO-8859-1',stream=True)
            parsejson = request.form
            tab = parsejson['table']
            fil = df[int(tab) - 1]
            #print(type(fil))
            if 'row' and 'colomn' in parsejson:
                row = parsejson['row']
                col = parsejson['colomn']
                cell = fil.iloc[int(row)][int(col)]
                string_cell = ''.join(str(cell))
                return string_cell

@app.route('/ml/table/row',methods=['POST'])
def row():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file,'Qlik-Sense*.pdf'):
            df = read_pdf(file, pages='all', multiple_tables=True, encoding='ISO-8859-1', stream=True)
            parsejson = request.form
            tab = parsejson['table']
            fil = df[int(tab) - 1]
            if 'row' in parsejson:
                row = parsejson['row']
                pff = fil.iloc[int(row)]
                string_row = ''.join(str(pff))
                return string_row

@app.route('/ml/table/update',methods=['POST'])
def ubdate():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file,'Qlik-Sense*.pdf'):
            df = read_pdf(file, pages='all', multiple_tables=True, encoding='ISO-8859-1', stream=True)
            parsejson = request.form
            tab = parsejson['table']
            row = parsejson['row']
            col = parsejson['colomn']
            fil = df[int(tab) - 1]
            pf1 = input("Enter New Value")
            pf = fil.replace(fil.ix[int(row)][int(col)], pf1)
            string_ubdate = "".join(str(pf))
            return string_ubdate

@app.route('/ml/table/delete',methods=['POST'])
def delete():
      for file in os.listdir('.'):
          if fnmatch.fnmatch(file,'Qlik-Sense*.pdf'):
              df = read_pdf(file, pages='all', multiple_tables=True, encoding='ISO-8859-1', stream=True)
              parsejson = request.form
              tab = parsejson['table']
              fil = df[int(tab) - 1]
              row = parsejson['row']
              pff = fil.iloc[int(row)]
              fil.drop(int(row),inplace=True)
              string_0 = ''.join(str(fil))
              return string_0


app.run(port=5000,debug=True)