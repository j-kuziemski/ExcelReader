#!/usr/bin/env python


import pandas as pd
import sys
import os
import glob


Par1 = (sys.argv[1])
Par2 = (sys.argv[2])


path = os.getcwd()
excel_files= glob.glob(os.path.join(path, "*.xlsx"))
excel_files1=['Scope1_SASK12_31.0.xlsx', 'Airtel_SASK12_Scope4_10.2.xlsx']


def site():
 for individual_excel_file in excel_files:
    df = pd.read_excel(individual_excel_file)
    dropowanie = df[['Site','Type','System_IP']].where(df['Site'] == Par1).dropna()
    print("File Name: " + individual_excel_file)
    if dropowanie.empty != False:
        print('Lack of node in database')
    else:
        print(dropowanie)

def ajpi():
 for individual_excel_file in excel_files:
    df = pd.read_excel(individual_excel_file)
    dropowanie = df[['Site','Type','System_IP']].where(df['System_IP'] == Par2).dropna()
    print("File Name: " + individual_excel_file)
    if dropowanie.empty != True:
        print('Lack of node in database')
    else:
        print(dropowanie)


if Par1 != '--':
    site()
else:
    print('Wrong parameter')

if Par2 != '--':
    ajpi()
else:
    print('Wrong parameter')