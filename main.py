#!/usr/bin/env python


import pandas as pd
import sys
import os
import glob
import msvcrt as m



Par1 = (sys.argv[1])
Par2 = (sys.argv[2])

def wait():
    m.getch()

path = os.getcwd()
excel_files= glob.glob(os.path.join(path, "*.xlsx"))


def SiteID_Sys():
 for individual_excel_file in excel_files:
    df = pd.read_excel(individual_excel_file)
    dropowanie = df[['Site','Type','System_IP']].where(df['Site'] == Par1).dropna()
    print("File Name: " + individual_excel_file)
    if dropowanie.empty != False:
        print('Lack of node in database')
    else:
        print(dropowanie)

def SiteIP_Sys():
 for individual_excel_file in excel_files:
    df = pd.read_excel(individual_excel_file)
    dropowanie = df[['Site','Type','System_IP']].where(df['System_IP'] == Par2).dropna()
    print("File Name: " + individual_excel_file)
    if dropowanie.empty != False:
        print('Lack of node in database')
    else:
        print(dropowanie)

def SiteID_P2P():
 for individual_excel_file in excel_files:
    df = pd.read_excel(individual_excel_file, sheet_name='Interface')
    dropowanie = df[['Node_ID','RemoteNode','AddressIP', 'AddressIPRem']].where(df['Node_ID'] == Par1).dropna()
    print("File Name: " + individual_excel_file)
    if dropowanie.empty != False:
        print('Lack of node in database')
    else:
        print(dropowanie)

def SiteIP_P2P():
 for individual_excel_file in excel_files:
    df = pd.read_excel(individual_excel_file, sheet_name='Interface')
    dropowanie = df[['Node_ID','RemoteNode','AddressIP', 'AddressIPRem']].where(df['AddressIP'] == Par2).dropna()
    print("File Name: " + individual_excel_file)
    if dropowanie.empty != False:
        print('Lack of node in database')
    else:
        print(dropowanie)

ans = True
while ans:
    print("""
    Menu:
    ---------------

    1. System
    2. Interface
    3. Exit
    """)
    ans = input("Choose option: ")
    if ans == "1":
        print("\nSystem searching was choosen")
        if Par1 != '--':
            SiteID_Sys()
        else:
            print('\nWrong parameter\n')

        if Par2 != '--':
            SiteIP_Sys()
        else:
            print('\nWrong parameter\n')

        exit()
        os.system('cls')
        break
    elif ans == "2":
        print("\nInterface searching was choosen")

        if Par1 != '--':
            SiteID_P2P()
        else:
            print('\nWrong parameter\n')

        if Par2 != '--':
            SiteIP_P2P()
        else:
            print('\nWrong parameter\n')
        exit()
        os.system('cls')
        break
    elif ans == "3":
        print("\nGoodbye")
        ans = None
    else:
        print("\nNot Valid Choice Try again")
        print("\nPress Enter...")
        exit()
        os.system('cls')
        ans = True







