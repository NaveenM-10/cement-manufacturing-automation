# Cement Manufacturing Automation Project

![Cement Manufacturing Automation](https://www.cementequipment.org/wp-content/uploads/2018/04/img_5ae1ae733c6df-1.png)

## Project Overview

This project focuses on automating the cement quality inspection process to minimize inspection cycle time, reduce raw material wastage, and enhance overall production efficiency. By leveraging advanced technologies such as sensors, IoT devices, machine learning algorithms, and data visualization tools, this project aims to provide real-time insights for better decision-making.

## Table of Contents

- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Business Objective](#business-objective)
- [Business Constraint](#business-constraint)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Usage](#usage)
- [Dashboard](#interactive-dashboards)
- [Project Structure](#project-structure)


## Business Problem

Inspecting cement quality manually once per hour has drawbacks. If an issue arises between inspections, we cannot rectify it and must discard the cement produced during that period. Stopping production, inspecting machine components, and addressing any issues before resuming manufacturing leads to wasted raw material, increased machine downtime, and loss of revenue. Moreover, there is a risk of not meeting the demand.

## Business Objective

Minimize inspecting cycle time & minimize raw material wastage.

## Business Constraint

Minimize the manual effort.

## Tech Stack

- **Python**
- **MySQL**
- **Matplotlib**
- **Seaborn**
- **Power BI**
- **Looker Studio**
- **Excel**

## Features

- **Data Cleaning and Preprocessing**: Identification and removal of outliers, transforming the data, handling of missing values, and ensuring data consistency.
- **Data Exploration and Analysis**: In-depth analysis using Matplotlib and Seaborn to uncover patterns and insights.
- **Interactive Dashboards**: Dynamic dashboards created with Power BI, Looker Studio, and Excel for effective data visualization and reporting.

  

## Usage

1. Load the dataset:
    ```python
      # Pushing the Raw data into Mysql database 
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
    ```
<img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20201336.png"/>
From the Above image we can see that there are 5514 records and 28 features in the dataset.

2. Run the data cleaning and preprocessing scripts:
    ```python
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

    ```

3. Perform data exploration and visualization:
    ```python
      ### Vizualization ###
      ## The code shows the few sample visuals/charts of the features in the dataset ##
      import matplotlib.pyplot as plt
      import seaborn as sns
      
      sns.histplot(transformed_data['Mill_TPH'],kde=True)
      plt.title('Log Transformed')
      
      sns.histplot(transformed_data_yeojohnson['Mill_TPH'],kde=True)
      plt.title('YeoJohnson Transformation')
      
      sns.histplot(transformed_data['Clinker_TPH'],kde=True)
      plt.title('Log Transformed')
      
      sns.histplot(transformed_data_yeojohnson['Clinker_TPH'],kde=True)
      plt.title('YeoJohnson Transformation')
      
      sns.boxplot(raw_data['Mill_TPH'])
      plt.title('Before Outlier Treatment [Mill_TPH]')
      
      sns.boxplot(clean_data['Mill_TPH'])
      plt.title('After Outlier Treatment [Mill_TPH]')
      
      sns.boxplot(raw_data['Clinker_TPH'])
      plt.title('Before Outlier Treatment [Clinker_TPH]')
      
      sns.boxplot(clean_data['Clinker_TPH'])
      plt.title('After Outlier Treatment [Clinker_TPH]')
    ```

<img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20204212.png" width="300" height="300"/>  <img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20204224.png" width="300" height="300"/>

<img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20204233.png" width="300" height="300"/>  <img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20204249.png" width="300" height="300"/>

<img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20204448.png" width="300" height="300"/>  <img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20204459.png" width="300" height="300"/>

<img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20204507.png" width="300" height="300"/>  <img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20204517.png" width="300" height="300"/>

## Interactive dashboards:
    Open the Power BI / Looker Studio / Excel files in the `dashboards` directory to view the interactive visualizations.
# Power BI Dashboard
<img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20204827.png"/>

# Excel Dashboard
<img src="https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/Cement_manufacturing_automation/Screenshot%202024-07-06%20204827.png"/>

## Project Structure
Cement-Manufacturing-Automation/
- data/
  - raw_data.csv
- scripts/
  - data_cleaning.py
  - data_analysis.py
- dashboards/
  - dashboard.pbix
  - dashboard.looker
  - dashboard.xlsx
- images/
  - [charts.png](https://github.com/NaveenM-10/cement-manufacturing-automation/tree/main/Cement_manufacturing_automation)
  - [README.md](https://github.com/NaveenM-10/cement-manufacturing-automation/blob/main/README.md)
