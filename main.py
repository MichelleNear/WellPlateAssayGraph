# Project:  Well Plate Assay
# Function: Process and display data
# Author:   Michelle Near

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Function: get minutes (float) from hh:mm:ss

def hms_to_min(time):
    time_str = str(time)
    h, m, s = time_str.split(':')
    minutes = (float(h) * 3600.0 + float(m) * 60.0 + float(s)) / 60.0
    return minutes


# Read dataset from Excel file

df = pd.read_excel(r'C:\Users\Michelle\Desktop\Anschutz\Data\WellPlate\Data3.xlsx')
group_size = 61

# Normalize 'Abs 404' values in each group and convert 'Time' to minutes (float)

for row in range(len(df)):
    if (row % group_size) == 0:  # First row of group
        first_abs = df.loc[row, 'Abs 404']
    df.loc[row, 'Abs 404'] = df.loc[row, 'Abs 404'] - first_abs
    df.loc[row, 'Time'] = hms_to_min(df.loc[row, 'Time'])

#Remove Condition 1 TM:TF
#df['Time'] = df['Time'].astype(float)
#df=df[df['Condition']!='1 TM:TF']

plt.figure(figsize=(15, 10))
plt.xlabel('Time (minutes)')
ax = sns.lineplot(x='Time',
    y='Abs 404',
    hue='Condition',
    legend='full',
    data=df)
#   palette=sns.color_palette("Set2"))
plt.xlim([0,20])
plt.show()

