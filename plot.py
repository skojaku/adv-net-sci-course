import numpy as np 
import pandas as pd

df = pd.read_csv("test.csv")
A = np.zeros((11,11))
print(df)
A[(df["src"].values, df["trg"].values)] = 1
A = A+A.T
deg = np.array(A.sum(axis = 0)).reshape(-1)
print(np.sum(A)/A.shape[0])
print(np.sum(A @ np.diag(deg))/np.sum(A))

