import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\HARSHADA PAWAR\\OneDrive\\Desktop\\CSV files\\Diwali Sales Data.csv",
                 encoding='unicode_escape')
a = df.isnull()
df.dropna(inplace=True)
df.drop(['Status','unnamed1'],axis=1,inplace=True)
df.info()

### Gender ####

df['Amount'] = df['Amount'].astype(int)
# df.info()

ax=sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data=sales_gen)
plt.show()

###Age####

ax = sns.countplot(x='Age Group', hue='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sns.countplot(x="Age Group",data =df)
plt.show()

####State#####

sale_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=sale_state,x='State',y='Orders')
plt.show()

sale_amount = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(7,5)})
sns.barplot(data=sale_amount,x='State',y='Amount')
plt.show()

##### Marital Status#####

ax=sns.countplot(x='Marital_Status',data=df)
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


sales_state = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_state,x='Marital_Status',y='Amount',hue='Gender')
plt.show()
df.info()

### Occupation ######

ax = sns.countplot(data=df,x='Occupation')
sns.set(rc={'figure.figsize':(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sales_state = df.groupby('Occupation',as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state,x='Occupation',y='Amount')
plt.show()

##### Product category ######

ax = sns.countplot(data=df,x='Product_Category')
sns.set(rc={'figure.figsize':(20,5)})
for bar in ax.containers:
    ax.bar_label(bar)
plt.show()

sales_state = df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state,x='Product_Category',y='Amount')
plt.show()

sales_state = df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state,x='Product_ID',y='Orders')
plt.show()

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Amount'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
plt.show()
