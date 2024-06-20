# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:48:07 2024

@author: Naveen
"""

import pandas as pd

from sqlalchemy import create_engine

import pymysql

engine=create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                     .format(user='root',
                             pw='password',
                             db='cement_manufacturing'))
sql="select * from cement"

sql1="select * from cement_treated"

raw_data=pd.read_sql_query(sql, engine)

clean_data=pd.read_sql_query(sql1, engine)

### EDA BEFOR DATA PRE-PROCESSING
###  FIRST MOMENT BUSINESS DECISION

# MEAN
raw_data['Mill_TPH'].mean()
raw_data['Clinker_TPH'].mean()
raw_data['Gypsum_TPH'].mean()
raw_data['DFA_TPH'].mean()
raw_data['WFA_TPH'].mean()
raw_data['Mill_KW'].mean()
raw_data['Mill_IL_Temp'].mean()
raw_data['Mill_OL_Temp'].mean()
raw_data['Mill_OL_BE_Amp'].mean()
raw_data['Mill_Vent_Fan_RPM'].mean()
raw_data['Mill_Vent_Fan_KW'].mean()
raw_data['Mill_Vent_BF_IL_Draft'].mean()
raw_data['Mill_Vent_BF_OL_Draft'].mean()
raw_data['Reject'].mean()
raw_data['Sep_RPM'].mean()
raw_data['Sep_KW'].mean()
raw_data['Sep_Amp'].mean()
raw_data['CA_Fan_RPM'].mean()
raw_data['CA_Fan_KW'].mean()
raw_data['Mill_Folaphone'].mean()
raw_data['Mill_IL_Draft'].mean()
raw_data['Mill_OL_Draft'].mean()
raw_data['Sep_Vent_IL_Draft'].mean()
raw_data['Sep_Vent_OL_Draft'].mean()
raw_data['Sep_Vent_bag_filter_fan_kw'].mean()
raw_data['Sep_Vent_bag_filter_fan_rpm'].mean()
raw_data['Residue'].mean()

# MEDIAN
raw_data['Mill_TPH'].median()
raw_data['Clinker_TPH'].median()
raw_data['Gypsum_TPH'].median()
raw_data['DFA_TPH'].median()
raw_data['WFA_TPH'].median()
raw_data['Mill_KW'].median()
raw_data['Mill_IL_Temp'].median()
raw_data['Mill_OL_Temp'].median()
raw_data['Mill_OL_BE_Amp'].median()
raw_data['Mill_Vent_Fan_RPM'].median()
raw_data['Mill_Vent_Fan_KW'].median()
raw_data['Mill_Vent_BF_IL_Draft'].median()
raw_data['Mill_Vent_BF_OL_Draft'].median()
raw_data['Reject'].median()
raw_data['Sep_RPM'].median()
raw_data['Sep_KW'].median()
raw_data['Sep_Amp'].median()
raw_data['CA_Fan_RPM'].median()
raw_data['CA_Fan_KW'].median()
raw_data['Mill_Folaphone'].median()
raw_data['Mill_IL_Draft'].median()
raw_data['Mill_OL_Draft'].median()
raw_data['Sep_Vent_IL_Draft'].median()
raw_data['Sep_Vent_OL_Draft'].median()
raw_data['Sep_Vent_bag_filter_fan_kw'].median()
raw_data['Sep_Vent_bag_filter_fan_rpm'].median()
raw_data['Residue'].median()

# MODE 
raw_data['Mill_TPH'].mode()
raw_data['Clinker_TPH'].mode()
raw_data['Gypsum_TPH'].mode()
raw_data['DFA_TPH'].mode()
raw_data['WFA_TPH'].mode()
raw_data['Mill_KW'].mode()
raw_data['Mill_IL_Temp'].mode()
raw_data['Mill_OL_Temp'].mode()
raw_data['Mill_OL_BE_Amp'].mode()
raw_data['Mill_Vent_Fan_RPM'].mode()
raw_data['Mill_Vent_Fan_KW'].mode()
raw_data['Mill_Vent_BF_IL_Draft'].mode()
raw_data['Mill_Vent_BF_OL_Draft'].mode()
raw_data['Reject'].mode()
raw_data['Sep_RPM'].mode()
raw_data['Sep_KW'].mode()
raw_data['Sep_Amp'].mode()
raw_data['CA_Fan_RPM'].mode()
raw_data['CA_Fan_KW'].mode()
raw_data['Mill_Folaphone'].mode()
raw_data['Mill_IL_Draft'].mode()
raw_data['Mill_OL_Draft'].mode()
raw_data['Sep_Vent_IL_Draft'].mode()
raw_data['Sep_Vent_OL_Draft'].mode()
raw_data['Sep_Vent_bag_filter_fan_kw'].mode()
raw_data['Sep_Vent_bag_filter_fan_rpm'].mode()
raw_data['Residue'].mode()

### SECOND MOMENT BUSINESS DECISION
## STANDARD DEVIATION
raw_data['Mill_TPH'].std()
raw_data['Clinker_TPH'].std()
raw_data['Gypsum_TPH'].std()
raw_data['DFA_TPH'].std()
raw_data['WFA_TPH'].std()
raw_data['Mill_KW'].std()
raw_data['Mill_IL_Temp'].std()
raw_data['Mill_OL_Temp'].std()
raw_data['Mill_OL_BE_Amp'].std()
raw_data['Mill_Vent_Fan_RPM'].std()
raw_data['Mill_Vent_Fan_KW'].std()
raw_data['Mill_Vent_BF_IL_Draft'].std()
raw_data['Mill_Vent_BF_OL_Draft'].std()
raw_data['Reject'].std()
raw_data['Sep_RPM'].std()
raw_data['Sep_KW'].std()
raw_data['Sep_Amp'].std()
raw_data['CA_Fan_RPM'].std()
raw_data['CA_Fan_KW'].std()
raw_data['Mill_Folaphone'].std()
raw_data['Mill_IL_Draft'].std()
raw_data['Mill_OL_Draft'].std()
raw_data['Sep_Vent_IL_Draft'].std()
raw_data['Sep_Vent_OL_Draft'].std()
raw_data['Sep_Vent_bag_filter_fan_kw'].std()
raw_data['Sep_Vent_bag_filter_fan_rpm'].std()
raw_data['Residue'].std()

## VARIANCE 
raw_data['Mill_TPH'].var()
raw_data['Clinker_TPH'].var()
raw_data['Gypsum_TPH'].var()
raw_data['DFA_TPH'].var()
raw_data['WFA_TPH'].var()
raw_data['Mill_KW'].var()
raw_data['Mill_IL_Temp'].var()
raw_data['Mill_OL_Temp'].var()
raw_data['Mill_OL_BE_Amp'].var()
raw_data['Mill_Vent_Fan_RPM'].var()
raw_data['Mill_Vent_Fan_KW'].var()
raw_data['Mill_Vent_BF_IL_Draft'].var()
raw_data['Mill_Vent_BF_OL_Draft'].var()
raw_data['Reject'].var()
raw_data['Sep_RPM'].var()
raw_data['Sep_KW'].var()
raw_data['Sep_Amp'].var()
raw_data['CA_Fan_RPM'].var()
raw_data['CA_Fan_KW'].var()
raw_data['Mill_Folaphone'].var()
raw_data['Mill_IL_Draft'].var()
raw_data['Mill_OL_Draft'].var()
raw_data['Sep_Vent_IL_Draft'].var()
raw_data['Sep_Vent_OL_Draft'].var()
raw_data['Sep_Vent_bag_filter_fan_kw'].var()
raw_data['Sep_Vent_bag_filter_fan_rpm'].var()
raw_data['Residue'].var()

# RANGE
raw_data['Mill_TPH'].max()-raw_data['Mill_TPH'].min()
raw_data['Clinker_TPH'].max()-raw_data['Clinker_TPH'].min()
raw_data['Gypsum_TPH'].max()-raw_data['Gypsum_TPH'].min()
raw_data['DFA_TPH'].max()-raw_data['DFA_TPH'].min()
raw_data['WFA_TPH'].max()-raw_data['WFA_TPH'].min()
raw_data['Mill_KW'].max()-raw_data['Mill_KW'].min()
raw_data['Mill_IL_Temp'].max()-raw_data['Mill_IL_Temp'].min()
raw_data['Mill_OL_Temp'].max()-raw_data['Mill_OL_Temp'].min()
raw_data['Mill_OL_BE_Amp'].max()-raw_data['Mill_OL_BE_Amp'].min()
raw_data['Mill_Vent_Fan_RPM'].max()-raw_data['Mill_Vent_Fan_RPM'].min()
raw_data['Mill_Vent_Fan_KW'].max()-raw_data['Mill_Vent_Fan_KW'].min()
raw_data['Mill_Vent_BF_OL_Draft'].max()-raw_data['Mill_Vent_BF_OL_Draft'].min()
raw_data['Mill_Vent_BF_IL_Draft'].max()-raw_data['Mill_Vent_BF_IL_Draft'].min()
raw_data['Reject'].max()-raw_data['Reject'].min()
raw_data['Sep_RPM'].max()-raw_data['Sep_RPM'].min()
raw_data['Sep_KW'].max()-raw_data['Sep_KW'].min()
raw_data['Sep_Amp'].max()-raw_data['Sep_Amp'].min()
raw_data['CA_Fan_RPM'].max()-raw_data['CA_Fan_RPM'].min()
raw_data['CA_Fan_KW'].max()-raw_data['CA_Fan_KW'].min()
raw_data['Mill_Folaphone'].max()-raw_data['Mill_Folaphone'].min()
raw_data['Mill_IL_Draft'].max()-raw_data['Mill_IL_Draft'].min()
raw_data['Mill_OL_Draft'].max()-raw_data['Mill_OL_Draft'].min()
raw_data['Sep_Vent_IL_Draft'].max()-raw_data['Sep_Vent_IL_Draft'].min()
raw_data['Sep_Vent_OL_Draft'].max()-raw_data['Sep_Vent_OL_Draft'].min()
raw_data['Sep_Vent_bag_filter_fan_kw'].max()-raw_data['Sep_Vent_bag_filter_fan_kw'].min()
raw_data['Sep_Vent_bag_filter_fan_rpm'].max()-raw_data['Sep_Vent_bag_filter_fan_rpm'].min()
raw_data['Residue'].max()-raw_data['Residue'].min()

### THIRD MOMENT BUSINESS DECISION
## SKEWNESS
raw_data['Mill_TPH'].skew()
raw_data['Clinker_TPH'].skew()
raw_data['Gypsum_TPH'].skew()
raw_data['DFA_TPH'].skew()
raw_data['WFA_TPH'].skew()
raw_data['Mill_KW'].skew()
raw_data['Mill_IL_Temp'].skew()
raw_data['Mill_OL_Temp'].skew()
raw_data['Mill_OL_BE_Amp'].skew()
raw_data['Mill_Vent_Fan_RPM'].skew()
raw_data['Mill_Vent_Fan_KW'].skew()
raw_data['Mill_Vent_BF_IL_Draft'].skew()
raw_data['Mill_Vent_BF_OL_Draft'].skew()
raw_data['Reject'].skew()
raw_data['Sep_RPM'].skew()
raw_data['Sep_KW'].skew()
raw_data['Sep_Amp'].skew()
raw_data['CA_Fan_RPM'].skew()
raw_data['CA_Fan_KW'].skew()
raw_data['Mill_Folaphone'].skew()
raw_data['Mill_IL_Draft'].skew()
raw_data['Mill_OL_Draft'].skew()
raw_data['Sep_Vent_IL_Draft'].skew()
raw_data['Sep_Vent_OL_Draft'].skew()
raw_data['Sep_Vent_bag_filter_fan_kw'].skew()
raw_data['Sep_Vent_bag_filter_fan_rpm'].skew()
raw_data['Residue'].skew()

### FOURTH MOMENT BUSINESS DECISION
## KURTOSIS
raw_data['Mill_TPH'].kurt()
raw_data['Clinker_TPH'].kurt()
raw_data['Gypsum_TPH'].kurt()
raw_data['DFA_TPH'].kurt()
raw_data['WFA_TPH'].kurt()
raw_data['Mill_KW'].kurt()
raw_data['Mill_IL_Temp'].kurt()
raw_data['Mill_OL_Temp'].kurt()
raw_data['Mill_OL_BE_Amp'].kurt()
raw_data['Mill_Vent_Fan_RPM'].kurt()
raw_data['Mill_Vent_Fan_KW'].kurt()
raw_data['Mill_Vent_BF_IL_Draft'].kurt()
raw_data['Mill_Vent_BF_OL_Draft'].kurt()
raw_data['Reject'].kurt()
raw_data['Sep_RPM'].kurt()
raw_data['Sep_KW'].kurt()
raw_data['Sep_Amp'].kurt()
raw_data['CA_Fan_RPM'].kurt()
raw_data['CA_Fan_KW'].kurt()
raw_data['Mill_Folaphone'].kurt()
raw_data['Mill_IL_Draft'].kurt()
raw_data['Mill_OL_Draft'].kurt()
raw_data['Sep_Vent_IL_Draft'].kurt()
raw_data['Sep_Vent_OL_Draft'].kurt()
raw_data['Sep_Vent_bag_filter_fan_kw'].kurt()
raw_data['Sep_Vent_bag_filter_fan_rpm'].kurt()
raw_data['Residue'].kurt()

################################# DATA PRE-PROCESSING    ####################################
##### HANDLING DUPLICATES 
raw_data.duplicated().sum()
## The above code shows that the data has no duplicates

### MISSING DATA 
raw_data.isna().sum()
## This line of code shows that there are missing values the data

### HANDLING OUTLIERS 
mill_tph_q1 = raw_data['Mill_TPH'].quantile(0.25)
mill_tph_q3 = raw_data['Mill_TPH'].quantile(0.75)
mill_tph_iqr = mill_tph_q3-mill_tph_q1
mill_tph_ul = mill_tph_q3 + 1.5 * mill_tph_iqr
mill_tph_ll = mill_tph_q1 - 1.5 * mill_tph_iqr
mill_tph_outliers = raw_data[(raw_data['Mill_TPH'] > mill_tph_ul) | (raw_data['Mill_TPH'] < mill_tph_ll)]
# It shows that Mill_TPH column has 153 outliers present in the data

clinker_tph_q1 = raw_data['Clinker_TPH'].quantile(0.25)
clinker_tph_q3 = raw_data['Clinker_TPH'].quantile(0.75)
clinker_tph_iqr = clinker_tph_q3-clinker_tph_q1
clinker_tph_ul = clinker_tph_q3 + 1.5 * clinker_tph_iqr
clinker_tph_ll = clinker_tph_q1 - 1.5 * clinker_tph_iqr
clinker_tph_outliers = raw_data[(raw_data['Clinker_TPH'] > clinker_tph_ul) | (raw_data['Clinker_TPH'] < clinker_tph_ll)]
# There are 143 outliers  present in the data

from feature_engine.outliers import Winsorizer
winsor_percentile= Winsorizer(capping_method='iqr',tail='both', fold=1.5 )
df=winsor_percentile.fit_transform(raw_data[['Mill_TPH', 'Clinker_TPH', 'Gypsum_TPH', 'DFA_TPH',
       'WFA_TPH', 'Mill_KW', 'Mill_IL_Temp', 'Mill_OL_Temp', 'Mill_OL_BE_Amp',
       'Mill_Vent_Fan_RPM', 'Mill_Vent_Fan_KW', 'Mill_Vent_BF_IL_Draft',
       'Mill_Vent_BF_OL_Draft', 'Reject', 'Sep_RPM', 'Sep_KW', 'Sep_Amp',
       'CA_Fan_RPM', 'CA_Fan_KW', 'Mill_Folaphone', 'Mill_IL_Draft',
       'Mill_OL_Draft', 'Sep_Vent_IL_Draft', 'Sep_Vent_OL_Draft',
       'Sep_Vent_bag_filter_fan_kw', 'Sep_Vent_bag_filter_fan_rpm', 'Residue']])

clean_data=pd.concat([raw_data[['Date_Time']],df],axis=1)

#### Transformation 
import numpy as np
transformed_data=np.log(clean_data[['Mill_TPH', 'Clinker_TPH', 'Gypsum_TPH', 'DFA_TPH',
       'WFA_TPH', 'Mill_KW', 'Mill_IL_Temp', 'Mill_OL_Temp', 'Mill_OL_BE_Amp',
       'Mill_Vent_Fan_RPM', 'Mill_Vent_Fan_KW', 'Mill_Vent_BF_IL_Draft',
       'Mill_Vent_BF_OL_Draft', 'Reject', 'Sep_RPM', 'Sep_KW', 'Sep_Amp',
       'CA_Fan_RPM', 'CA_Fan_KW', 'Mill_Folaphone', 'Mill_IL_Draft',
       'Mill_OL_Draft', 'Sep_Vent_IL_Draft', 'Sep_Vent_OL_Draft',
       'Sep_Vent_bag_filter_fan_kw', 'Sep_Vent_bag_filter_fan_rpm', 'Residue']])

## YEOJOHNSON TRANSFORMATION
from feature_engine import transformation
tf=transformation.YeoJohnsonTransformer()
transformed_data_yeojohnson=tf.fit_transform(clean_data[['Mill_TPH', 'Clinker_TPH', 'Gypsum_TPH', 'DFA_TPH',
       'WFA_TPH', 'Mill_KW', 'Mill_IL_Temp', 'Mill_OL_Temp', 'Mill_OL_BE_Amp',
       'Mill_Vent_Fan_RPM', 'Mill_Vent_Fan_KW', 'Mill_Vent_BF_IL_Draft',
       'Mill_Vent_BF_OL_Draft', 'Reject', 'Sep_RPM', 'Sep_KW', 'Sep_Amp',
       'CA_Fan_RPM', 'CA_Fan_KW', 'Mill_Folaphone', 'Mill_IL_Draft',
       'Mill_OL_Draft', 'Sep_Vent_IL_Draft', 'Sep_Vent_OL_Draft',
       'Sep_Vent_bag_filter_fan_kw', 'Sep_Vent_bag_filter_fan_rpm', 'Residue']])


###### DATA SCALING
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
scaled_data=pd.DataFrame(sc.fit_transform(clean_data[['Mill_TPH', 'Clinker_TPH', 'Gypsum_TPH', 'DFA_TPH',
       'WFA_TPH', 'Mill_KW', 'Mill_IL_Temp', 'Mill_OL_Temp', 'Mill_OL_BE_Amp',
       'Mill_Vent_Fan_RPM', 'Mill_Vent_Fan_KW', 'Mill_Vent_BF_IL_Draft',
       'Mill_Vent_BF_OL_Draft', 'Reject', 'Sep_RPM', 'Sep_KW', 'Sep_Amp',
       'CA_Fan_RPM', 'CA_Fan_KW', 'Mill_Folaphone', 'Mill_IL_Draft',
       'Mill_OL_Draft', 'Sep_Vent_IL_Draft', 'Sep_Vent_OL_Draft',
       'Sep_Vent_bag_filter_fan_kw', 'Sep_Vent_bag_filter_fan_rpm', 'Residue']]))

##### EDA AFTER DATA PRE-PROCESSING
###  FIRST MOMENT BUSINESS DECISION

# MEAN
clean_data['Mill_TPH'].mean()
clean_data['Clinker_TPH'].mean()
clean_data['Gypsum_TPH'].mean()
clean_data['DFA_TPH'].mean()
clean_data['WFA_TPH'].mean()
clean_data['Mill_KW'].mean()
clean_data['Mill_IL_Temp'].mean()
clean_data['Mill_OL_Temp'].mean()
clean_data['Mill_OL_BE_Amp'].mean()
clean_data['Mill_Vent_Fan_RPM'].mean()
clean_data['Mill_Vent_Fan_KW'].mean()
clean_data['Mill_Vent_BF_IL_Draft'].mean()
clean_data['Mill_Vent_BF_OL_Draft'].mean()
clean_data['Reject'].mean()
clean_data['Sep_RPM'].mean()
clean_data['Sep_KW'].mean()
clean_data['Sep_Amp'].mean()
clean_data['CA_Fan_RPM'].mean()
clean_data['CA_Fan_KW'].mean()
clean_data['Mill_Folaphone'].mean()
clean_data['Mill_IL_Draft'].mean()
clean_data['Mill_OL_Draft'].mean()
clean_data['Sep_Vent_IL_Draft'].mean()
clean_data['Sep_Vent_OL_Draft'].mean()
clean_data['Sep_Vent_bag_filter_fan_kw'].mean()
clean_data['Sep_Vent_bag_filter_fan_rpm'].mean()
clean_data['Residue'].mean()

# MEDIAN
clean_data['Mill_TPH'].median()
clean_data['Clinker_TPH'].median()
clean_data['Gypsum_TPH'].median()
clean_data['DFA_TPH'].median()
clean_data['WFA_TPH'].median()
clean_data['Mill_KW'].median()
clean_data['Mill_IL_Temp'].median()
clean_data['Mill_OL_Temp'].median()
clean_data['Mill_OL_BE_Amp'].median()
clean_data['Mill_Vent_Fan_RPM'].median()
clean_data['Mill_Vent_Fan_KW'].median()
clean_data['Mill_Vent_BF_IL_Draft'].median()
clean_data['Mill_Vent_BF_OL_Draft'].median()
clean_data['Reject'].median()
clean_data['Sep_RPM'].median()
clean_data['Sep_KW'].median()
clean_data['Sep_Amp'].median()
clean_data['CA_Fan_RPM'].median()
clean_data['CA_Fan_KW'].median()
clean_data['Mill_Folaphone'].median()
clean_data['Mill_IL_Draft'].median()
clean_data['Mill_OL_Draft'].median()
clean_data['Sep_Vent_IL_Draft'].median()
clean_data['Sep_Vent_OL_Draft'].median()
clean_data['Sep_Vent_bag_filter_fan_kw'].median()
clean_data['Sep_Vent_bag_filter_fan_rpm'].median()
clean_data['Residue'].median()

# MODE 
clean_data['Mill_TPH'].mode()
clean_data['Clinker_TPH'].mode()
clean_data['Gypsum_TPH'].mode()
clean_data['DFA_TPH'].mode()
clean_data['WFA_TPH'].mode()
clean_data['Mill_KW'].mode()
clean_data['Mill_IL_Temp'].mode()
clean_data['Mill_OL_Temp'].mode()
clean_data['Mill_OL_BE_Amp'].mode()
clean_data['Mill_Vent_Fan_RPM'].mode()
clean_data['Mill_Vent_Fan_KW'].mode()
clean_data['Mill_Vent_BF_IL_Draft'].mode()
clean_data['Mill_Vent_BF_OL_Draft'].mode()
clean_data['Reject'].mode()
clean_data['Sep_RPM'].mode()
clean_data['Sep_KW'].mode()
clean_data['Sep_Amp'].mode()
clean_data['CA_Fan_RPM'].mode()
clean_data['CA_Fan_KW'].mode()
clean_data['Mill_Folaphone'].mode()
clean_data['Mill_IL_Draft'].mode()
clean_data['Mill_OL_Draft'].mode()
clean_data['Sep_Vent_IL_Draft'].mode()
clean_data['Sep_Vent_OL_Draft'].mode()
clean_data['Sep_Vent_bag_filter_fan_kw'].mode()
clean_data['Sep_Vent_bag_filter_fan_rpm'].mode()
clean_data['Residue'].mode()

### SECOND MOMENT BUSINESS DECISION
## STANDARD DEVIATION
clean_data['Mill_TPH'].std()
clean_data['Clinker_TPH'].std()
clean_data['Gypsum_TPH'].std()
clean_data['DFA_TPH'].std()
clean_data['WFA_TPH'].std()
clean_data['Mill_KW'].std()
clean_data['Mill_IL_Temp'].std()
clean_data['Mill_OL_Temp'].std()
clean_data['Mill_OL_BE_Amp'].std()
clean_data['Mill_Vent_Fan_RPM'].std()
clean_data['Mill_Vent_Fan_KW'].std()
clean_data['Mill_Vent_BF_IL_Draft'].std()
clean_data['Mill_Vent_BF_OL_Draft'].std()
clean_data['Reject'].std()
clean_data['Sep_RPM'].std()
clean_data['Sep_KW'].std()
clean_data['Sep_Amp'].std()
clean_data['CA_Fan_RPM'].std()
clean_data['CA_Fan_KW'].std()
clean_data['Mill_Folaphone'].std()
clean_data['Mill_IL_Draft'].std()
clean_data['Mill_OL_Draft'].std()
clean_data['Sep_Vent_IL_Draft'].std()
clean_data['Sep_Vent_OL_Draft'].std()
clean_data['Sep_Vent_bag_filter_fan_kw'].std()
clean_data['Sep_Vent_bag_filter_fan_rpm'].std()
clean_data['Residue'].std()

## VARIANCE 
clean_data['Mill_TPH'].var()
clean_data['Clinker_TPH'].var()
clean_data['Gypsum_TPH'].var()
clean_data['DFA_TPH'].var()
clean_data['WFA_TPH'].var()
clean_data['Mill_KW'].var()
clean_data['Mill_IL_Temp'].var()
clean_data['Mill_OL_Temp'].var()
clean_data['Mill_OL_BE_Amp'].var()
clean_data['Mill_Vent_Fan_RPM'].var()
clean_data['Mill_Vent_Fan_KW'].var()
clean_data['Mill_Vent_BF_IL_Draft'].var()
clean_data['Mill_Vent_BF_OL_Draft'].var()
clean_data['Reject'].var()
clean_data['Sep_RPM'].var()
clean_data['Sep_KW'].var()
clean_data['Sep_Amp'].var()
clean_data['CA_Fan_RPM'].var()
clean_data['CA_Fan_KW'].var()
clean_data['Mill_Folaphone'].var()
clean_data['Mill_IL_Draft'].var()
clean_data['Mill_OL_Draft'].var()
clean_data['Sep_Vent_IL_Draft'].var()
clean_data['Sep_Vent_OL_Draft'].var()
clean_data['Sep_Vent_bag_filter_fan_kw'].var()
clean_data['Sep_Vent_bag_filter_fan_rpm'].var()
clean_data['Residue'].var()

# RANGE
clean_data['Mill_TPH'].max()-clean_data['Mill_TPH'].min()
clean_data['Clinker_TPH'].max()-clean_data['Clinker_TPH'].min()
clean_data['Gypsum_TPH'].max()-clean_data['Gypsum_TPH'].min()
clean_data['DFA_TPH'].max()-clean_data['DFA_TPH'].min()
clean_data['WFA_TPH'].max()-clean_data['WFA_TPH'].min()
clean_data['Mill_KW'].max()-clean_data['Mill_KW'].min()
clean_data['Mill_IL_Temp'].max()-clean_data['Mill_IL_Temp'].min()
clean_data['Mill_OL_Temp'].max()-clean_data['Mill_OL_Temp'].min()
clean_data['Mill_OL_BE_Amp'].max()-clean_data['Mill_OL_BE_Amp'].min()
clean_data['Mill_Vent_Fan_RPM'].max()-clean_data['Mill_Vent_Fan_RPM'].min()
clean_data['Mill_Vent_Fan_KW'].max()-clean_data['Mill_Vent_Fan_KW'].min()
clean_data['Mill_Vent_BF_OL_Draft'].max()-clean_data['Mill_Vent_BF_OL_Draft'].min()
clean_data['Mill_Vent_BF_IL_Draft'].max()-clean_data['Mill_Vent_BF_IL_Draft'].min()
clean_data['Reject'].max()-clean_data['Reject'].min()
clean_data['Sep_RPM'].max()-clean_data['Sep_RPM'].min()
clean_data['Sep_KW'].max()-clean_data['Sep_KW'].min()
clean_data['Sep_Amp'].max()-clean_data['Sep_Amp'].min()
clean_data['CA_Fan_RPM'].max()-clean_data['CA_Fan_RPM'].min()
clean_data['CA_Fan_KW'].max()-clean_data['CA_Fan_KW'].min()
clean_data['Mill_Folaphone'].max()-clean_data['Mill_Folaphone'].min()
clean_data['Mill_IL_Draft'].max()-clean_data['Mill_IL_Draft'].min()
clean_data['Mill_OL_Draft'].max()-clean_data['Mill_OL_Draft'].min()
clean_data['Sep_Vent_IL_Draft'].max()-clean_data['Sep_Vent_IL_Draft'].min()
clean_data['Sep_Vent_OL_Draft'].max()-clean_data['Sep_Vent_OL_Draft'].min()
clean_data['Sep_Vent_bag_filter_fan_kw'].max()-clean_data['Sep_Vent_bag_filter_fan_kw'].min()
clean_data['Sep_Vent_bag_filter_fan_rpm'].max()-clean_data['Sep_Vent_bag_filter_fan_rpm'].min()
clean_data['Residue'].max()-clean_data['Residue'].min()

### THIRD MOMENT BUSINESS DECISION
## SKEWNESS
clean_data['Mill_TPH'].skew()
clean_data['Clinker_TPH'].skew()
clean_data['Gypsum_TPH'].skew()
clean_data['DFA_TPH'].skew()
clean_data['WFA_TPH'].skew()
clean_data['Mill_KW'].skew()
clean_data['Mill_IL_Temp'].skew()
clean_data['Mill_OL_Temp'].skew()
clean_data['Mill_OL_BE_Amp'].skew()
clean_data['Mill_Vent_Fan_RPM'].skew()
clean_data['Mill_Vent_Fan_KW'].skew()
clean_data['Mill_Vent_BF_IL_Draft'].skew()
clean_data['Mill_Vent_BF_OL_Draft'].skew()
clean_data['Reject'].skew()
clean_data['Sep_RPM'].skew()
clean_data['Sep_KW'].skew()
clean_data['Sep_Amp'].skew()
clean_data['CA_Fan_RPM'].skew()
clean_data['CA_Fan_KW'].skew()
clean_data['Mill_Folaphone'].skew()
clean_data['Mill_IL_Draft'].skew()
clean_data['Mill_OL_Draft'].skew()
clean_data['Sep_Vent_IL_Draft'].skew()
clean_data['Sep_Vent_OL_Draft'].skew()
clean_data['Sep_Vent_bag_filter_fan_kw'].skew()
clean_data['Sep_Vent_bag_filter_fan_rpm'].skew()
clean_data['Residue'].skew()

### FOURTH MOMENT BUSINESS DECISION
## KURTOSIS
clean_data['Mill_TPH'].kurt()
clean_data['Clinker_TPH'].kurt()
clean_data['Gypsum_TPH'].kurt()
clean_data['DFA_TPH'].kurt()
clean_data['WFA_TPH'].kurt()
clean_data['Mill_KW'].kurt()
clean_data['Mill_IL_Temp'].kurt()
clean_data['Mill_OL_Temp'].kurt()
clean_data['Mill_OL_BE_Amp'].kurt()
clean_data['Mill_Vent_Fan_RPM'].kurt()
clean_data['Mill_Vent_Fan_KW'].kurt()
clean_data['Mill_Vent_BF_IL_Draft'].kurt()
clean_data['Mill_Vent_BF_OL_Draft'].kurt()
clean_data['Reject'].kurt()
clean_data['Sep_RPM'].kurt()
clean_data['Sep_KW'].kurt()
clean_data['Sep_Amp'].kurt()
clean_data['CA_Fan_RPM'].kurt()
clean_data['CA_Fan_KW'].kurt()
clean_data['Mill_Folaphone'].kurt()
clean_data['Mill_IL_Draft'].kurt()
clean_data['Mill_OL_Draft'].kurt()
clean_data['Sep_Vent_IL_Draft'].kurt()
clean_data['Sep_Vent_OL_Draft'].kurt()
clean_data['Sep_Vent_bag_filter_fan_kw'].kurt()
clean_data['Sep_Vent_bag_filter_fan_rpm'].kurt()
clean_data['Residue'].kurt()

### AUTO EDA
## 1 SWEETVIZ
import sweetviz as sv
s=sv.analyze(raw_data)
s.show_html()

## 2 DTALE
import dtale
d=dtale.show(raw_data)
d.open_browser()

## 3 AUTOVIZ
from autoviz.AutoViz_Class import AutoViz_Class
av=AutoViz_Class()
a=av.AutoViz("C:/Users/Naveen/Desktop/cement_treated.csv",chart_format='html')

## 4 YDATA_PROFILING
# pip install ydata_profiling
from ydata_profiling import ProfileReport
p=ProfileReport(raw_data)
p.to_file("out_html")

## 5 DATAPREP
from dataprep.eda import create_report
report=create_report(raw_data,title='my report')
report.save('dataprep.html')
