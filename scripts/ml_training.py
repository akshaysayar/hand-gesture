from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score 
from sklearn.metrics import confusion_matrix, precision_recall_curve, roc_curve, auc, log_loss
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle,os

def train_model(inpoot,model_name):
    os.chdir(os.path.join(os.path.split(os.path.abspath(__file__))[0],".."))

    final_data = "data/" + inpoot
    model = "models/" + model_name

    final_train = pd.read_csv(final_data)
    print(final_train.shape)

    # create X (features) and y (response)
    X = final_train.drop("target",axis=1)
    y = final_train['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1, random_state=2)

    # check classification scores of logistic regression
    logreg = LogisticRegression(max_iter=10000)
    logreg.fit(X_train, y_train)
    pickle.dump(logreg, open(model, 'wb'))


if __name__ == "__main__":
    inpoot = "final_5.csv"
    model_name = "basicLR_5.pkl"
    train_model(inpoot,model_name)