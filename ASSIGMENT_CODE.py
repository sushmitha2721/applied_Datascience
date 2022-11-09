import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
Housing_df = pd. read_csv('housing_in_london_monthly_variables.csv')
Housing_df['date'] = Housing_df['date'].astype('datetime64[ns]')
Housing_df.set_index('date',inplace=True)

# 1st visualization: line plot

def House_Plot(areas,data):
    ''' The method is used to plot the average price of each area in london from 1996 to 2020,
        The function takes first argument as list of areas and second argument as data in form of dataframe'''
    for i in areas:
        x = data[data['area'] == i ]
        plt.plot(x['average_price'],label=i)
    plt.legend()
    plt.ylabel("Average price of house")
    plt.xlabel("years")
    plt.title('Change of average house price in london areas from 1996 to 2020')
    plt.show()
House_Plot(['hammersmith and fulham','hounslow','barnet','ealing'],Housing_df)


# 2nd visualization : Bar plot

barnet  = Housing_df[Housing_df['area'] == 'barnet']
barnet = barnet[barnet.index.year >= 2001]

hounslow  = Housing_df[Housing_df['area'] == 'hounslow']
hounslow = hounslow[hounslow.index.year >= 2001]

hammersmith = Housing_df[Housing_df['area'] == 'hammersmith']
hammersmith = hammersmith[hammersmith.index.year >= 2001]

ealing = Housing_df[Housing_df['area'] == 'ealing']
ealing = ealing[ealing.index.year >= 2001]


a=barnet['no_of_crimes'].groupby(barnet.index.year).mean()
b=hounslow['no_of_crimes'].groupby(hounslow.index.year).mean()
d=ealing['no_of_crimes'].groupby(ealing.index.year).mean()

n=20
r = np.arange(n)
width = 0.25
plt.figure(figsize=(19,8))
plt.bar(r, a, color = 'blue',
        width = width,
        label='barnet')
plt.bar(r + width, b, color = 'yellow',
        width = width,
        label='hounslow')

plt.bar(r + (width*2), d, color = 'red',
        width = width,
        label='ealing')
plt.xlabel("Year")
plt.ylabel("Average Number of Crimes")
plt.title("Average crime rate in each area from 2001 to 2020")
plt.xticks(r + width/2,hounslow.index.year.unique(),rotation=90)
plt.legend()
plt.show()


# 3rd visualization: Pie chart

num_of_house = Housing_df[['area','houses_sold']]

num_of_house = num_of_house.dropna()
areas= ['barking and dagenham', 'barnet', 'bexley',
       'brent', 'bromley', 'camden', 'croydon', 'ealing', 'enfield',
       'tower hamlets', 'greenwich', 'hackney','hammersmith and fulham', 'haringey', 'harrow', 'havering',
       'hillingdon', 'hounslow', 'islington', 'kensington and chelsea',
       'kingston upon thames', 'lambeth', 'lewisham', 'merton', 'newham',
       'redbridge', 'richmond upon thames', 'southwark', 'sutton',
       'waltham forest', 'wandsworth', 'westminster']

count_houses=[]
for a in areas :
    x = num_of_house[num_of_house['area'] == a]
    count_houses.append([x['houses_sold'].sum(),a])

count_houses=sorted(count_houses,reverse=True)
sums=0
num_area=10
for i in range(len(count_houses)):
    if i>num_area:
        sums=sums+count_houses[i][0]
    i=i+1
    if i == len(count_houses):
        count_houses=count_houses[:num_area]
        break

count_houses.append([sums,'others'])
count = [i[0] for i in count_houses]
area = [i[1] for i in count_houses]
plt.figure(figsize=(8,8))
plt.pie(count,labels=area,autopct='%1.1f%%',startangle=70)
plt.axis()
plt.title('Top '+str(num_area)+' areas with most houses sold from 2001 to 2020')
plt.legend()
plt.show()
