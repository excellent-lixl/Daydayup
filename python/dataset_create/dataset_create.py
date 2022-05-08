from sklearn.datasets import make_classification
import logging
import numpy as np
import pandas as pd

n_samples=20000
n_features=100
n_classes=2
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info('Begin create data set.')
x,y = make_classification(n_samples=n_samples, n_features=n_features, n_informative=2,
                          n_redundant=2, n_repeated=0, n_classes=n_classes,
                          n_clusters_per_class=2, weights=None,
                          flip_y=0.01, class_sep=1.0, hypercube=True,
                          shift=0.0, scale=1.0, shuffle=True, random_state=None)
logging.info('Finish create data set.')
y=y.reshape(-1,1)
logging.info('Begin merge data set.')
data = np.concatenate([x, y], axis=1)
logging.info('Finish merge data set.')

np.savetxt("dataset.csv", data, delimiter=",")

header = ""
for i in range(n_features):
    header = header + "x{},".format(i)
header = header+"y\n"
print(header)
with open("dataset.csv", "r+") as f:
     old = f.read()
     f.seek(0)
     f.write(header)
     f.write(old)

