import pandas as pd
import os
import re

path = 'src\data\cities crime data'
files_list = os.listdir(path)
files_list.remove('merged_kansas_state_2007_2020.csv')


merged_kansas_state_2007_2020 = pd.DataFrame()


for file in files_list:
    if '.csv' in str(file):
        city_file = pd.read_csv(path + '\\' + file)
        city_file['City name'] = file[:-4]
        merged_kansas_state_2007_2020 = pd.concat([merged_kansas_state_2007_2020, city_file])

merged_kansas_state_2007_2020 = merged_kansas_state_2007_2020.fillna(0)
print("NaN columns: ", merged_kansas_state_2007_2020.isna().sum())
print(files_list)
print(merged_kansas_state_2007_2020)

for i in range(len(merged_kansas_state_2007_2020.columns)):
    column = i+1
    if column < len(merged_kansas_state_2007_2020.columns)-1:
        for row in range(len(merged_kansas_state_2007_2020.iloc[:, column])):
            #print('column number is: ', column)
            #print('number of row: ', row)
            merged_kansas_state_2007_2020.iloc[row, column] = int(float(re.findall("\w*[\s\w.\s]*", str(merged_kansas_state_2007_2020.iloc[row, column]))[0]))

    else:
        break


for row in range(len(merged_kansas_state_2007_2020.iloc[:,0])):
    if row < len(merged_kansas_state_2007_2020.iloc[:,0]):
        merged_kansas_state_2007_2020.iloc[row, 0] = str(merged_kansas_state_2007_2020.iloc[row, 0])[0:-13]
    else:
        break

merged_kansas_state_2007_2020[merged_kansas_state_2007_2020['Type'] == 'City-Data.co'] = merged_kansas_state_2007_2020[merged_kansas_state_2007_2020['Type'] == 'City-Data.co'].replace('City-Data.co', 'Total')

print(merged_kansas_state_2007_2020)

merged_kansas_state_2007_2020.to_csv(path + '\\' + 'merged_kansas_state_2007_2020.csv')