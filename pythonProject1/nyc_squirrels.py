import pandas as pd
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
list1 = data['Primary Fur Color'].to_list()
g = 0
c = 0
b = 0
for i in list1:
    if i =="Gray":
        g+=1
    elif i =="Black":
        b+=1
    elif i =="Cinnamon":
        c+=1
dict = {"Colors":["Gray","Black","Cinnamon"]
        ,"Numbers":[g,b,c]}
pf = pd.DataFrame(dict)
print(pf)

#OR

grey_data = len(data[data["Primary Fur Color"]=="Gray"])
black_data = len(data[data["Primary Fur Color"] =="Black"])
cin_data = len(data[data["Primary Fur Color"]=="Cinnamon"])
list2 = {"Colors":['grey','black','cinnamon'],
         "Numbers": [grey_data,black_data,cin_data]}
df = pd.DataFrame(list2)
print(df)
df.to_csv('Colors.csv')