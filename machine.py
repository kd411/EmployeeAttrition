import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('original_dataset.csv')
df = df.drop(['DailyRate', 'EmployeeCount', 'YearsAtCompany', 'TotalWorkingYears', 'JobLevel', 'HourlyRate', 'MonthlyRate', 'Over18', 'StandardHours', 'EnvironmentSatisfaction', 'JobInvolvement', 'PerformanceRating', 'TrainingTimesLastYear', 'RelationshipSatisfaction', 'StockOptionLevel', 'WorkLifeBalance', 'YearsWithCurrManager'], axis=1)
df = df[['Attrition', 'Age', 'BusinessTravel', 'Department', 'DistanceFromHome', 'Education', 'EducationField', 'Gender', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked', 'OverTime', 'PercentSalaryHike', 'YearsInCurrentRole', 'YearsSinceLastPromotion']]
df.to_csv('dataset-complete.csv')

Var_Corr = df.corr()
X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values
t = df.iloc[3, 1:].values

labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
labelencoder_X_5 = LabelEncoder()
X[:, 5] = labelencoder_X_5.fit_transform(X[:, 5])
labelencoder_X_6 = LabelEncoder()
X[:, 6] = labelencoder_X_6.fit_transform(X[:, 6])
labelencoder_X_7 = LabelEncoder()
X[:, 7] = labelencoder_X_7.fit_transform(X[:, 7])
labelencoder_X_9 = LabelEncoder()
X[:, 9] = labelencoder_X_9.fit_transform(X[:, 9])
labelencoder_X_12 = LabelEncoder()
X[:, 12] = labelencoder_X_12.fit_transform(X[:, 12])

X = X.astype(float)
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

onehotencoder1 = OneHotEncoder(categorical_features = [1])
X = onehotencoder1.fit_transform(X).toarray()
X = X[:, 1:]
onehotencoder2 = OneHotEncoder(categorical_features = [3])
X = onehotencoder2.fit_transform(X).toarray()
X = X[:, 1:]
onehotencoder5 = OneHotEncoder(categorical_features = [5])
X = onehotencoder5.fit_transform(X).toarray()
X = X[:, 1:]
onehotencoder7 = OneHotEncoder(categorical_features = [11])
X = onehotencoder7.fit_transform(X).toarray()
X = X[:, 1:]
onehotencoder9 = OneHotEncoder(categorical_features = [19])
X = onehotencoder9.fit_transform(X).toarray()
X = X[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
p = clf.predict(X_test)
print(accuracy_score(y_test,p))
