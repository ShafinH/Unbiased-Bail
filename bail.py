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
import sys
import model

print("hellos")

filename = sys.argv[0]

data = pd.read_csv("miguel.csv", header=0)

data.columns

df = data.drop(labels=['id', 'name', 'first', 'last', 'compas_screening_date', 'dob', 'days_b_screening_arrest', 
                         'c_jail_in', 'c_jail_out', 'c_case_number', 'c_offense_date', 'c_arrest_date', 'c_days_from_compas',
                         'r_case_number', 'r_charge_degree', 'r_days_from_arrest', 'r_offense_date', 'r_charge_desc', 
                         'r_jail_in', 'r_jail_out', 'vr_case_number', 'vr_charge_degree', 'vr_offense_date', 'decile_score.1',
                         'violent_recid', 'vr_charge_desc', 'in_custody', 'out_custody', 'priors_count.1', 'start', 'end', 
                         'v_screening_date', 'event', 'type_of_assessment', 'v_type_of_assessment', 'screening_date',
                         'score_text', 'v_score_text', 'v_decile_score', 'decile_score', 'is_recid', 'is_violent_recid'], axis=1)
df.columns = ['sex', 'age', 'age_category', 'race', 'juveline_felony_count', 'juveline_misdemeanor_count', 'juveline_other_count', 
              'prior_convictions', 'current_charge', 'charge_description', 'recidivated_last_two_years']
df.head()

for col in df.columns:
    df[col] = model.ldict[col].transform(new_df[col])

new_refreshed_df = model.ohc.transform(df).toarray()

y_column = 'recidivated_last_two_years'
X_all, y_all = df.drop(y_column, axis=1), df[y_column]
#X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=0.3)

#X_caucasian = X_test[X_test['Caucasian'] == 1]
#y_caucasian = y_test[X_test['Caucasian'] == 1]
#X_african_american = X_test[X_test['African-American'] == 1]
#y_african_american = y_test[X_test['African-American'] == 1]

model_svm = pickle.load(open("justice", 'rb'))

prediction = model_svm.predict(X_all)
if prediction = 1:
  pred = "SHOULD NOT"
else
  pred = "SHOULD"
print(pred)