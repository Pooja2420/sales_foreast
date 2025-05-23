#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import pandas as pd
import matploylib.pyplot as pt
get_ipython().run_line_magic('matplotlib', 'inline')
import seborn as snns
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split
train=pd.read_csv("https://drive.google.com/file/d/1kCgCmcIZ48ft-78seUE_AXOCZMAHAuuj/view?usp=sharing")
test=pd.read_csv("https://drive.google.com/file/d/1fln1an0sqmQQTtwk0tH3mXWKFmF4nqfG/view?usp=sharing")
train.shape
test.shape
train.head()
data=pd.concat9[train,test])
data.drop("Loan_ID",axis=1,inplace=True)
data.isnull().sum()
for i in [data]:
	i["Gender"]=i["Gender"].fillna(data.Gender.dropna().mode()[0])
	i["Married"]=i["Married"].fillna(data.Maried.dropna().mode()[0])
	i["Dependents"]=i["Dependents"].fillna(data.Dependents.dropna().mode()[0])
	i["Self_Employed"]=i["Self_Employed"].fillna(data.Self_Employed.dropna().mode()[0])
	i["Credit_History"]=i["Credit_History"].fillna(data.Credit_History.dropna().mode()[0])
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor
data1=data.loc[:,['LoanAmount','Loan_Amount_Term']]
imp=IterativeImputer(RandomForestRegressor(),max_iter=10,random_state=0)
data1=pd.DataFrame(imp.fit_Transform(data1),columns=data1.columns)
for i in [data]:
	i["Gender"]=i["Gender"].map({"Male":0,"Female":1}).astype(int)
	i["Married"]=i["Married"].map({"No":0,"Yes":1}).astype(int)
	i["Education"]=i["Education"].map({"Not Graduate":0,"Graduate":1}).astype(int)
	i["Self_Employed"]=i["Self_Employed"].map({"No":0,"Yes":1}).astype(int)
	i["Credit_History"]=i["Credit_History"].astype(int)
for i in [data]:
	i["Property_Area"]=i["Property-Area"].map({"Urban":0,"Rural":1,"Semiurban":2}).astype(int)
	i["Dependents"]=i["Dependents"].map({"0":0,"1":1,"2":2,"3+":3})
new_train=data.iloc[:614]
new_test=data.iloc[614:]
new_rain["Loan_Status"]=new_train["Loan_Status].map({'N':0,"Y":1}).astype(int)
fig,az=plt.subplots(2,4,figsize=(16,10))
sns.countplot('Loan_Status',data=new_train,ax=ax[0][0])
sns.countptlot('Gender',data=new_train,ax=ax[0][1])
sns.countplot('Married',data=new_train,ax=ax[0][2])
sns.countplot('Education',data=new_train,ax=ax[0][3])
sns.countplot('Self_Employed',data=new_train,ax=ax[1][0])
sns.countplot('LProperty_Area',data=new_train,ax=ax[1][1])
sns.countplot('Credit_History',data=new_train,ax=ax[1][2])
sns.countplot('Dependents',data=new_train,ax=ax[1][3])
sns.boxplot(x='Loan_Status',y='ApplicantIncome',data=new_train)
sns.boxplot(x='Loan_Status',y='cOApplicantIncome',data=new_train)
sns.catplot(x='Gender',y='LoanAmount',data=new_train,kind='box')
sns.catplot(x='Gender',y='LoanAmount',data=new_train,kind='box',hue='Loan_Status',col='Married')
sns.catplot(x='Gender',y='CoapplicantIncome',data=new_train,kind='box',hue='Loan_Status',col='Property_Area')
plt.figure9figsize=(10,10))
correlation_matrix=new_train.corr()
sns.heatmap9correlation_matrix,annot=true)
plt.show
for i in [data]:
i["TotalIncom"]=i["ApplicantIncome"]+i["CoapplicantIncome"]
r=0.00833
data['EMI']=data.apply(lambda x: (x['oanAmount']*r*((1+r)**x['Loan_amount_Term']))/((1+r)**((x('Loam_Amount_Term'])-1)),axis=1)
dat['Dependents_EMI_meam']=daa.groupby(['Dependents'])['EMI''].transform('mean'0
data['LoanAmount_per_TotalIncome']=data['LoanAmount']]/data[''TotalIncome']
data['Loan_Amount_Term_per_TotalIncom']=data[['Loan_Amount_Term']/data[['TotalIncom']
data['EMI_per_Loan_Amount_Term']]=data['EMI']/data['Loan_Amount_Term']
data['EMI_per_LoanAmount']=data[['EMI']/data['LoanAmount']
data['Property_Area_LoanAmount_per_TotalIncome_mean']=data.groupby(['Property_Area'])'LoanAmount_per_Totalincome'].transform('mean')
data['Credit_History_Income_Sum']=data.groupby(['Credit_History'])['TotalIncome'].transform('sum')
data=['Dependents_LoanAmount_Sum']=data.groupby(['Dependents'])['LoanAmount'].transform('sum')
from sklear.preprocessin import KBinsDiscretizer
Loan_Amount_Term_discretizer=KBDiscretizer9n_bins=5,,encode='ordinal',strategy='quantile')
data['Loan_Amount_Term_bins']=Loan_Amount_Term_discretizer.fit_transformm(data['Loan_Amount_Term'].values.reshape(-1,1))astype(float)
TotalIncome_discretizer=KBinsDiscretizer(n_bins=5,encode='ordinal',strategy='quantile')
data['TotalIncome_Bins']=TotalIncome_discretizer.fit_transformm(data['TotalIncome'].values.reshape(-1,1))astype(float)
LoanAmount_per_TotalIncome_discretizer=KBinsDiscretizer(n_bins=5,encode='ordinal',strategy='quantile')
data['LoanAmount_per_Totalincome_Bins']=LoanAmount_per_TotalIncome_discretizer.fit_transformm(data['Loanamount_per_Totalincome'].values.reshape(-1,1))astype(float)
data=data.drop(['EMI'],axis=1)
data=data.drop(['Totalincome'],axis=1)
data=data.drop(['LoanAmount_per_Total_Income'],axis=1)
new_train.shape
x=new_train.drop("Loan_Status",axis=1)
y=new_train["Loan_Status"]
from sklearn.model_selection import train_test_split
x_train,x-test,y_train,y_test=train_test_split(x,y,test_size=0.3)
x_train_shape
x_test_shape
log_clf=LogisticRegression()
from sklearn.model_selection import cross_val_score
cross_val_score(log_clf,x_train,y_train,scoring=make_scorer(accuracy_score),cv=3)
predo=log_clf.fit(x_train,y_train).predict(x_test0
accuracy_score(predo,y_test)
from sklearn.model_selection import GridSearchCV
LRparam_grid={'C':[0.001,0.01,0.1,1,10,100,1000]
'penalty':['l1','l2'],
'max_iter':list(range(100,800,100)),
'solver'':['newton-cg',lbfgs','linlinear','sag','saga']
}
LR_search=GridSearchCV(LogisticReression(),LPparam_grid,refit=True,verbos=,cv=5)
LR_search.fit(x_train,y_train)
LR_search.best_params_
print('mea Accuracy:%.3f' %LR_search.best_scrore_)
print('Config:%s'' LR_search.best_params_)
Config:{'C':0.001,'max_iter':00,'penalty':'l1','solver':'liblinear'
l=LR_search.predict(x_test)
accuracy_score(l,y_test)
hj=LR_search.predict(new_test)
test_df=pd.DataFrame(data=hj,columns=["Loan_Statust'])
final_pred=pd.concat([[s['Loan_ID'],test_df],axis=1)
final_pred[['Loan_Status']=final_pred['Loan_Status'].mp({1:'Y',0:'N'})
final_pred.to_csv9"fianl38.csv",index=False)




--------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy.special import boxcox1p
import seaborn as sns

features=pd.read_csv("features.csv")
store=pd.read_csv("stores.csv")
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

train=train.groupby(['Store','Date'])['Weekly_Sales'].sum()
train=train.reset_index()
train.head(10)

data=pd.merge(train,features,on=['Store','Date'],how='inner')
data.head(10)

data=pd.merge(data,store,on=['Store'],how='inner')
data.head(10)

data=data.sort_values(by='Date')
data.head(10)
sns.countplot(x="Type", data=data)
sns.boxplot(x='Type',y='Weekly_Sales',data=data)
data["Weekly_Sales"].plot.hist()
sns.countplot(x="IsHoliday", data=data)
data.isnull().sum()
sns.heatmap(data.isnull(),yticklabels=False, cmap="viridis")
data=data.drop(['MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5'],axis=1)
data.head(10)
data.isnull().sum()
sns.heatmap(data.isnull(),yticklabels=False, cmap="viridis")
data['Holiday']=[int(i) for i in list(data.IsHoliday)]
data.head(10)
Type_dummy=pd.get_dummies(data['Type'],drop_first=True)
Type_dummy.head(10)
data=pd.concat([data,Type_dummy],axis=1)
data.head(10)
data=data.drop(['Type','IsHoliday'],axis=1)
data.drop(10)
#splitting data in input and output
X=data.drop(['Weekly_Sales','Store','Date'],axis=1)
y=data['Weekly_Sales']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
LR=LinearRegression(normalize=True)
LR.fit(X_train,y_train)
y_pred=LR.predict(X_test)
plt.plot(y_test,y_pred,'ro')
plt.plot(y_test,y_test,'b-')
plt.show()
Root_mean_square_error=np.sqrt(np.mean(np.square(y_test-y_pred)))
print(Root_mean_square_error)
from sklearn.metrics import r2_score
r2=r2_score(y_test,y_pred)
print(r2)
prediction=LR.predict(pd.DataFrame([(40.37,2.876,173.325456,7.934,103464,0,0,0)]))
print(prediction)

