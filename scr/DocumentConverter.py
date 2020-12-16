# -*- coding: utf-8 -*-
"""
Main File to convert bills 
"""

import pandas as pd
df = pd.read_excel (r'C:\Users\ACER\D2\Dev\011\Modelo.xlsx')
print(df)
CurrentLine= (df.iat[0, 0] )
for i in range(0, len(df)):
    CurrentLine= (df.iat[i, 0] )
    DChar = CurrentLine.find("D", (len(CurrentLine)-5), len(CurrentLine))
    print (DChar)

