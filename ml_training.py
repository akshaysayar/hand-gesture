from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score 
from sklearn.metrics import confusion_matrix, precision_recall_curve, roc_curve, auc, log_loss
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

final_train = pd.read_csv("/home/akshay/data/personal/Python_projects/Hand_gesture/data/final_3.csv")
final_train.shape

# create X (features) and y (response)
X = final_train.drop("target",axis=1)
y = final_train['target']

# use train/test split with different random_state values
# we can change the random_state values that changes the accuracy scores
# the scores change a lot, this is why testing scores is a high-variance estimate
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1, random_state=2)

# check classification scores of logistic regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
# y_pred = logreg.predict(X_test)
# y_pred_proba = logreg.predict_proba(X_test)[:, 1]
# [fpr, tpr, thr] = roc_curve(y_test, y_pred_proba)
# print('Train/Test split results:')
# print(logreg.__class__.__name__+" accuracy is %2.3f" % accuracy_score(y_test, y_pred))
# print(logreg.__class__.__name__+" log_loss is %2.3f" % log_loss(y_test, y_pred_proba))
# print(logreg.__class__.__name__+" auc is %2.3f" % auc(fpr, tpr))


pickle.dump(logreg, open("/home/akshay/data/personal/Python_projects/Hand_gesture/models/basicLR_3.pkl", 'wb'))