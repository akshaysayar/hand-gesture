from lazypredict.Supervised import LazyClassifier, LazyRegressor
import os, pandas as pd
from sklearn.model_selection import train_test_split


def check(inpoot):
    os.chdir(os.path.join(os.path.split(os.path.abspath(__file__))[0],".."))
    file = "data/"+inpoot
    final_train = pd.read_csv(file)
    final_train.shape

    # create X (features) and y (response)
    X = final_train.drop("target",axis=1)
    y = final_train['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.8, random_state=2)

    clf = LazyClassifier(predictions=True,verbose=0,ignore_warnings=True, custom_metric=None)
    models, predictions = clf.fit(X_train, X_test, y_train, y_test)
    print(models)


if __name__ == "__main__":
    inpoot = "final_3.csv"
    check(inpoot)