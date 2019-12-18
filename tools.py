import pandas as pd
import numpy as np
import copy
def generate_measure_table(data, row_index, column_name, column_size):
    size_list = list(range(0,column_size))
    df = pd.DataFrame(data)
    # get mean and std of the column
    mean = df.iloc[:,size_list].mean().values.tolist()
    std = df.iloc[:,size_list].std().values.tolist()
    
    # add index for rows
    df = pd.DataFrame(data, index=row_index)
    
    # add division for mean and std
    df.loc['--------'] = ['--------','--------','--------']
    df.loc['avg     '] = mean
    df.loc['std'] = std
    
    # add column name
    df.columns = column_name
    return df


def generate_friedman_table(data, row_index, column_name, column_size, is_time):
    size_list = list(range(0,column_size))
    
    # create rank matrix 
    # generate friedman test table
    data_rank = copy.deepcopy(data)
    
    # turn the value into rank number
    if is_time == 0:
        for row in data_rank:
            s_row = sorted(enumerate(row), key=lambda x: x[1])
            idx = [i[0] for i in s_row]
            for index, or_index in enumerate(idx):
                row[or_index] = len(idx) - index
    else:
        for row in data_rank:
            s_row = sorted(enumerate(row), key=lambda x: x[1])
            idx = [i[0] for i in s_row]
            for index, or_index in enumerate(idx):
                row[or_index] = index + 1

    # get mean rank row
    df = pd.DataFrame(data_rank)
    mean = df.iloc[:,size_list].mean().values.tolist()

    # add index for rows
    df = pd.DataFrame(data_rank, index=row_index)
    
    # add division for mean and std
    df.loc['--------'] = ['--------','--------','--------']
    df.loc['avg_rank'] = mean
    
    # add column name
    df.columns = column_name
    return df
