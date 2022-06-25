# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 21:16:29 2022

@author: tanay
"""

#DATA Ingest from local drive

def data_ingest(dir):
    
    from os import chdir
    chdir(dir)

    import pandas as pd
    
    return(pd.read_csv("train.csv"), pd.read_csv("test.csv"))


train, test = data_ingest("C:\\Users\\tanay\\Documents\\GitHub\\House-Prices-Advanced-Regression-Techniques\\Data")
