# Purpose: 
# Author: Christian Copic, 2023

import os
import matplotlib.pyplot as plt
import pandas as pd
from pptx import Presentation
from pptx.util import Inches


def main():
    cwd = os.getcwd()
    # Adding count for debugging purposes
    count = 0
    # Will have to change this line to be compatible with windows
    for file in os.listdir(cwd + '/devicedataset'):
        if count < 200:
            if file[-4:] == '.csv':
                data = pd.read_csv(cwd + '/devicedataset/' + file)
                device_name = file.split('[')[1].split(']')[0].split(' ')[0]
                make_graph(data, device_name)
                e_char(data, device_name)

                count = count + 1
        else:
            continue
    create_pptx()

# Create ID vs. VGS curves of data
def make_graph(data, device_name):
    #log y with regular x axis
    plt.semilogy(figsize=(9, 5))

    data['ID'] = abs(data['ID'])
    VD_values = data['VD'].unique()

    for i in range(len(VD_values)):
        subdf = data[data['VD'] == VD_values[i]]
        plt.plot(subdf['VG'], subdf['ID'], label = '$V_{DS}$ = ' + str(VD_values[i]) + 'V')
    
    # Use LaTeX for labels
    plt.xlabel('$V_{GS}$ (V)')
    plt.ylabel('$-I_{D}$ (A)')
    plt.title('$-I_{D}$ (A) vs. $V_{GS}$ (V) from ' + device_name)
    plt.legend()
    plt.savefig(device_name + '.png')
    plt.close()

    #save to into pptx file code here:

# Calculate electrical characteristics of device
def e_char(data, device_name):
    VD_values = data['VD'].unique()
    for i in range(len(VD_values)):
        subdf = data[data['VD'] == VD_values[i]]
        print('For VD = ' + str(VD_values[i]) + ' on device ' + device_name + ': ')
        print('Min ID Value: ' + str(subdf['ID'].min(0)))
        print('Max ID Value: ' + str(subdf['ID'].max(0)))
        print('Ion/Ioff ratio: ' + str(subdf['ID'].max(0) / subdf['ID'].min(0)))
        if(VD_values[i] == -1.0): print('Max IG Value: ' + str(subdf['IG'].max(0)))

    #put into csv/xlsx file code here:
    #also add maximum IG value for -1V = VDS

def create_pptx():
    ppt = Presentation()

    first_slide = ppt.slides.add_slide(ppt.slide_layouts[0])
    title = "Parsed Data Matplotlib Graphs"
    first_slide.shapes[0].text_frame.paragraphs[0].text = title
    
    for file in os.listdir(os.getcwd()):
        if file[-4:] == '.png':
            img = file
            slide = ppt.slide_layouts[1]
            slide = ppt.slides.add_slide(slide)
            slide.shapes.add_picture(img, left= Inches(2),top = Inches(1),height = Inches(5))
            os.remove(file)
 
    ppt.save('data_parser.pptx')

if __name__ == '__main__':
    main()