import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('src\data\cities crime data\merged_kansas_state_2007_2020.csv').iloc[:, 1:]

print(df)

crimes = df['Type'].unique()

print(crimes)
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'gray', 'black', 'purple', 'pink', 'brown']

for crime in crimes:
    fig = plt.figure()
    color_index = 0
    crime_to_plot = pd.DataFrame()
    for row in df[df['Type'] == crime].index:
        print(row)
        crime_to_plot = pd.concat([crime_to_plot,
                                   pd.DataFrame({df.iloc[row, -1]: df.iloc[row, 1:-1]})], axis=1)
    
    print(crime, crime_to_plot)
    sns.lineplot(crime_to_plot, linestyle='solid').set_title(crime)

    plt.show()