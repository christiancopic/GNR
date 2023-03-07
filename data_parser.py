# Purpose: 
# Author: Christian Copic, 2023

import os
import matplotlib.pyplot as plt
import pandas as pd


def main():
    cwd = os.getcwd()
    # Will have to change this line to be compatible with windows
    count = 0
    for file in os.listdir(cwd + '/devicedataset'):
        if count < 2:
            if file[-4:] == '.csv':
                make_graph(file)
                count = count + 1
        else:
            continue

def make_graph(file):
    cwd = os.getcwd()
    data = pd.read_csv(cwd + '/devicedataset/' + file)
    plt.semilogy(figsize=(6.8, 4.2))
    data['ID'] = data['ID'] * -1
    VD_values = data['VD'].unique()
    #print(data)
    for i in range(len(VD_values)):
        subdf = data[data["VD"] == VD_values[i]]
        #print(subdf)
        plt.plot(subdf['VG'], subdf['ID'], label = '$V_{DS}$ = ' + str(VD_values[i]) + 'V')
    # Use LaTeX for labels
    plt.xlabel('$V_{GS}$ (V)')
    plt.ylabel('$-I_{D}$ (A)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()