# Purpose: 
# Author: Christian Copic, 2023

import os
import matplotlib.pyplot as plt
import pandas as pd


def main():
    cwd = os.getcwd()
    # Adding count for debugging purposes
    count = 0
    # Will have to change this line to be compatible with windows
    for file in os.listdir(cwd + '/devicedataset'):
        if count < 2:
            if file[-4:] == '.csv':
                data = pd.read_csv(cwd + '/devicedataset/' + file)
                device_name = file.split('[')[1].split(']')[0]
                make_graph(data, device_name)
                e_char(data, device_name)
                count = count + 1
        else:
            continue

# Create ID vs. VGS curves of data
def make_graph(data, device_name):
    #log y with regular x axis
    plt.semilogy(figsize=(9, 5))
    data['ID'] = data['ID'] * -1
    VD_values = data['VD'].unique()
    for i in range(len(VD_values)):
        subdf = data[data['VD'] == VD_values[i]]
        plt.plot(subdf['VG'], subdf['ID'], label = '$V_{DS}$ = ' + str(VD_values[i]) + 'V')
    
    # Use LaTeX for labels
    plt.xlabel('$V_{GS}$ (V)')
    plt.ylabel('$-I_{D}$ (A)')
    plt.title('$-I_{D}$ (A) vs. $V_{GS}$ (V) from ' + device_name)
    plt.legend()
    plt.show()

# Calculate electrical characteristics of device
def e_char(data, device_name):
    VD_values = data['VD'].unique()
    for i in range(len(VD_values)):
        subdf = data[data['VD'] == VD_values[i]]
        print('For VD = ' + str(VD_values[i]) + ' on device ' + device_name + ': ')
        print('Min Value: ' + str(subdf['ID'].min(0)))
        print('Max Value: ' + str(subdf['ID'].max(0)))
        print('Ion/Ioff ratio: ' + str(subdf['ID'].max(0) / subdf['ID'].min(0)))
        

if __name__ == '__main__':
    main()