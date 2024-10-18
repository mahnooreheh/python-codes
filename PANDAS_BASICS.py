import pandas as pd

#Series is one dimensional eg, Columns
# whereas, DataFrame is 2 dimensional

data = pd.read_csv('weather_data (1).csv')
print(type(data['temp']))#A Series
print(type(data)) #A DataFrame

print(data.info(verbose=True)) #prints info about everything inside the dataframe
datad = data.to_dict()
print(datad)

list1 = data['temp'].to_list()
sum1 = 0
for i in list1:
    sum1 = sum1 + int(i)
avg = sum1/len(list1)
print(f"The Avg temperature was: {round(avg,2)} ")
#or
print(f"The avg temp is: {round(data['temp'].mean(),2)}")

maximumval = data['temp'].max()
print(f"The maximum temperature was: {maximumval}")

#2nd way of accessing column
cond = data.condition
tempe = data.temp
print(tempe, cond)

#accessing row data
row1 = data[data.day == 'Monday']
print(row1)

maxtemprow = data[data.temp == maximumval]
print(maxtemprow)

monday = data[data.day == 'Monday']
monday_temp_f = (9/5)*monday.temp+32
print(monday_temp_f)

#creating data frame from scratch

dict = {"Students":["Mahnoor","Hiba","Wania"],
        "Grades":[100,90, 101]}
df = pd.DataFrame(dict)
print(df)
df.to_csv('new_file.csv')


