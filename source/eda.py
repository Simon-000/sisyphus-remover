#TODO: write docstring using Google conventions

import pandas as pd

def assess_data_frame_quality(raw_data_frame, dataset_name):
    display("Data quality assessment for `%s`:" % dataset_name)
    
    display("Top 20 observations:")
    display(raw_data_frame.head(20))
    
    display("Bottom 20 observations:")
    display(raw_data_frame.tail(20))
    
    display("Data types:")
    display(raw_data_frame.info())
    
    display("Summary statistics:")
    display(raw_data_frame.describe())
    
    display("Prevalence of missing values:")
    
    # Calculate number and proportion of null values across all features
    missing_values = raw_data_frame.isnull().sum()
    percent_missing_values = 100 * raw_data_frame.isnull().sum() / len(raw_data_frame)
    missing_values_table = pd.concat([missing_values, percent_missing_values], axis=1)
    missing_values_table_columns = missing_values_table.rename(columns = {0 : 'Missing Values', 1 : '% of Total Values'})
    missing_values_table_columns = missing_values_table_columns[missing_values_table_columns.iloc[:,1] != 0].sort_values('% of Total Values', ascending=False).round(1)
    display("Your selected dataframe has %s columns. There are %s columns that have missing values." % (str(raw_data_frame.shape[1]), str(missing_values_table_columns.shape[0])))
    display(missing_values_table_columns)