# -*- coding: utf-8 -*-
"""
Main File to convert bills 
"""

import pandas as pd
import numpy as np

ValueArray = np.zeros(50)

df = pd.read_excel (r'C:\Users\ACER\D2\Dev\011\Modelo.xlsx')
print(df)
CurrentLine= (df.iat[0, 0] )

for i in range(0, len(df)):
    CurrentLine= (df.iat[i, 0] )
    PosLine = CurrentLine.find("D", (len(CurrentLine)-7), len(CurrentLine))
    if PosLine != -1  and CurrentLine.find("UBER") != -1:
        NewLine = CurrentLine.replace(',', '.')
        ValueArray[i] =  (NewLine[(len(NewLine)-7):(len(NewLine)-2)])
        print (ValueArray[i])
       
        
        

