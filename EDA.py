import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sn 
import warnings
warnings.filterwarnings('ignore')
# Reading the data set
df = pd.read_csv(r"C:\Users\HP\Desktop\DS Projects\Data_science\terrorism.csv", encoding='ISO-8859-1')
df.head(18) #displaying head values
df.tail()  # displaying tail values
#Renaming the columns
df.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','provstate':'state','region_txt':'Region','attacktype1_txt':'AttackType',
'target1':'Target','nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive'} ,inplace=True)
# renamed columns
df=df[['Year','Month','Day','Country','state','Region','AttackType','Target','Killed','Wounded','Summary','Group','Target_type','Weapon_type','Motive']]
df.isnull().sum()
df.info()
print("most attacked")
print("contry:",df['Country'].value_counts().idxmax())
print("Region:",df['Region'].value_counts().idxmax())
print("Year:",df['Year'].value_counts().idxmax())
print("Type:",df['AttackType'].value_counts().idxmax())
#bar plot
plt.subplots(figsize=(15,6))
sn.barplot(x=df['Country'].value_counts()[:20].index,y=df['Country'].value_counts()[:20].values)
sn.color_palette("husl",9)
plt.title('Top countries affected',fontsize=16)
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

x_year= df['Year'].unique()
y_count_year = df['Year'].value_counts(dropna=True).sort_index()
plt.figure(figsize=(15,8))
sn.barplot(x=x_year,y=y_count_year,palette='PuBu')
plt.xticks(rotation=90)
plt.xlabel('Attack Year')
plt.ylabel('Number of Attacks per year')
plt.title('Attack every year',fontsize=16)
plt.show()
# Region wise Graph plotting
pd.crosstab(df['Year'],df['Region']).plot(kind='area',figsize=(20,8))
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.show()


plt.subplots(figsize=(15,8))
sorted_df = df.sort_values(by='Target_type')
sn.countplot(data=sorted_df, x='Target_type', palette='GnBu_r')
plt.xticks(rotation=90)
plt.title("Type of Targets")
plt.show()
#Attack type V/S Region
pd.crosstab(df.Region,df.AttackType).plot.barh(figsize=(15,6))
fig = plt.gcf()
fig.set_size_inches(12,8)
plt.show()
# country wise attack and kills
count_at = df['Country'].value_counts()[:15].to_frame()
count_at.columns=['Attacks']
coun_kill = df.groupby('Country')['Killed'].sum().to_frame()
count_at.merge(coun_kill,left_index=True,right_index=True,how='left').plot.bar(figsize=(15,6))
fig = plt.gcf()
fig.set_size_inches(12,8)
plt.show()
# groups of terrorism
sn.barplot(x=df['Group'].value_counts()[1:15].values,y=df['Group'].value_counts()[1:15].index)
plt.xticks(rotation=90)
plt.title('Terrorism groups with most attacks')
fig = plt.gcf()
fig.set_size_inches(12,8)
plt.show()

top_grp= df[df['Group'].isin(df['Group'].value_counts()[1:11].index)]
pd.crosstab(top_grp.Year,top_grp.Group).plot(color = sn.color_palette('cividis_r',15))
fig=plt.gcf()
fig.set_size_inches(12,8)
plt.show()
# Activities in india
india=df[df['Country']=='India']
#terrorist group in india
sn.barplot(x=india['Group'].value_counts()[1:11].values,y=india['Group'].value_counts()[1:11].index)
plt.xticks(rotation=90)
plt.title('Terrorist groups in india')
fig = plt.gcf()
fig.set_size_inches(12,8)
plt.show()
# types of attacks in india
sn.barplot(x=india['AttackType'].value_counts()[:11].values,y=india['AttackType'].value_counts()[:11].index)
plt.xticks(rotation=90)
plt.title("Most Common Attacks in india")
fig = plt.gcf()
fig.set_size_inches(12,8)
plt.show()