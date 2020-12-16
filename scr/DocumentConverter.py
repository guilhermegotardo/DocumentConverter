# -*- coding: utf-8 -*-
"""
Main File to convert bills 
"""

import pandas as pd
df = pd.read_excel (r'C:\Users\ACER\D2\Dev\011\Modelo.xlsx')
CurrentLine= (df.iat[0, 0] )
DChar = CurrentLine.find("D", (len(CurrentLine)-5), len(CurrentLine))
print (DChar)

