import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 131543: invalid continuation byte

df=pd.read_csv("/content/drive/MyDrive/Rinex/Rinex AI Batch July 2023/laptop_price.csv",encoding='latin')
df

df.drop(columns=['laptop_ID'],inplace=True)

df.sample()

df.info()

df.isnull().sum()

df.duplicated().sum()

df[df.duplicated()]

df.drop_duplicates(inplace=True)

df.shape

df['Price']=(df['Price_euros']*90.96).astype('int')
df.drop(columns=['Price_euros'],inplace=True)

df.sample()

# EDA
# - Univariate Analysis
# - Multi-Variate Analysis

# Company Column
df['Company'].value_counts()

9+7+7+6+4+4+3+3+3+3+2

plt.rcParams['figure.figsize']=[6,3.5]  # The default setting for entire notebook
# plt.figure(figsize=(10,8)) # individual graphs

df['Company'].value_counts().plot(kind='bar')

sns.barplot(x=df['Company'],y=df['Price'])
plt.xticks(rotation=90)
plt.show()

df=df[df.groupby('Company').Company.transform('count')>10].copy()

1275-1224

df.shape

df=df.reset_index(drop=True)

df['Company'].value_counts().plot(kind='bar')

sns.barplot(x=df['Company'],y=df['Price'],errorbar=None)
plt.xticks(rotation=90)
plt.show()

df['Product'].value_counts()

df.drop(columns=['Product'],inplace=True)

df.sample()

df['TypeName'].value_counts()

df['TypeName'].value_counts().plot(kind='bar')

sns.barplot(x=df['TypeName'],y=df['Price'],errorbar=None)
plt.xticks(rotation=90)
plt.show()

df['Inches'].value_counts()

# 15.6 : 15 inch
# 14.0 : 14 inch
# 17.3 : 17 inch
# 13.3 : 13 inch

df['Inches'].value_counts().plot(kind='bar')

sns.displot(x=df['Inches'],kde=True)

sns.barplot(x=df['Inches'],y=df['Price'],errorbar=None)
plt.xticks(rotation=90)
plt.show()

df['ScreenResolution'].value_counts()

# X_res  : horizontal pixels
# Y_res  : vertical pixels
# IPS    : IPS panel or not
# Touchscreen : Touchscreen or not

a="IPS Panel Full HD / Touchscreen 1920x1080"

a.split()

a.split()[-1]

a.split()[-1].split('x')

a.split()[-1].split('x')[0]

a.split()[-1].split('x')[1]

(lambda x:x.split()[-1].split('x')[0])("IPS Panel Full HD / Touchscreen 1920x1080")

(lambda x:x.split()[-1].split('x')[1])("IPS Panel Full HD / Touchscreen 1920x1080")

(lambda x:1 if "IPS" in x else 0)(" Panel Full HD /  1920x1080")

df['X_res']=df['ScreenResolution'].apply(lambda x:x.split()[-1].split('x')[0]).astype('int')
df['Y_res']=df['ScreenResolution'].apply(lambda x:x.split()[-1].split('x')[1]).astype('int')
df['Touchscreen']=df['ScreenResolution'].apply(lambda x:1 if "Touchscreen" in x else 0).astype('int')
df['IPS']=df['ScreenResolution'].apply(lambda x:1 if "IPS" in x else 0).astype('int')

df.sample(6)

df.drop(columns=['ScreenResolution'],inplace=True)

df.sample()

df['Ram'].value_counts()

df['Ram']=df['Ram'].apply(lambda x:x.replace("GB","")).astype('int')

df['Ram'].value_counts()

df['Ram'].value_counts().plot(kind='bar')

sns.barplot(x=df['Ram'],y=df['Price'],errorbar=None)
plt.xticks(rotation=90)
plt.show()

df['Cpu'].value_counts()

a="Intel Core i5 8250U 1.6GHz"

(lambda a:" ".join(a.split()[0:3]))("Intel Core i5 8250U 1.6GHz")

df['Cpu']=df['Cpu'].apply(lambda a:" ".join(a.split()[0:3]))

df['Cpu'].value_counts()

def fetch_processor_name(text):
  if text=='Intel Core i7' or text=='Intel Core i5' or text=='Intel Core i3' or text=='Intel Core M':
    return text
  elif text.split()[0]=='Intel':
    return " ".join(text.split()[0:2])
  else:
    return "AMD Processor"

df['Cpu']=df['Cpu'].apply(fetch_processor_name)

df['Cpu'].value_counts()

df['Cpu'].value_counts().plot(kind='bar')

sns.barplot(x=df['Cpu'],y=df['Price'],errorbar=None)
plt.xticks(rotation=90)
plt.show()

df['Memory'].value_counts()

# -- Due to complexity in handling various storage options, we will skip the memory column

df.drop(columns=['Memory'],inplace=True)

df.sample()

df['Gpu'].value_counts()

df['Gpu']=df['Gpu'].apply(lambda x:x.split()[0])

df['Gpu'].value_counts()

df['Gpu'].value_counts().plot(kind='bar')

sns.barplot(x=df['Gpu'],y=df['Price'],errorbar=None)
plt.xticks(rotation=90)
plt.show()

df['OpSys'].value_counts()

def fetch_os(text):
  if text=="Windows 10" or text=="Windows 10 S":
    return "Windows 10"
  elif text=="Windows 7":
    return text
  elif text=="Mac OS X" or text=="macOS":
    return "Mac OS"
  else:
    return "Linux/No OS/Others"

df['OpSys']=df['OpSys'].apply(fetch_os)

df['OpSys'].value_counts()

df['OpSys'].value_counts().plot(kind='bar')

sns.barplot(x=df['OpSys'],y=df['Price'],errorbar=None)
plt.xticks(rotation=90)
plt.show()

df['Weight']

df['Weight']=df['Weight'].apply(lambda x:x.replace("kg","")).astype('float')

sns.displot(x=df['Weight'],kde=True)

sns.scatterplot(x=df['Weight'],y=df['Price'])

df.sample()

df['Touchscreen'].value_counts()

df['Touchscreen'].value_counts().plot(kind='bar')

sns.barplot(x=df['Touchscreen'],y=df['Price'],errorbar=None)
plt.xticks(rotation=90)
plt.show()

df['IPS'].value_counts().plot(kind='bar')

sns.barplot(x=df['IPS'],y=df['Price'],errorbar=None)
plt.xticks(rotation=90)
plt.show()

df.corr(numeric_only=True)

df.corr(numeric_only=True)['Price']

# Pixel density(ppi) is a much better measure than X_res and Y_res

df['ppi']=round(((df['X_res']**2)+(df['Y_res']**2))**0.5/df['Inches']).astype('int')

df['ppi']

df.corr(numeric_only=True)['Price']

df.drop(columns=['Inches','X_res','Y_res'],inplace=True)

df['ppi'].value_counts()

sns.displot(x=df['ppi'],kde=True)

sns.scatterplot(x=df['ppi'],y=df['Price'])

df.sample()

df.shape

sns.displot(x=df['Price'],kde=True)
plt.show()

sns.displot(x=np.log(df['Price']),kde=True)
plt.show()

X=df.drop(columns=['Price'])
y=np.log(df['Price'])

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.15,random_state=42)

X.shape

X_train.shape

X_test.shape

1224*0.85

X.head()

X_train.head()

y_train.head()

X_test.head()

y_test.head()

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor

X_train.sample()

# LinearRegression
step1=ColumnTransformer(transformers=[
    ('col_tnf',OneHotEncoder(sparse_output=False,drop='first'),[0,1,2,4,5])
    ],remainder='passthrough')
step2=LinearRegression()
pipe=Pipeline([('step1',step1),('step2',step2)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

print("R2 score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

# Lasso
step1=ColumnTransformer(transformers=[
    ('col_tnf',OneHotEncoder(sparse_output=False,drop='first'),[0,1,2,4,5])
    ],remainder='passthrough')
step2=Lasso(alpha=0.001)
pipe=Pipeline([('step1',step1),('step2',step2)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

print("R2 score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

# Ridge
step1=ColumnTransformer(transformers=[
    ('col_tnf',OneHotEncoder(sparse_output=False,drop='first'),[0,1,2,4,5])
    ],remainder='passthrough')
step2=Ridge(alpha=8)
pipe=Pipeline([('step1',step1),('step2',step2)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

print("R2 score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

# KNeighborsRegressor
step1=ColumnTransformer(transformers=[
    ('col_tnf',OneHotEncoder(sparse_output=False,drop='first'),[0,1,2,4,5])
    ],remainder='passthrough')
step2=KNeighborsRegressor()
pipe=Pipeline([('step1',step1),('step2',step2)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

print("R2 score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

# DecisionTreeRegressor
step1=ColumnTransformer(transformers=[
    ('col_tnf',OneHotEncoder(sparse_output=False,drop='first'),[0,1,2,4,5])
    ],remainder='passthrough')
step2=DecisionTreeRegressor(max_depth=8)
pipe=Pipeline([('step1',step1),('step2',step2)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

print("R2 score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

# Support Vector Regressor
step1=ColumnTransformer(transformers=[
    ('col_tnf',OneHotEncoder(sparse_output=False,drop='first'),[0,1,2,4,5])
    ],remainder='passthrough')
step2=SVR(C=10000)
pipe=Pipeline([('step1',step1),('step2',step2)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

print("R2 score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

# AdaBoostRegressor
step1=ColumnTransformer(transformers=[
    ('col_tnf',OneHotEncoder(sparse_output=False,drop='first'),[0,1,2,4,5])
    ],remainder='passthrough')
step2=AdaBoostRegressor()
pipe=Pipeline([('step1',step1),('step2',step2)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

print("R2 score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

# RandomForestRegressor
step1=ColumnTransformer(transformers=[
    ('col_tnf',OneHotEncoder(sparse_output=False,drop='first'),[0,1,2,4,5])
    ],remainder='passthrough')
step2=RandomForestRegressor()
pipe=Pipeline([('step1',step1),('step2',step2)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

print("R2 score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

# eXtreme Gradient Boosting Regressor
step1=ColumnTransformer(transformers=[
    ('col_tnf',OneHotEncoder(sparse_output=False,drop='first'),[0,1,2,4,5])
    ],remainder='passthrough')
step2=XGBRegressor(n_estimators=50,max_depth=4)
pipe=Pipeline([('step1',step1),('step2',step2)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

print("R2 score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

# GradientBoostingRegressor
step1=ColumnTransformer(transformers=[
    ('col_tnf',OneHotEncoder(sparse_output=False,drop='first'),[0,1,2,4,5])
    ],remainder='passthrough')
step2=GradientBoostingRegressor(n_estimators=300)
pipe=Pipeline([('step1',step1),('step2',step2)])
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

print("R2 score:",r2_score(y_test,y_pred))
print("MAE:",mean_absolute_error(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

import pickle
pickle.dump(df,open('df.pkl','wb'))
pickle.dump(pipe,open('pipe.pkl','wb'))

!pip install streamlit --quiet

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pickle
# import numpy as np
# 
# df=pickle.load(open('df.pkl','rb'))
# pipe=pickle.load(open('pipe.pkl','rb'))
# 
# st.title("Laptop Price Predictor")
# company=st.selectbox("Brand",df['Company'].unique(),index=4)
# type=st.selectbox("Type",df['TypeName'].unique(),index=1)
# cpu=st.selectbox("Processor",df['Cpu'].unique(),index=0)
# ram=st.selectbox("RAM(in GB)",[2,4,6,8,12,16,24,32,64,128],index=3)
# gpu=st.selectbox("GPU",df['Gpu'].unique(),index=0)

X_train.sample()

df['Gpu'].unique()

!streamlit run app.py & npx localtunnel --port 8501

