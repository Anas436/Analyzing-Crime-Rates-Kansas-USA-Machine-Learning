import pandas as pd
import os

path = 'src\data\cities crime data'
files_list = os.listdir(path)


merged_kansas_state_2007_2020 = pd.DataFrame()

for file in files_list:
    if '.csv' in str(file):

        city_file = pd.read_csv(path + '\\' + file)
        city_file['City name'] = file[:-4]
        merged_kansas_state_2007_2020 = pd.concat([merged_kansas_state_2007_2020, city_file])

print(files_list)
print(merged_kansas_state_2007_2020)

merged_kansas_state_2007_2020.to_csv(path + '\\' + 'merged_kansas_state_2007_2020.csv')