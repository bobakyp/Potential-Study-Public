import sys
import os
import glob
import sqlalchemy
import pandas as pd
import numpy as np
import ipywidgets as widgets
import textwrap
import ipywidgets
from ipywidgets import interact, interactive, fixed, interact_manual
import IPython.display
from IPython.display import display, clear_output

import plotly.graph_objects as go
path1 = os.getcwd()
sys.path.append("../../..")
# read each sheet of Resi excel file
drop_down = ipywidgets.Dropdown(options = ['Consumer Rebate Program - Future Offering',
                                           'Residential Lighting Efficiency Program', 'City Plants',
                                           'Behavioral Program - Future Offering',
                                           'Residential New Construction - Future Offering',
                                           'Consumer Rebate Program', 'Efficient Product Marketplace',
                                           'HVAC Optimization', 'Window AC Recycling',
                                           'Refrigerator Turn-In & Recycle',
                                           'HVAC Optimization - Future Offering', 'CAMR',
                                           'Refrigerator Exchange', 'Home Energy Improvement Program',
                                           'Efficient Product Marketplace - Future Offering',
                                           'Residential Lighting Efficiency Program - Future Offering',
                                           'Biz-CDI'],
                                   value ='CAMR',
                                   description = 'Program:',
                                   disabled = False,
                                   )
def func1(Program_name):
    df_Savings = pd.read_excel('PS_Residential_Results.xlsx', sheet_name = 'Res Energy Savings')
#df_TP_Savings = pd.read_excel('PS_Residential_Results.xlsx', sheet_name = 'Res TP')
#df_Participants = pd.read_excel('PS_Residential_Results.xlsx', sheet_name = 'Res Participants')
#df_Costs = pd.read_excel('PS_Residential_Results.xlsx', sheet_name = 'Res Costs')


#Rename column headers
    Program_Savings = df_Savings.loc[:,['Realistic Achievable Potential By Measure','Unnamed: 3',\
                                         'Cumulative Annual Energy (MWh) Savings - GROSS','Unnamed: 30','Unnamed: 31',\
                                        'Unnamed: 32','Unnamed: 33','Unnamed: 34','Unnamed: 35','Unnamed: 36','Unnamed: 37',\
                                        'Unnamed: 38','Unnamed: 39','Unnamed: 40','Unnamed: 41','Unnamed: 42','Unnamed: 43',\
                                        'Unnamed: 44','Unnamed: 45','Unnamed: 46','Unnamed: 47','Unnamed: 48']]
    dict = {'Cumulative Annual Energy (MWh) Savings - GROSS':'2022','Unnamed: 30':'2023','Unnamed: 31':'2024',\
        'Unnamed: 32':'2025','Unnamed: 33':'2026','Unnamed: 34':'2027','Unnamed: 35':'2028','Unnamed: 36':'2029',\
        'Unnamed: 37':'2030','Unnamed: 38':'2031','Unnamed: 39':'2032','Unnamed: 40':'2033','Unnamed: 41':'2034',\
        'Unnamed: 42':'2035','Unnamed: 43':'2036','Unnamed: 44':'2037','Unnamed: 45':'2038','Unnamed: 46':'2039',\
        'Unnamed: 47':'2040','Unnamed: 48':'2041','Realistic Achievable Potential By Measure':'Measure',\
       'Unnamed: 3':'Program'}
    Program_Savings.rename(columns=dict,inplace=True)

#condition for program name
    #Program_name = ['CAMR']
    Program_Savings = Program_Savings.loc[Program_Savings['Program'].isin([Program_name])] 
    # selecting rows based on program_name condition 
    
    Program_Savings = Program_Savings.reset_index(drop=True)

#display(Program_Savings)
    Savings_PerYear = (Program_Savings.sum(axis = 0, skipna =True))
    Savings_PerYear = Savings_PerYear.reset_index(drop = False)
    Savings_PerYear = Savings_PerYear.drop(Savings_PerYear.index[[0,1]])
    dict = {'index': 'Year', 0:'{} Market potential Savings'.format(Program_name)}
    Savings_PerYear.rename(columns=dict,inplace=True)
    Savings_PerYear = Savings_PerYear.reset_index(drop = True)
    Savings_PerYear['{} Market potential Savings'.format(Program_name)] = \
    Savings_PerYear['{} Market potential Savings'.format(Program_name)].div(1000)
#Savings_PerYear = Savings_PerYear.reset_index(drop = False)
#display(Savings_PerYear)
#display(Program_Savings.head())
    Title = Program_name + 'Market potential Savings'
    x = Savings_PerYear.plot('Year', '{} Market potential Savings'.format(Program_name) , xlabel='Year',ylabel='GWh')
    x.set_title('{} Market potential Savings'.format(Program_name))
    x.get_legend().remove()
#, kind = 'scatter')
    #return(x)
    return(Savings_PerYear)
#print(txt.format(price = 49))     
ipywidgets.interact(func1, Program_name = drop_down )
