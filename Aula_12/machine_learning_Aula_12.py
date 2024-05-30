import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_iris
iris = load_iris()

data = pd.DataFrame(data = np.c_[iris ['data'], iris ['target']], columns = iris['feature_names'] + ['target'])

display(data) # type: ignore
sns.pairplot(data)