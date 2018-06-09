import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os

srcPath = "/Users/juanalbertolahera/Projects/Kaggle/Titanic/input/"
print(os.listdir(srcPath))
from collections import Counter

data = pd.read_csv("/Users/juanalbertolahera/Projects/Kaggle/Titanic/input/train.csv")[["Survived", "Age", "Fare"]]
data = data.fillna(data.mean())
data.head()

passenger_id=pd.read_csv("/Users/juanalbertolahera/Projects/Kaggle/Titanic/input/test.csv")["PassengerId"]

test_data=pd.read_csv("/Users/juanalbertolahera/Projects/Kaggle/Titanic/input/test.csv")[["Age","Fare"]]
test_data=test_data.fillna(test_data.mean())
test_data.head()
test_data=test_data.values

import matplotlib.pyplot as plt
col=data["Survived"]
plt.scatter( x=data["Fare"],y=data["Age"], c=col)
plt.show()
