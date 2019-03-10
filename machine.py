import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import flash
import numpy as np


def check(X, clf):
    X = np.array(X)
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
    p = clf.predict(X)
    t = ()
    for x in p:
        if x == 0:
            a = 'No'
        else:
            a = 'Yes'
        t = t+(a,)
    return t


def analyze(df, clf):
    feature_importances = pd.DataFrame(clf.feature_importances_, index=['Age', 'BusinessTravel', 'Department', 'DistanceFromHome', 'Education', 'EducationField', 'Gender', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked', 'OverTime', 'PercentSalaryHike', 'YearsInCurrentRole', 'YearsSinceLastPromotion'],columns=['importance']).sort_values('importance',ascending=False)
    feature_importances['x1'] = feature_importances.index
    ax = feature_importances.plot.bar(x='x1', y='importance', rot=90)
    plt.savefig('templates/graphs/raw/feature_importances.png', frameon=True)

    intervals = [x for x in range(0, 22000, 2000)]
    categories = ['<'+str(x) for x in range(2000, 22000, 2000)]
    df1 = df
    df1['Income_Categories'] = pd.cut(df.MonthlyIncome, intervals, labels=categories)
    ax = sns.countplot(x="Income_Categories", hue="Attrition", palette="Set1", data=df1)
    ax.set(title="Monthly Income vs Attrition", xlabel="Income group", ylabel="Total")
    plt.xticks(rotation=-30)
    plt.savefig('templates/graphs/raw/MIvsAttr.png')

    intervals = [x for x in range(18,63,3)]
    categories = ['<'+str(x) for x in range(21,63,3)]
    df1 = df
    df1['Age_Categories'] = pd.cut(df.Age, intervals, labels=categories)
    ax = sns.countplot(x="Age_Categories", hue="Attrition", palette="Set1", data=df1)
    ax.set(title="Age vs Attrition", xlabel="Age group", ylabel="Total")
    plt.xticks(rotation=-30)
    plt.savefig('templates/graphs/raw/AgevsAttr.png')

    intervals = [x for x in range(0,32,2)]
    categories = ['<'+str(x) for x in range(2,32,2)]
    df1 = df
    df1['Distance_from_home'] = pd.cut(df.DistanceFromHome, intervals, labels=categories)
    ax = sns.countplot(x="Distance_from_home", hue="Attrition", palette="Set1", data=df1)
    ax.set(title="Distance from home vs Attrition", xlabel="Distance", ylabel="Total")
    plt.xticks(rotation=-30)
    plt.savefig('templates/graphs/raw/DistanceFromHomevsAttr.png')

    ax = sns.countplot(x="PercentSalaryHike", hue="Attrition", palette="Set1", data=df1)
    ax.set(title="Salary Hike Percentage vs Attrition", xlabel="Salary Hike Percentage", ylabel="Total")
    plt.savefig('templates/graphs/raw/PercentSalaryHikevsAttr.png')

    ax = sns.countplot(x="NumCompaniesWorked", hue="Attrition", palette="Set1", data=df1)
    ax.set(title="Number Of Previously Worked Companies vs Attrition", xlabel="Number Of Previously Worked Companies", ylabel="Total")
    plt.savefig('templates/graphs/raw/NPWCvsAttr.png')

    intervals = [x for x in range(0,22,2)]
    categories = ['<'+str(x) for x in range(2,22,2)]
    df1 = df
    df1['Current_Role'] = pd.cut(df.YearsInCurrentRole, intervals, labels=categories)
    ax = sns.countplot(x="Current_Role", hue="Attrition", palette="Set1", data=df1)
    ax.set(title="Number Of Years in Current Role vs Attrition", xlabel="Number Of Years in Current Role", ylabel="Total")
    plt.xticks(rotation=-30)
    plt.savefig('templates/graphs/raw/YICRvsAttr.png')

    ax = sns.countplot(x="OverTime", hue="Attrition", palette="Set1", data=df1)
    ax.set(title="Over Time vs Attrition", xlabel="Over Time", ylabel="Total")
    plt.savefig('templates/graphs/raw/OverTimevsAttr.png')

    ax = sns.countplot(x="JobRole", hue="Attrition", palette="Set1", data=df1)
    ax.set(title="Job Role vs Attrition", xlabel="Job Role", ylabel="Total")
    plt.xticks(rotation=70)
    plt.savefig('templates/graphs/raw/JobRolevsAttr.png')

    intervals = [x for x in range(0,18,2)]
    categories = ['<'+str(x) for x in range(2,18,2)]
    df1 = df
    df1['Promotion'] = pd.cut(df.YearsSinceLastPromotion, intervals, labels=categories)
    ax = sns.countplot(x="Promotion", hue="Attrition", palette="Set1", data=df1)
    ax.set(title="Number of Years since Promotion vs Attrition", xlabel="Number of Years since Promotion", ylabel="Total")
    plt.xticks(rotation=-30)
    plt.savefig('templates/graphs/raw/YSCPvsAttr.png')

    ax = sns.countplot(x="MaritalStatus", hue="Attrition", palette="Set1", data=df1)
    ax.set(title="Marital Status vs Attrition", xlabel="Marital Status", ylabel="Total")
    plt.savefig('templates/graphs/raw/MSvsAttr.png')


def run(data):
    df = pd.read_csv('original_dataset.csv')
    df = df.drop(['DailyRate', 'EmployeeCount', 'YearsAtCompany', 'TotalWorkingYears', 'JobLevel', 'HourlyRate', 'MonthlyRate', 'Over18', 'StandardHours', 'EnvironmentSatisfaction', 'JobInvolvement', 'PerformanceRating', 'TrainingTimesLastYear', 'RelationshipSatisfaction', 'StockOptionLevel', 'WorkLifeBalance', 'YearsWithCurrManager'], axis=1)
    df = df[['Attrition', 'Age', 'BusinessTravel', 'Department', 'DistanceFromHome', 'Education', 'EducationField', 'Gender', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked', 'OverTime', 'PercentSalaryHike', 'YearsInCurrentRole', 'YearsSinceLastPromotion']]
    X = df.iloc[:, 1:].values
    y = df.iloc[:, 0].values

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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40,random_state=0)

    clf = RandomForestClassifier(n_estimators=200)
    clf.fit(X_train,y_train)
    p = clf.predict(X_test)
    acc = accuracy_score(y_test,p)*100
    flash(acc)
    X = [list(elem) for elem in data]
    [r.pop(0) for r in X]
    att = check(X, clf)
    i = 0
    for row in att:
        X[i].insert(0, row)
        i = i+1
    df1 = pd.DataFrame(X)
    df1.columns=['Attrition', 'Age', 'BusinessTravel', 'Department', 'DistanceFromHome', 'Education', 'EducationField', 'Gender', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked', 'OverTime', 'PercentSalaryHike', 'YearsInCurrentRole', 'YearsSinceLastPromotion']
    analyze(df, clf)
    df1.to_csv('dataset1.csv')
    return att
