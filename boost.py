# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:43:22 2022

@author: Mano
"""
import pandas as pd
data=pd.read_excel("C:/Users/Mano/Documents/imarticus/boost.xlsx")
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
stats.ttest_ind(data.AGE_BETWEENS_5_to_15,data.AGE_BETWEEN_16_to_25)#2sample t-test
