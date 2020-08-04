import pandas as pd
import numpy as np
from matplotlib import pyplot
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
import pickle
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

data = pd.read_csv("compas-scores-two-years.csv", header=0)
data.head(n=20)

data.columns

df = data.drop(labels=['id', 'name', 'first', 'last', 'compas_screening_date', 'dob', 'days_b_screening_arrest', 
                         'c_jail_in', 'c_jail_out', 'c_case_number', 'c_offense_date', 'c_arrest_date', 'c_days_from_compas',
                         'r_case_number', 'r_charge_degree', 'r_days_from_arrest', 'r_offense_date', 'r_charge_desc', 
                         'r_jail_in', 'r_jail_out', 'vr_case_number', 'vr_charge_degree', 'vr_offense_date', 'decile_score.1',
                         'violent_recid', 'vr_charge_desc', 'in_custody', 'out_custody', 'priors_count.1', 'start', 'end', 
                         'v_screening_date', 'event', 'type_of_assessment', 'v_type_of_assessment', 'screening_date',
                         'score_text', 'v_score_text', 'v_decile_score', 'decile_score', 'is_recid', 'is_violent_recid'], axis=1)
df.columns = ['sex', 'age', 'age_category', 'race', 'juveline_felony_count', 'juveline_misdemeanor_count', 'juveline_other_count', 
              'prior_convictions', 'current_charge', 'charge_description', 'two_year_recid']
df.head()

filtered_df = data.apply(pd.to_numeric, errors='ignore')
filtered_df = filtered_df.applymap(str)

le_dict = {}
for col in filtered_df.columns:
    le_dict[col] = LabelEncoder().fit(filtered_df[col])
    filtered_df[col] = le_dict[col].transform(filtered_df[col])

enc = OneHotEncoder()
enc.fit(filtered_df)
refreshed_df = enc.transform(filtered_df).toarray()
refreshed_df  = pd.DataFrame(data=refreshed_df)

def encoder(var):
    ohc = enc
    ldict = le_dict
#value_counts = df['charge_description'].value_counts() 
#df = df[df['charge_description'].isin(value_counts[value_counts >= 70].index)].reset_index(drop=True) # drop rare charges
#for colname in df.select_dtypes(include='object').columns: # use get_dummies repeatedly one-hot encode categorical columns
#  one_hot = pd.get_dummies(df[colname])
#  df = df.drop(colname, axis=1)
#  df = df.join(one_hot)
#df.head()



y_column = 'two_year_recid'
X_all, y_all = refreshed_df.drop(y_column, axis=1), refreshed_df[y_column]
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=0.3)

#X_caucasian = X_test[X_test['Caucasian'] == 1]
#y_caucasian = y_test[X_test['Caucasian'] == 1]
#X_african_american = X_test[X_test['African-American'] == 1]
#y_african_american = y_test[X_test['African-American'] == 1]

model_svm = svm.SVC(kernel='linear')
model_svm.fit(X_train, y_train)

print("SVM Training accuracy:", model_svm.score(X_train, y_train))
print("SVM Testing accuracy:", model_svm.score(X_test, y_test))

pickle.dump(model_svm, open("justice2", 'wb'))

#pyplot.rcParams['figure.figsize'] = [15, 10]
#importance_svm = model_svm.coef_[0]

#features = X_all.columns
#pyplot.xticks(rotation="vertical")
#pyplot.gca().tick_params(axis='both', which='major', labelsize=20)

#svm_importance_plot = pyplot.bar(features, importance_svm)
#pyplot.xlabel("Feature", fontsize=20)
#pyplot.ylabel("Coefficient Value", fontsize=20)
#pyplot.show()

#y_pred_caucasian = model_svm.predict(X_caucasian)
#print("Caucasian acceptance rate:", np.count_nonzero(y_pred_caucasian) / len(y_pred_caucasian))
##y_pred_afam = model_svm.predict(X_african_american)
#print("African-American acceptance rate:", np.count_nonzero(y_pred_afam) / len(y_pred_afam))

